# Purpose-specific handoff and evidence

Read when a short note is insufficient. This is a documentation convention, not
a universal API, task registry, or access-control implementation.

Carry identity/use, actual producer/consumer/owner, exact artifact/revision/
representation/hash/span where relevant, effective contract, hard constraints,
existing authorization reference, dependencies, omissions, current evidence,
and next/stop conditions. Reference protected evidence through its authorized
custodian. Disclose a sanitized projection only to an allowed audience and
state what the projection omits and cannot prove.

Keep these questions separate:

| Question | Necessary evidence | Insufficient by itself |
|---|---|---|
| Is the record structurally valid? | Exact applicable schema and validation result | A plausible template or field names |
| Does the source support the claim? | Exact original/span, version, semantic context and permitted use | Matching hash alone |
| Did execution happen as claimed? | Trustworthy actual runner/object/environment/raw/stage record | Author's PASS statement or internally consistent summary |
| Was the intended object consumed and accepted? | Actual consumer selection and purpose-specific receipt; behavioral evidence where claimed | Sending, ACK, schema pass, or model self-report |
| Was it independently checked? | Non-author review of the exact object and oracle, with independence limits | Repeated agreement from the same source |

Do not hide missing dependencies behind a concise summary. Expand enough source
to close required definitions, negation, timing, and exceptions. If decisive
source cannot be obtained, limit the dependent claim. More text is not always
the remedy for a reasoning error: route an adequate-source interpretation
dispute to an appropriate reviewer/oracle owner.

If an effective contract requires full reading, a shorter view cannot waive it.
Do not impose an arbitrary compression ratio, context size, or cost claim.
Keep expected answers and private holdouts outside the evaluated model's input.

Reassess only dependencies that changed: a new consumer, audience, source,
permission, representation, oracle, or environment affects some claims without
invalidating every cached byte or unrelated judgment. R02 does not implement a
runtime context compiler or define a new production schema.
