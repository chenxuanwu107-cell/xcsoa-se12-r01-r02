# Public-candidate security, source and release audit

Date: 2026-11-03. Scope: this sanitized candidate tree and its newly created local
Git database. Maintainer self-review; not external independent security/legal
certification. Final exact commit/history results are retained by the local
custodian outside the publishable directory.

## Source integrity

Both requested primary archives were located and SHA256 matched:

- R01 W8, 2026-10-13 v0.1 candidate:
  `b8822ddc06456e05a86d0ac0f73bc62ecc8ced579a3b676235a798862d0e2a7d`.
- R02 W06-R8 FR1, 2026-10-15 v0.1 candidate:
  `54d56a1355b59556bd4c9dab5c03f1710d6e51f8c1ce54fb42f308863c33b31e`.

The current preparation independently checked top-level manifests/checksum
tables: R01 31/32 entries respectively, R02 703/704, with no mismatches.
Those are overlapping identity checks, not independent method tests. CRC and
bounded in-memory nested ZIP inspection executed without running archive code.
AppleDouble metadata files named like ZIPs were kept separate from actual ZIP
payloads; they are not evidence of corrupt requested archives.

The exact R01 and R02 original Method members were recovered, not recreated from
conversation summaries. Their identities and other selected source objects are
in the [source ledger](../provenance/SOURCE_LEDGER.json). The initial secondary
joint-audit snapshots matched those source identities; final packaging uses the
actual supplied primary archive chain. Current native authority is not inferred.

## Sanitization and Git scope

The publishable directory was created empty. Only new, selected text artifacts
were written. No internal .git directory, original archive, third-party source
tree, prototype Git fixture, runtime schema/configuration, database, credentials,
private chat/member record or raw research log was copied into it. Detailed
local paths and custody chains are kept outside this repository. Public source
hashes/titles identify research objects without revealing their private locations.

The checker scans candidate text for credential/private-key patterns, private
absolute paths, private platform IDs and non-reserved email addresses; validates
the full allowlisted file set; rejects symlinks/binaries; and inspects **all local
Git objects, including unreachable objects**, metadata and reflogs. A separate
negative control verifies that deleting a secret in a later commit is still
detected in old history. This is not an assertion that pattern matching detects
every possible secret or personal identity. The newly written prose was also
reviewed for internal architecture, source-rights and unintended disclosure.

Git uses an empty template, neutral automation identity, one new root history,
no remote, no inherited objects, no tags and no publishing hooks. No history
rewrite is offered as a substitute for an unsafe old repository. Final local
post-commit integrity/history and exact SHA are recorded separately by the
custodian; the bundled check report identifies its own pre-commit scope.

## Outcomes and limits

The [check report](check-results.json) records STATIC_CHECK_PASS only for its
stated scope. Test designs and examples do not establish model compliance.
METHOD_RESEARCH_CANDIDATE / MODEL_BEHAVIOR_NOT_RUN / HUMAN_REVIEW_PENDING remain.
The upstream research limits in [Research Status](../docs/RESEARCH_STATUS.md)
remain intact. No historical benchmark or synthetic result is claimed as this
release's effectiveness score.

The bundled skill-creator quick validator could not run in the default Python
environment because PyYAML is absent. No dependency was installed. A local
standard-library frontmatter/entrypoint validator and the release tests ran
instead; this does not mislabel the unavailable validator as PASS.

Legal/title clearance remains incomplete: see [rights audit](../legal/RIGHTS_AUDIT.md),
[license review](../legal/REVIEW.md), and [scenario FAQ](../legal/FAQ.md). No final
license is adopted. The enterprise restriction cannot retract applicable
GitHub-platform grants, including currently documented AI/affiliate rights.

No remote creation/push was performed. Git is available; GitHub CLI was absent
from the inspected command environment. Private-repository creation was not
authorized and no preview link exists. No credentials/auth-file contents were
read or printed to compensate. No Public visibility or GitHub Release action ran.

## Proposed repository metadata

- Name: `xcsoa-se12-r01-r02`
- Description: `Research-derived requirements and engineering handoff skills for independent professional use; custom source-available license candidate.`
- Topics: `requirements-engineering`, `engineering-coordination`, `handoff`,
  `agent-skills`, `source-available`, `research-candidate`
- Version: `v0.1.0-rc.1` (proposed only; no tag or release created)

Before public distribution: clear title/legal decisions, accept the applicable
platform implications, adopt the exact final license, establish a private
security contact, rerun checks on any changed bytes, and approve the exact final
commit plus the distinct actions of repository creation/visibility/release.
Research freeze and production/activation approval are separate questions.
