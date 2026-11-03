# Codex Quick Start / 复制文件夹即可安装

**Authorized local review only: HOLD_PUBLIC / LEGAL_REVIEW_REQUIRED.**
The license candidate is not effective. These steps grant no additional rights;
retain the source distribution's LICENSE, legal notices and research status.
Cloud use also needs an applicable cleared configuration; see
[personal use](PERSONAL_USE.md). No global configuration change is needed.

## Copy one complete folder

Copy `skills/r01-requirements` or `skills/r02-coordination` into your project's
`.agents/skills/`. Copy both folders to install both. Copy the **whole folder**,
including references, README, examples and test designs; do not flatten it or
copy only SKILL.md. Neither Skill requires the other or Xuanwu AI.

```text
your-project/
  .agents/skills/
    r01-requirements/
      SKILL.md
      references/handoff.md
      ...
    r02-coordination/
      SKILL.md
      references/handoff.md
      references/git-evidence.md
      ...
```

The following shell commands do the same copy. Replace both example paths.
Start with an absent destination; if a guard fails, stop and review the existing
installation rather than merging versions. Use real project directories; stop
if `.agents` or `.agents/skills` is a symlink. The destination guards also reject
symlinks.

```bash
cd "/path/to/your-project"
xcsoa_source="/path/to/xcsoa-se12-r01-r02"
test ! -L .agents && test ! -L .agents/skills && mkdir -p .agents/skills
```

R01 alone:

```bash
test ! -e .agents/skills/r01-requirements && test ! -L .agents/skills/r01-requirements && cp -R "$xcsoa_source/skills/r01-requirements" .agents/skills/
```

R02 alone:

```bash
test ! -e .agents/skills/r02-coordination && test ! -L .agents/skills/r02-coordination && cp -R "$xcsoa_source/skills/r02-coordination" .agents/skills/
```

For a combined installation, run both copy commands in the same project.
Do not run them again over an existing installation. Installed folders are
copies, not a second maintained source: change the source distribution and
replace an old local copy deliberately when updating. Project-local copies
avoid changing the user's global Skill set.

## Discover, then invoke

From that project, start the normal Codex CLI:

```bash
codex
```

Enter `/skills` **inside Codex**, not in the shell. Confirm the selected names
and project-local paths appear. Then type `$` to select a Skill, or begin the
request with `$r01-requirements` or `$r02-coordination`. Open the same project
in the desktop app if using that surface. If changes do not appear, restart the
session and check the project path and duplicate names. Do not change global
permissions to work around a failed initialization.

This layout and invocation syntax follow the official
[Build skills](https://learn.chatgpt.com/docs/build-skills) documentation.
YAML `name` and `description` are already present. `agents/openai.yaml` is
optional; no extra metadata, adapter, dependency installation or method copy is
needed for this packaging.

## Minimal review requests

Enter these as **Codex chat text**, after successful discovery. They are test
requests and expected properties, not recorded model outputs.

```text
$r01-requirements
Original request, demo-1: an offline inventory tool must use SQLite and never
upload customer records. Draft a short requirements note. Retention duration
is undecided. Ask only what changes the decision. Do not edit files or execute.
```

Check that offline, SQLite and no-upload remain binding, retention is not
invented, clarification stays focused, and no execution is claimed.

```text
$r02-coordination
Prepare a FOR_REVIEW handoff for two independent verification jobs sharing
one exclusive device controlled by the existing Operator. Planning only.
Evidence A: a test is designed; no invocation or output exists.
Evidence B: a supplied run record has raw output "4 passed" and exit 0.
Evidence C: a supplied run record has raw output "expected false; actual true"
and exit 1. Distinguish TEST_DESIGNED, TEST_EXECUTED and TEST_FAILED without
running anything, inventing a defect cause or claiming verification yourself.
```

Check independent work packages, device sequencing and the review-only handoff.
A is TEST_DESIGNED / execution NOT_RUN; B has supplied execution/pass evidence;
C has supplied execution/failure evidence. These records do not authorize a
rerun, repair or deployment, and supplied transcripts are not the assistant's
own executed tests. A simple request should still receive a simple answer.

## Actual verification limits

Complete-folder copying, frontmatter and relative-reference checks were run in
fresh R01-only, R02-only and combined projects. These are packaging checks.
The maintainer's native CLI still exits before initialization in the current
restricted environment; `/skills`, explicit invocation and new model behavior
are **NOT_RUN**, not compatibility PASS. No new professional qualification is
claimed by these instructions.

R01 W8 remains **HUMAN_FREEZE_PENDING**; R02 FR1 remains
**FROZEN_RESEARCH_CANDIDATE / NOT_ACTIVE**. Original behavior designs remain
NOT_RUN. The separate historical local smoke does not certify native Codex use.

Research-publication scope: the v0.1 candidate can be considered for publication
with Native Compatibility UNVERIFIED; the SQLite block is not a requirement to
rewrite the Skill or obtain a compatibility PASS before research distribution.
Rights, actual license adoption and exact publication approval remain separate
gates. G1 is confirmed for `chenxuanwu107-cell/xcsoa-se12-r01-r02`; it does not
authorize uploading this still-unlicensed candidate.
See [Roadmap](../ROADMAP.md) for the ten future positions; they are not dependencies.
