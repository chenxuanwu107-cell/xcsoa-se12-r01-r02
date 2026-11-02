# Combined use — synthetic, not executed

A freelancer is preparing a personal local draft for a paid customer. In this
illustration the individual retains control of the Skill, and the customer gets
only an ordinary requirements document. Eligibility under the proposed license
is separate from the assistant's data/action permission. The current candidate
still grants no new rights.

Original request, demo-3: “Prepare an offline inventory prototype. SQLite only;
no uploads. I want a reviewable plan first.”

**R01 expected note:** preserve SQLite, offline operation, no uploads and the
review-only phase. Propose observable local persistence and non-export checks,
marked NOT_RUN. Do not substitute response speed for correctness. Clarify record
requirements only if they change the reviewable plan. Version the requirements.

**R02 expected handoff:** consume that requirements note directly, define one
bounded draft work item with applicable checks, and identify the real reviewer
and FOR_REVIEW purpose. Keep implementation/testing/acceptance unobserved until
actual evidence exists. Do not create a twelve-role workflow, enterprise Skill
deployment, API access, or permission to send data. The customer can review and
request ordinary deliverable changes without controlling the Skill itself.

The seam is original wording → bounded requirements revision → plan and exact
consumer/use. It does not establish that either skill was loaded by a model,
used correctly, accepted, or effective. There is no combined-behavior PASS.
