# R02 examples — synthetic expected walkthroughs

These illustrations are not model outputs, execution receipts or real projects.

## One device, two tasks

Input: two logically independent checks need the same device; planning only is
authorized. Both tasks have sufficient inputs and the same existing resource owner.

Expected plan: retain two logical tasks, one resource wait, and the actual
admission owner. Do not infer simultaneous execution, draw a dependency cycle,
invent a capacity number, or claim permission to run. A short queue note is
enough. If the existing queue already satisfies this, NO_CHANGE is valid.

## Unexecuted candidate for review

Input: a reviewer explicitly requests a document at revision demo-2 FOR_REVIEW;
no product tests, delivery or review have occurred.

Expected handoff: identify exact document/revision, producer, intended reviewer,
purpose and constraints; execution NOT_RUN; prepared yes; sent/ACK/acceptance/
independent review not observed. It may later be accepted for review without
becoming a verified deliverable. Unknown use must instead remain unknown.

## Wrong oracle and missing first failure

Input: effective contract says an interval excludes its end; code returns false
at the end. A test expects true. A later run passed after changing that test,
but the first failing raw record was not retained.

Expected: route the oracle discrepancy to its owner; do not change correct code.
Keep code NO_CHANGE if appropriate. First failure MISSING, later run separately
identified, actual execution only as supported by trustworthy records. Do not
recreate A0, replace its identity with the later result, or claim independent
verification from author self-checks. A simple bounded note can preserve this.

Further negative controls: a wrapper exiting zero cannot hide a failed child;
zero discovered tests is not a pass. Reverting code cannot unsend a message or
restore divergent data. A rejection followed by acceptance stays one episode
with both events, and unfinished cases are not deleted from evaluation.
