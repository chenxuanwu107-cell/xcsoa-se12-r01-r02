# Quick Start / 快速开始

For authorized review now; future operation depends on an adopted license and
the user's own permissions. This local candidate supplies no new rights.

Pick one skill:

- **R01:** original wording → faithful requirements → acceptance intent → next
  consumer or bounded unknown. No R02 installation required.
- **R02:** goal/constraints → work boundaries → dependencies/resources →
  purpose-specific handoff → bounded failure/reopen if relevant. No R01 required.

Provide only authorized material. Include the actual intended use and audience,
relevant original source/version and existing permissions. Explain a concrete
decision, not merely “improve everything.” Clear tasks should remain short.

If your assistant supports local skill folders, use its configured location and
copy the selected directory there. Otherwise explicitly supply its SKILL.md and
only the references it calls for. Host-specific discovery and model behavior are
not tested by this repository. Preserve the root LICENSE, legal notices and
research status when making an otherwise authorized standalone copy; pending
redistribution rights must be resolved before distributing one to others.

Example R01 instruction:

```text
Use r01-requirements on the following original requirement, revision demo-1:
“Local-only storage using SQLite; do not send customer data outside this device.”
Purpose: requirements note for an authorized local draft, not deployment.
Keep constraints binding, propose refutable acceptance, and identify unknowns.
```

Example R02 instruction:

```text
Use r02-coordination. A candidate is ready for a reviewer, but no tests have run.
The recipient explicitly wants FOR_REVIEW. Prepare a short handoff and keep
execution, independent review and consumer acceptance states separate.
Planning only; no send, command execution or deployment is requested.
```

The expected approach is documented in the skills' examples. It is illustrative,
not evidence of output from a model. For static packaging checks, from this
repository's root run:

```bash
python3 -B tools/check_release.py
python3 -B -m unittest discover -s tests -v
```

No network or dependency installation is required by those checks. They inspect
this repository and its local Git objects, not your project or customer data.
The method tests remain NOT_RUN even when these commands succeed.
