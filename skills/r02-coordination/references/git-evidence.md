# Conditional Git evidence

Read only if the next decision depends on repository state or the link between
an accepted artifact and an actual engineering baseline. Inspection requires
the task's existing read permission; this document supplies none. Do not fetch,
install, run product tests, mutate Git/configuration, or broaden file access
merely to fill an evidence packet.

Choose the smallest relevant question:

- **Current facts:** exact authorized repository/worktree, view and literal scope.
- **Before work / after a stage:** accepted artifact → saved baseline or lawful
  reproducible recipe → actual consumer selection. The two times are distinct.
- **Failure inspection:** read an already preserved original; do not recreate A0.
- **Targeted refresh:** inspect only a decision-relevant omission or changed premise.

Distinguish commit objects, index, and working-tree bytes. Account for routing
and custom index/view overrides, replacement refs, alternates, shallow history,
and missing/promisor objects when relevant. An authorized custom view is valid
if explicitly bound to the expected task view. Changing directory alone does
not remove inherited routing overrides. Do not print environment values that
could contain credentials or private locators.

Object lookup can cause lazy fetching. Use protections supported by the actual
client or a justified equivalent; if protection is unavailable, stop the
dependent object lookup rather than remove it and retry. Missing local objects
remain missing. A metadata-only query needs its own bounded justification.
There is no universal command-safety or client-version qualification here.

A content hash proves only observed byte identity. It does not prove the right
repository/view, accepted baseline, actual consumer, permission, trusted
timestamp, complete backup, or execution authenticity. A report cannot attest
to its own execution. Keep command proposal, actual execution evidence, and
independent review distinct. Do not copy internal Git histories or fixtures
into a public deliverable. No runtime collector or historical prototype code is
included in this skill.
