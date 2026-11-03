#!/usr/bin/env python3
"""Local static release checks. No model, network, installation, or product run."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    "private_absolute_path": re.compile(r"/(?:Users|home|workspace|private|tmp)/[^\s\"'<>]+"),
    "windows_user_path": re.compile(r"\b[A-Za-z]:\\Users\\[^\s]+"),
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github_token": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    "cloud_access_key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "api_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "bearer_value": re.compile(r"(?i)Bearer\s+[A-Za-z0-9._~-]{16,}"),
    "credential_assignment": re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?token|password|secret)\s*[=:]\s*[\"']?[A-Za-z0-9_+/=-]{16,}"),
    "private_platform_id": re.compile(r"\b(?:ou_|oc_|cli_|libfile_)[A-Za-z0-9]{12,}\b"),
    "private_email": re.compile(r"\b(?!git@github\.com:)[A-Za-z0-9._%+-]+@(?!(?:[A-Za-z0-9.-]+\.)?(?:example|invalid)(?:\.[a-z]+)?\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
}
LINK = re.compile(r"!?\[[^\]\n]+\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")


def scan_text(label, text):
    """Report locations/rule IDs, never echo the matched secret."""
    return [{"file": label, "line": text.count("\n", 0, m.start()) + 1,
             "rule": rule} for rule, pattern in PATTERNS.items()
            for m in pattern.finditer(text)]


def public_files(root):
    files, issues = [], []
    def visit(directory):
        for p in sorted(directory.iterdir()):
            rel = p.relative_to(root).as_posix()
            if rel == ".git":
                if p.is_symlink() or not p.is_dir():
                    issues.append({"file": rel, "rule": "nonlocal_git_directory"})
                continue
            if p.is_symlink():
                issues.append({"file": rel, "rule": "symlink_forbidden"})
            elif p.is_dir():
                visit(p)
            elif p.is_file():
                files.append(p)
            else:
                issues.append({"file": rel, "rule": "special_file_forbidden"})
    visit(root)
    return files, issues


def anchor_ids(text):
    anchors, counts = set(), {}
    for title in re.findall(r"^#{1,6}\s+(.+)$", text, re.M):
        title = re.sub(r"[`*_]", "", title).lower()
        base = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
        count = counts.get(base, 0)
        counts[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def check_links(root, file, text):
    issues = []
    for match in LINK.finditer(text):
        target = match.group(1).strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme:
            if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
                issues.append({"file": file.relative_to(root).as_posix(), "rule": "unsafe_link"})
            continue
        path, _, anchor = unquote(target).partition("#")
        dest = (file.parent / path).resolve() if path else file.resolve()
        try:
            dest.relative_to(root.resolve())
        except ValueError:
            issues.append({"file": file.relative_to(root).as_posix(), "rule": "escaping_link"})
            continue
        if not dest.is_file():
            issues.append({"file": file.relative_to(root).as_posix(), "rule": "missing_link"})
        elif anchor and anchor not in anchor_ids(dest.read_text(encoding="utf-8")):
            issues.append({"file": file.relative_to(root).as_posix(), "rule": "missing_anchor"})
    return issues


def check_rights(ledger, names):
    """Validate evidence accounting, without adjudicating copyright or law."""
    issues = []
    records = ledger.get("files", [])
    paths = [r.get("path") for r in records]
    if len(paths) != len(set(paths)) or set(paths) != set(names):
        issues.append({"file": "rights-manifest.json", "rule": "rights_file_set_mismatch"})
    for record in records:
        required = ["content_parts", "evidence_refs", "unconfirmed_parts", "relicensing_basis"]
        if any(not record.get(k) for k in required):
            issues.append({"file": record.get("path", "rights-manifest.json"), "rule": "rights_basis_missing"})
            continue
        parts = record["content_parts"]
        if any(k not in parts for k in ["human_original_expression", "ai_assistance", "inherited_expression", "third_party", "factual_metadata"]):
            issues.append({"file": record["path"], "rule": "rights_categories_missing"})
        grant = record["relicensing_basis"]
        if grant.get("status") == "CLEARED" and not grant.get("title_evidence_refs"):
            issues.append({"file": record["path"], "rule": "unsupported_rights_clearance"})
        if grant.get("status") != "CLEARED" and not grant.get("missing_evidence"):
            issues.append({"file": record["path"], "rule": "unexplained_rights_unknown"})
    return issues


def git_run(root, args, data=None):
    env = {"PATH": "/usr/bin:/bin", "LC_ALL": "C", "GIT_CONFIG_NOSYSTEM": "1",
           "GIT_CONFIG_GLOBAL": os.devnull, "GIT_NO_REPLACE_OBJECTS": "1",
           "GIT_NO_LAZY_FETCH": "1", "GIT_TERMINAL_PROMPT": "0"}
    return subprocess.run(["git", "--no-optional-locks", "-c", "core.hooksPath=" + os.devnull,
                           "-c", "core.fsmonitor=false"] + args, cwd=root, env=env,
                          input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          check=True).stdout


def scan_git(root):
    if not (root / ".git").is_dir():
        return {"status": "NOT_INITIALIZED", "issues": [], "objects_scanned": 0}
    issues = []
    if git_run(root, ["rev-parse", "--show-prefix"]).strip():
        raise ValueError("not repository root")
    for name in ["objects/info/alternates", "shallow", "commondir"]:
        if (root / ".git" / name).exists():
            issues.append({"file": ".git/" + name, "rule": "inherited_git_storage"})
    # A normal clone of the published repository has an origin and release tags.
    # Keep rejecting other destinations; all objects, including tag objects, are scanned.
    allowed_origins = {
        "https://github.com/chenxuanwu107-cell/xcsoa-se12-r01-r02.git",
        "git@github.com:chenxuanwu107-cell/xcsoa-se12-r01-r02.git",
    }
    for remote in git_run(root, ["remote"]).decode().splitlines():
        urls = git_run(root, ["remote", "get-url", "--all", remote]).decode().splitlines()
        push_urls = git_run(root, ["remote", "get-url", "--push", "--all", remote]).decode().splitlines()
        if remote != "origin" or not urls or any(u not in allowed_origins for u in urls + push_urls):
            issues.append({"file": ".git/config", "rule": "unexpected_remote"})
    refs = git_run(root, ["for-each-ref", "--format=%(refname)"]).decode()
    if any(not r.startswith(("refs/heads/", "refs/tags/")) for r in refs.splitlines()):
        issues.append({"file": ".git/refs", "rule": "unexpected_ref"})
    listing = git_run(root, ["cat-file", "--batch-all-objects", "--batch-check=%(objectname) %(objecttype) %(objectsize)"])
    total = 0
    for row in listing.decode().splitlines():
        oid, kind, size = row.split()
        if int(size) > 1000000:
            issues.append({"file": "git-object:" + oid, "rule": "oversized_git_object"})
            continue
        raw = git_run(root, ["cat-file", kind, oid])
        total += 1
        if kind != "tree":
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                issues.append({"file": "git-object:" + oid, "rule": "binary_git_object"})
            else:
                issues.extend(scan_text("git-object:" + oid, text))
    # Include uncommitted config, ref logs, author/committer identities and messages.
    for folder in [root / ".git" / "logs"]:
        if folder.exists():
            for p in folder.rglob("*"):
                if p.is_file():
                    issues.extend(scan_text("git-metadata", p.read_text(errors="strict")))
    issues.extend(scan_text("git-config", (root / ".git/config").read_text()))
    roots = git_run(root, ["rev-list", "--all", "--max-parents=0"]).decode().splitlines()
    commits = git_run(root, ["rev-list", "--all"]).decode().splitlines()
    if len(roots) != 1 or not commits:
        issues.append({"file": ".git", "rule": "unexpected_history_roots"})
    git_run(root, ["fsck", "--full", "--strict"])
    return {"status": "PASS" if not issues else "FAIL", "issues": issues,
            "objects_scanned": total, "commit_count": len(commits), "root_count": len(roots),
            "scope": "all local objects including unreachable objects; metadata and reflogs"}


def check(root=ROOT):
    root = root.resolve()
    files, issues = public_files(root)
    names = {p.relative_to(root).as_posix() for p in files}
    manifest_path = root / "release-manifest.json"
    manifest = json.loads(manifest_path.read_text())
    expected = {r["path"]: r for r in manifest["files"]}
    if len(expected) != len(manifest["files"]) or names != set(expected) | {"release-manifest.json"}:
        issues.append({"file": "release-manifest.json", "rule": "file_set_mismatch"})
    links, jsons = 0, 0
    for p in files:
        rel = p.relative_to(root).as_posix()
        b = p.read_bytes()
        if len(b) > 300000 or p.suffix not in [".md", ".json", ".py", ""] and p.name != ".gitignore":
            issues.append({"file": rel, "rule": "unapproved_file_type_or_size"})
        if rel in expected and (hashlib.sha256(b).hexdigest() != expected[rel]["sha256"] or len(b) != expected[rel]["bytes"]):
            issues.append({"file": rel, "rule": "manifest_hash_mismatch"})
        try:
            text = b.decode("utf-8")
        except UnicodeDecodeError:
            issues.append({"file": rel, "rule": "binary_file"})
            continue
        if "\x00" in text:
            issues.append({"file": rel, "rule": "nul_in_text"})
        issues.extend(scan_text(rel, text))
        if p.suffix == ".md":
            links += len(LINK.findall(text))
            issues.extend(check_links(root, p, text))
        if p.suffix == ".json":
            json.loads(text)
            jsons += 1
        if p.suffix == ".py":
            compile(text, rel, "exec")
    for skill in ["r01-requirements", "r02-coordination"]:
        p = root / "skills" / skill / "SKILL.md"
        t = p.read_text()
        front = t.split("---", 2)
        if len(front) != 3 or not re.search(r"^name: " + re.escape(skill) + r"$", front[1], re.M) or not re.search(r"^description: .+", front[1], re.M):
            issues.append({"file": p.relative_to(root).as_posix(), "rule": "skill_frontmatter"})
        for section in ["Trigger", "Negative Trigger", "Input", "Procedure", "Output", "Failure", "Stop", "Tests"]:
            if "## " + section + "\n" not in t:
                issues.append({"file": p.relative_to(root).as_posix(), "rule": "missing_skill_section"})
        cases = json.loads((p.parent / "tests/cases.json").read_text())
        ids = set()
        for case in cases["cases"]:
            if case["id"] in ids or not case["input"] or not case["expected_properties"] or not case["forbidden_outcomes"] or case["result"] is not None or case["actual_output"] is not None or case["status"] != "NOT_RUN":
                issues.append({"file": "skills/" + skill + "/tests/cases.json", "rule": "invalid_test_design"})
            ids.add(case["id"])
    example = json.loads((root / "tests/example-records.json").read_text())
    source_map = {s["id"]: s for s in example["sources"]}
    for s in source_map.values():
        if hashlib.sha256(s["text"].encode()).hexdigest() != s["sha256"]:
            issues.append({"file": "tests/example-records.json", "rule": "example_source_hash"})
    for r in example["records"]:
        if r["source_sha256"] != source_map[r["source_id"]]["sha256"] or r["execution"] != "NOT_RUN" or r["consumer_acceptance"] != "NOT_OBSERVED" or r["independent_verification"] != "NOT_RUN" or r["outcome_claim"] is not None:
            issues.append({"file": "tests/example-records.json", "rule": "example_false_evidence"})
    issues.extend(check_rights(json.loads((root / "rights-manifest.json").read_text()), names))
    git = scan_git(root)
    issues.extend(git["issues"])
    return {"status": "STATIC_CHECK_PASS" if not issues else "STATIC_CHECK_FAIL",
            "files_checked": len(files), "markdown_links_checked": links,
            "json_files_parsed": jsons, "git": git, "issues": issues,
            "method_status": "METHOD_RESEARCH_CANDIDATE",
            "model_behavior": "NOT_EVALUATED_BY_STATIC_CHECKER", "upstream_model_behavior": "MODEL_BEHAVIOR_NOT_RUN",
            "human_review": "HUMAN_REVIEW_PENDING",
            "license_status": "CUSTOM_LICENSE / SOURCE_AVAILABLE / LEGAL_REVIEW_REQUIRED",
            "limitations": ["Pattern scans are bounded and not exhaustive.",
                "External URLs are not fetched by this checker.",
                "Static checks do not establish ownership, legal validity, method quality or model behavior."]}


if __name__ == "__main__":
    try:
        result = check()
    except Exception as exc:
        # No arbitrary source content or local exception path is printed.
        result = {"status": "STATIC_CHECK_FAIL", "rule": "checker_exception", "exception_type": type(exc).__name__}
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["status"] == "STATIC_CHECK_PASS" else 1)
