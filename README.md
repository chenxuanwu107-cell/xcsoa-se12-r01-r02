# XCSOA SE12 — R01 & R02

Two independently usable research-derived skills for requirements engineering
and engineering coordination/handoff. No Xuanwu AI installation is required.

**LOCAL RELEASE CANDIDATE · v0.1.0-rc.1 · NOT PUBLISHED**

**CUSTOM_LICENSE / SOURCE_AVAILABLE / LEGAL_REVIEW_REQUIRED**

[中文](README.zh-CN.md) · [Quick Start](docs/QUICK_START.md) ·
[Research status](docs/RESEARCH_STATUS.md) · [Audit](reports/RELEASE_AUDIT.md)

| Skill | Use it for | Start here |
|---|---|---|
| R01 Requirements Engineering | Faithful constraints, bounded clarification, acceptance intent | [Skill](skills/r01-requirements/SKILL.md) · [Guide](skills/r01-requirements/README.md) |
| R02 Engineering Coordination & Handoff | Consumable plans, resources, purpose-specific handoffs, bounded replanning | [Skill](skills/r02-coordination/SKILL.md) · [Guide](skills/r02-coordination/README.md) |

Use either skill alone. For combined work, R01 produces a bounded requirements
note and R02 consumes it to plan or hand off. A clear ordinary task stays short;
there is no mandatory twelve-role chain. The repository contains instructions
and static release checks, not a scheduler, runtime, authority service, or model.

## Quick start

This candidate grants no new use rights until the verified licensor adopts the
license. The following is an installation/use example for an authorized reviewer
or a future eligible user after adoption.

1. Read the chosen `SKILL.md` and its local references when relevant.
2. Give the assistant the original request, relevant source revisions, audience,
   intended use, and existing action permissions.
3. Ask for the smallest sufficient output and mark proposed checks NOT_RUN.

Example request:

```text
Use r01-requirements. This personal offline tool must use SQLite and must not
upload customer data. Prepare acceptance intent for a local draft only.
Preserve those hard constraints; identify only decision-relevant unknowns.
```

For a host supporting directory-based skills, copy only the chosen skill folder
into the host's configured skill location. The host determines discovery and
invocation. No install script or host configuration change is included. The
root license and research limits remain applicable to standalone copies.

See [R01 examples](skills/r01-requirements/examples.md),
[R02 examples](skills/r02-coordination/examples.md), and
[the combined example](docs/COMBINED_EXAMPLE.md). These are synthetic expected
walkthroughs, not observed model runs or real customer cases.

## Status and checks

- R01 W8: **HUMAN_FREEZE_PENDING**. Original method retained; W4 patches not adopted.
- R02 FR1: **FROZEN_RESEARCH_CANDIDATE / NOT_ACTIVE**, five-step core retained.
- **METHOD_RESEARCH_CANDIDATE / MODEL_BEHAVIOR_NOT_RUN / HUMAN_REVIEW_PENDING**.
- Static checks are described in [Tests](docs/TESTS.md); their actual results are
  in [the check report](reports/check-results.json).

Public distribution would not establish production qualification, real-world
benefit, or activation of an existing Xuanwu skill. No benchmark score, success
rate, adoption count, or professional effectiveness result is claimed.

## Proposed license

The proposed **XCSOA Individual & Independent Professional Use License** permits
individual commercial projects and independent freelancers serving paid
enterprise clients, while withholding organizational operational use of the
Skill. Customers can use and commercialize ordinary deliverables that do not
contain substantial protected Skill content or provide runtime access.
Employee use for an employer, corporate APIs, managed deployment/integration,
and proxy operation are outside that grant.

This is **source-available**, not OSI Open Source. Public reading does not grant
additional enterprise operational rights; applicable platform rights and legal
exceptions remain. The current GitHub terms include platform and affiliate AI
rights that this license cannot remove; see [legal review](legal/REVIEW.md).

The root [LICENSE](LICENSE) is pending. Read the [English candidate](legal/LICENSE-CANDIDATE.en.md),
[Chinese reference translation](legal/LICENSE-CANDIDATE.zh-CN.md), and
[scenario FAQ](legal/FAQ.md). MIT, Apache-2.0, CC BY-NC-SA, and PolyForm
Noncommercial are not final-license recommendations or adopted alternatives.
Rights ownership and legal enforceability remain to be reviewed.

## Provenance and maintenance

[Source ledger](provenance/SOURCE_LEDGER.json),
[adaptation map](provenance/ADAPTATION.md), and
[rights audit](legal/RIGHTS_AUDIT.md) distinguish exact source identities from
the public adaptation. Original archives, third-party texts/code, private logs,
credentials, databases, and internal architecture are excluded.

Read [Security](SECURITY.md), [Contributing](CONTRIBUTING.md), and
[Changelog](CHANGELOG.md) before proposing changes. No remote repository,
GitHub Release, public visibility change, or operational activation is authorized
by these documents.
