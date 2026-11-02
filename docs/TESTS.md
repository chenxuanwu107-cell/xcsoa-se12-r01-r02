# Tests and negative controls

`python3 -B tools/check_release.py` is a standard-library, local-only static
validator. It checks the exact manifest file set and hashes, text-only bounds,
relative Markdown links/anchors, skill frontmatter/required sections, parseable
JSON, test-design fields, example source hashes and truth-preserving example
records, sensitive-content patterns and all local Git objects/metadata.
Prepublication-1 also checks per-file rights-ledger coverage, required evidence
categories, and the presence of title evidence for any claimed clearance. This
validates accounting only; it does not determine whether the evidence grants rights.
It reports STATIC_CHECK_PASS only for that scope. It cannot prove absence of
every secret, semantic method equivalence, ownership, or professional behavior.

`python3 -B -m unittest discover -s tests -v` exercises scanner detection of
synthetic secret/private-path inputs, missing/escaping links, symlink rejection,
and a harmless synthetic secret hidden only in an older Git commit. Fixtures
are generated in temporary directories; their credential strings are fake and
are not copied into this repository. The history control demonstrates why
deleting a current file does not sanitize prior commits. This is a test of the
release checker, not a security certification or model evaluation.
Two additional controls reject an omitted rights-ledger file and a claimed
clearance with no title evidence. They do not adjudicate copyright validity.

The JSON cases within each skill are newly worded exposed scenario designs with
source references, inputs, expected properties, forbidden outcomes and null
results. They are MODEL_BEHAVIOR_NOT_RUN. The example records are synthetic
data checked for internal identity/state consistency, not real receipts.

To run behavioral tests later: freeze the exact candidate, source conditions,
unseen tasks where appropriate, allowed outcomes, independent oracle, runner,
model configuration and budget before collecting outputs. Retain raw outputs,
all attempts/failures/timeouts/refusals, author versus independent reviews, and
consumer-purpose evidence. Do not merge denominators across reruns or count
duplicate sources/agents as independent experiments.

Links: local links and anchors are checked mechanically; the external official
legal/platform links were fetched during preparation with specific failures
recorded in the link report. No broad “all URLs pass” or ongoing availability
claim is made. The release checker makes no network requests.
