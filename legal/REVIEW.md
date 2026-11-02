# License and platform review

Reviewed for drafting on 2026-11-03. **LEGAL_REVIEW_REQUIRED**; no lawyer opinion,
enforceability certification, or established chain of title is asserted.

## Policy selection

The confirmed policy allows individual commercial work and paid independent
services for enterprise customers, with ordinary output rights for customers;
it withholds enterprise operation of the Skill itself. MIT, Apache-2.0,
CC BY-NC-SA and PolyForm Noncommercial are withdrawn as final recommendations.
No prior grant under those licenses was made in this candidate.

| Candidate | Relevant difference | Disposition |
|---|---|---|
| MIT | Broad use/distribution rights, including commercial use; notice retention; no express patent license | Cannot preserve the enterprise restriction. [License text](https://choosealicense.com/licenses/mit/) |
| Apache-2.0 | Broad individual/entity copyright grant, express contributor patent grant and patent-litigation termination, modified-file and applicable NOTICE obligations | Cannot preserve the enterprise restriction. [Official text](https://www.apache.org/licenses/LICENSE-2.0) |
| CC BY-NC-SA | A noncommercial condition does not express the intended unrestricted individual commercial work | Not recommended; not adopted. [Official deed](https://creativecommons.org/licenses/by-nc-sa/4.0/) |
| PolyForm Noncommercial | Noncommercial scope does not express this individual commercial / organizational operation distinction | Not recommended; not adopted. [Official text](https://polyformproject.org/licenses/noncommercial/1.0.0) |
| Custom candidate | Separates individual professional use, protected Skill and ordinary outputs; organizational operation excluded | Workable policy drafting direction; legal effectiveness and rights remain pending. |

The Open Source Definition requires free redistribution and prohibits
discrimination against persons/groups and fields of endeavor. The proposed
organizational restriction is incompatible with that positioning. Use
**SOURCE_AVAILABLE**, never an OSI-approved/open-source badge. This is a
classification inference, not an OSI review of this draft.
[OSI definition §§1, 3, 5–6](https://opensource.org/osd).

## Legal boundaries researched

These are limited comparative observations, not universal legal classifications.
The candidate's eligibility rules are proposed policy choices; tax and employment
labels do not decide contractual use rights automatically.

| Boundary | Primary evidence | Drafting consequence |
|---|---|---|
| US sole proprietor | The SBA distinguishes sole proprietorship from a separate business entity. [SBA](https://legacy.sba.gov/business-guide/launch-your-business/choose-business-structure) | A genuine natural-person business can qualify; do not treat every registered business as identical. |
| UK sole trader vs company | A limited company is legally separate from its owners. [GOV.UK](https://www.gov.uk/set-up-business) | One-person companies do not become natural persons; trading names alone need not disqualify. |
| PRC sole-proprietorship enterprise | Civil Code Article 102 lists personal sole-proprietorship enterprises among unincorporated organizations; unlimited liability is not the same as natural-person identity. [Civil Code, official source](https://www.spp.gov.cn/zdgz/202006/t20200602_463886.shtml), [Sole Proprietorship Law Article 2](https://scjgj.gz.gov.cn/zcfg/fl/content/post_9744783.html) | Do not automatically allow a Chinese enterprise by importing the English label “sole proprietorship.” Civil Code full-page access returned 403; the official indexed excerpt supports only this narrow classification. |
| PRC one-person company | Company Law Article 3 gives companies legal-person status; Article 42 permits a single shareholder. [SAMR current text](https://www.samr.gov.cn/djzcj/zcfg/fl/art/2026/art_9b4263a169cf43c2aba950cfc9ac1af2.html) | Separate entity remains outside the individual operational grant. |
| Contractors / employees | Actual agreement and working relationship matter; tax and employment statuses can differ. [Acas](https://www.acas.org.uk/employment-status), [GOV.UK](https://www.gov.uk/employment-status/selfemployed-contractor) | Contract name, private laptop, duration or location alone is insufficient. Keep legitimate freelance output services distinct from proxy operation. |
| Ideas vs expression | US 17 USC §102(b) excludes ideas, procedures, systems and methods of operation from copyright protection. [US Copyright Office statute](https://www.copyright.gov/title17/92chap1.html) | Restrict only rights actually held; do not promise ownership of professional methods or arbitrary similarity thresholds. Other laws/contract effects need separate review. |
| AI assistance | US Copyright Office Part 2 requires human authorship and treats human selection/modification separately from wholly generated expression; prompts alone generally do not establish authorship of outputs. [Official report, pp. 18, 24–27, 41](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) | Human authorship, employment/commission terms, provider terms and jurisdiction must be checked; AI drafting does not establish exclusive title. This is US-specific guidance. |

## GitHub hosting is a substantive approval decision

The currently retrieved GitHub Terms D.4 grant platform/affiliate rights,
including AI/ML development; D.5 grants platform viewing/forking rights to users.
J.3's AI-input opt-out does not remove D.4–D.8 rights or rights in public
repository content. The custom license cannot retract those grants. Account or
enterprise agreements may differ; none was inspected here.
[GitHub Terms D.3–D.5 and J.3](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service).

Thus the policy can withhold an additional enterprise operational license while
preserving platform/legal rights. It cannot truthfully promise that no company
receives any rights through public GitHub hosting. The owner must accept the
applicable platform terms or choose another distribution arrangement. No
repository or account settings were changed, and no platform acceptance was
performed by this task.

## Decisions before adoption

1. Verify licensor identity, publication authority and protected contributions
   per file; resolve the [rights audit](RIGHTS_AUDIT.md).
2. Select exactly one of the unselected S1/S2 alternatives in Sharing Options.
   GitHub-native platform rights cannot be excluded by this choice.
3. Confirm the proposed treatment of registered sole enterprises, incorporated
   solo businesses, ambiguous contractors and third-party hosted model processing.
4. Choose governing law, dispute forum/procedure, notice/contact, language priority,
   term/termination/remediation and any patent treatment with qualified counsel.
5. Review assent and enforceability, mandatory local protections, copyright vs
   contract conditions, and compatibility with platform/contributor agreements.
6. Approve an exact final license and exact sanitized release commit separately
   from research freeze, production use or active-system authorization.

These unresolved items are not filled with invented names, addresses or legal
assurances. Neither publication nor a static PASS can close them.

## Prepublication-1 revision scope

User decision: REVISE + HOLD_PUBLIC; remote creation, Public and Release are
expressly unauthorized. [Cloud processing](CLOUD_PROCESSING.md) proposes a
narrow technical-processing permission without a product-wide exemption.
[Sharing Options](SHARING_OPTIONS.md) leaves S1/S2 unselected;
[Platform Paths](PLATFORM_PATHS.md) separately leaves G1/G2 unselected.
[Risk Matrix](RISK_MATRIX.md) and the upgraded per-file rights manifest record
which evidence and legal decisions remain missing. Neither public product
documentation nor human research direction is proof of file-level title.
No root LICENSE adoption or professional-method change occurs in this revision.
