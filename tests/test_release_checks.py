"""Negative controls for packaging checks; not professional-skill tests."""
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest


spec = importlib.util.spec_from_file_location("release_check", Path(__file__).resolve().parents[1] / "tools/check_release.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class ReleaseCheckerControls(unittest.TestCase):
    def test_fake_credential_detected_without_echo(self):
        fake = "gh" + "p_" + "SYNTHETIC" * 4
        findings = checker.scan_text("fixture", fake)
        self.assertIn("github_token", [f["rule"] for f in findings])
        self.assertNotIn(fake, str(findings))

    def test_private_locator_detected(self):
        fake = "/" + "Users" + "/synthetic-person/private-note"
        self.assertIn("private_absolute_path", [f["rule"] for f in checker.scan_text("fixture", fake)])

    def test_public_hash_and_reserved_identity_are_legal(self):
        self.assertEqual(checker.scan_text("fixture", "a" * 64 + "\nrelease-candidate@invalid.example"), [])
        self.assertEqual(checker.scan_text("fixture",
            "git@github.com:chenxuanwu107-cell/xcsoa-se12-r01-r02.git"), [])

    def test_missing_and_escaping_links(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            p = root / "README.md"
            p.write_text("test")
            text = "[missing](absent.md) [escape](../outside.md)"
            rules = {f["rule"] for f in checker.check_links(root, p, text)}
            self.assertEqual(rules, {"missing_link", "escaping_link"})

    def test_valid_anchor(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            p = root / "README.md"
            p.write_text("# Local heading\n")
            self.assertEqual(checker.check_links(root, p, "[here](#local-heading)"), [])

    def test_symlink_rejected_without_read(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "redirect").symlink_to("nonexistent")
            files, findings = checker.public_files(root)
            self.assertEqual(files, [])
            self.assertEqual(findings[0]["rule"], "symlink_forbidden")

    def test_rights_inventory_cannot_omit_a_file(self):
        findings = checker.check_rights({"files": []}, {"one.md"})
        self.assertIn("rights_file_set_mismatch", [r["rule"] for r in findings])

    def test_claimed_clearance_requires_title_evidence(self):
        record = {"path": "one.md", "content_parts": {k: "not established" for k in
            ["human_original_expression", "ai_assistance", "inherited_expression", "third_party", "factual_metadata"]},
            "evidence_refs": ["observed-generation"], "unconfirmed_parts": ["actual title"],
            "relicensing_basis": {"status": "CLEARED", "title_evidence_refs": []}}
        findings = checker.check_rights({"files": [record]}, {"one.md"})
        self.assertIn("unsupported_rights_clearance", [r["rule"] for r in findings])

    def test_removed_secret_still_detected_in_history(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            template = root / "empty-template"
            template.mkdir()
            def git(*args):
                return checker.git_run(root, ["-c", "user.name=Fixture Builder", "-c",
                    "user.email=fixture@invalid.example"] + list(args))
            git("init", "--template=" + str(template), "--initial-branch=main")
            fake = "gh" + "p_" + "HARMLESSFIXTURE" * 3
            p = root / "removed.txt"
            p.write_text(fake)
            git("add", "removed.txt")
            git("commit", "-m", "synthetic first state")
            p.unlink()
            git("add", "-u")
            git("commit", "-m", "remove synthetic fixture from current tree")
            report = checker.scan_git(root)
            self.assertEqual(report["status"], "FAIL")
            self.assertIn("github_token", [f["rule"] for f in report["issues"]])
            self.assertEqual(report["commit_count"], 2)

    def test_published_origin_and_tags_keep_security_checks(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            template = root / "empty-template"
            template.mkdir()
            def git(*args):
                return checker.git_run(root, ["-c", "user.name=Fixture Builder", "-c",
                    "user.email=fixture@invalid.example"] + list(args))
            git("init", "--template=" + str(template), "--initial-branch=main")
            (root / "README.md").write_text("# Synthetic published fixture\n")
            git("add", "README.md")
            git("commit", "-m", "synthetic published state")
            git("tag", "-a", "v0.0.0-fixture", "-m", "synthetic release")
            git("remote", "add", "origin",
                "https://github.com/chenxuanwu107-cell/xcsoa-se12-r01-r02.git")
            git("update-ref", "refs/remotes/origin/main", "HEAD")
            git("symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main")
            self.assertEqual(checker.scan_git(root)["status"], "PASS")
            git("remote", "set-url", "origin",
                "git@github.com:chenxuanwu107-cell/xcsoa-se12-r01-r02.git")
            self.assertEqual(checker.scan_git(root)["status"], "PASS")
            git("remote", "set-url", "--push", "origin", "https://example.invalid/other.git")
            findings = checker.scan_git(root)["issues"]
            self.assertIn("unexpected_remote", [f["rule"] for f in findings])
            fake = "gh" + "p_" + "HARMLESSTAGFIXTURE" * 3
            git("tag", "-a", "v0.0.1-fixture", "-m", fake)
            findings = checker.scan_git(root)["issues"]
            self.assertIn("github_token", [f["rule"] for f in findings])


if __name__ == "__main__":
    unittest.main()
