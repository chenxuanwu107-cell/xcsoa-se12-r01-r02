# XCSOA SE12 — R01 与 R02

两个可独立使用的研究方法 Skill：需求工程，以及工程协调与交接。
无需安装玄武 AI，也不要求十二岗位串联。

**本地发行候选 · v0.1.0-rc.1 · 尚未公开发布**

**CUSTOM_LICENSE / SOURCE_AVAILABLE / LEGAL_REVIEW_REQUIRED**

[English](README.md) · [快速开始](docs/QUICK_START.md) ·
[研究状态](docs/RESEARCH_STATUS.md) · [安全与发行审计](reports/RELEASE_AUDIT.md)

| Skill | 解决的问题 | 入口 |
|---|---|---|
| R01 需求工程 | 保留原意和硬约束、有限澄清、可反驳验收意图 | [SKILL](skills/r01-requirements/SKILL.md) · [独立说明](skills/r01-requirements/README.md) |
| R02 工程协调与交接 | 可消费计划、依赖与资源、用途化交接、按失败对象有界重开 | [SKILL](skills/r02-coordination/SKILL.md) · [独立说明](skills/r02-coordination/README.md) |

普通明确任务使用短记录；只有当前决定确实需要时才展开参考。两个 Skill 可组合：
R01 输出需求说明，R02 按实际接收者与用途组织计划。这里不提供调度器、执行平台、
授权服务或模型，也不自动激活任何现役系统。

## 快速开始

当前候选未授予新的使用权。以下供已获权审阅者，或许可证正式采用后的合格使用者参考：

1. 阅读所选 Skill 的 `SKILL.md`，按需读取其内部参考。
2. 提供原始需求、相关来源版本、受众、消费用途和已有动作权限。
3. 请求最小充分输出，未运行的检查保留 NOT_RUN。

```text
使用 r02-coordination。两个互不依赖的测试任务共用一台设备。
请给出资源等待与执行许可分开的短计划；不要把资源争用写成逻辑循环。
当前只允许规划，不运行测试。
```

支持目录式 Skill 的宿主可将所选 Skill 目录复制到其配置的安装位置。
发现与调用方式由宿主决定，本包没有安装脚本，不修改宿主设置。独立副本仍适用
根许可证与研究限制。[详细说明](docs/QUICK_START.md)。

[R01 示例](skills/r01-requirements/examples.md)、[R02 示例](skills/r02-coordination/examples.md)
与[组合示例](docs/COMBINED_EXAMPLE.md)均为合成预期演示，不是真实客户记录或模型实测。

## 研究与质量状态

- R01 W8 仍待 **Human Freeze**；原始核心保留，W4 三项补丁未采用。
- R02 FR1 保持 **FROZEN_RESEARCH_CANDIDATE / NOT_ACTIVE**；五步核心不变。
- **METHOD_RESEARCH_CANDIDATE / HUMAN_REVIEW_PENDING**；上游行为资格仍为 NOT_RUN，新发生的有限本地 Smoke 单独报告。
- [静态检查](docs/TESTS.md)的实际结果见[检查报告](reports/check-results.json)。

公开发行不等于生产资格、真实效果验证、模型遵从或现役玄武 Skill 激活。
没有 Benchmark 分数、通过率、用户数量或效果提升声明。

## 许可政策候选

拟采用 `XCSOA Individual & Independent Professional Use License`：允许个人商业项目、
独立开发者及自由职业者接企业付费订单并交付普通工作成果；企业可正常使用、修改、
出售或许可合法成果。成果不得夹带 Skill 本体、其受保护内容的实质性复制或运行访问权。
企业部署、员工代表企业运行、企业 API、组织集成及代理规避不在授权范围内。

本项目定位为 **Source-Available，不是 OSI Open Source**。企业可阅读公开资料，
但不因此取得超出平台条款及法定例外的 Skill 商业运行权。当前 GitHub 条款另含平台及
关联方 AI 权利，定制许可不能撤销；详见[法律审查](legal/REVIEW.md)。

[根 LICENSE](LICENSE)保持待批准。[英文许可候选](legal/LICENSE-CANDIDATE.en.md)、
[中文参考译文](legal/LICENSE-CANDIDATE.zh-CN.md)及[场景 FAQ](legal/FAQ.md)尚未经律师审核。
MIT、Apache-2.0、CC BY-NC-SA、PolyForm Noncommercial 均不作为最终建议或已采用许可。
实际权利归属及可执行性尚待核实。

## 来源与维护

[来源清单](provenance/SOURCE_LEDGER.json)、[适配映射](provenance/ADAPTATION.md)及
[权利审计](legal/RIGHTS_AUDIT.md)记录范围。原始研究归档、论文书籍、第三方代码、
私人聊天、凭据、数据库和未公开生产架构均未收录。

[安全政策](SECURITY.md) · [贡献规则](CONTRIBUTING.md) · [变更记录](CHANGELOG.md)。
未创建远程仓库，未推送、发布 Release 或设置 Public。

Prepublication review 2 / 发布前修订 2：**ACCEPT_REVISION_FOR_REVIEW + HOLD_PUBLIC**。
[Cloud processing / 云端边界](legal/CLOUD_PROCESSING.md) ·
[Sharing / S2 拟议优先（未生效）](legal/SHARING_OPTIONS.md) ·
[Distribution / G2 保守研究路径（非平台选择）](legal/PLATFORM_PATHS.md) ·
[Legal and rights risk matrix / 风险矩阵](legal/RISK_MATRIX.md)。
No remote creation, Public or Release is authorized.

[Personal-use guide / 个人使用说明](docs/PERSONAL_USE.md) ·
[Actual isolated local acceptance / 本地验收实测](reports/PREPUBLICATION_2.md)。
Frozen research labels remain historical qualification limits; the new local
smoke is separate evidence, with native Codex Discovery still blocked.
