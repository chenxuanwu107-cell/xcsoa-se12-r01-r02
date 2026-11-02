# Security policy

This is an instruction/documentation research candidate, not a security boundary
or runtime enforcement layer. No supported production version or response SLA
is established. Model instructions must not be relied on as access control.

Report permission expansion, secret/private-source disclosure, fabricated
execution/acceptance, unsafe source interpretation, or release-checker defects
using a minimal synthetic reproduction. Include the exact version, expected
boundary, observed result and impact; do not post credentials, private chats,
customer records, unpublished architecture, or original internal archives.

No remote repository or private reporting endpoint currently exists. For review,
use the already authorized private channel with the maintainer. Do not open a
public issue with sensitive evidence. Before public publication, establish and
verify a private reporting channel. GitHub private vulnerability reporting is
available to public-repository administrators when enabled; it has not been
enabled here. [Official configuration guide](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).

Maintainers should preserve the first report, use bounded authorized evidence,
review the exact change with a non-author where possible, and keep unknowns
visible. Do not request full private logs or claim independent verification from
an author self-check. If a secret enters history, deletion from the latest tree
alone is insufficient; assess the affected history and rotate a real exposed
credential through its owner. Publication requires a fresh audit and approval.
