# 语音代理评估语料库与 TRG 评估流程

[English](README.md) | **简体中文**

[![CI](https://github.com/shivamnegi92/voice-agent-eval-corpus/actions/workflows/validate.yml/badge.svg)](https://github.com/shivamnegi92/voice-agent-eval-corpus/actions/workflows/validate.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22924302.svg)](https://doi.org/10.5281/zenodo.22924302)
[![arXiv](https://img.shields.io/badge/arXiv-2609.30798-b31b1b.svg)](https://arxiv.org/abs/2609.30798)
[![HF Space](https://img.shields.io/badge/%F0%9F%A4%97%20Space-TRG%20demo-blue)](https://huggingface.co/spaces/shivamnegi92/trg-voice-agent-eval)

本项目包含一个经过核验、可复现的实时语音代理研究元数据语料库，以及 **TRG**（Timing、Recovery、Grounded：时序、恢复、结果依据）最低报告规范、合规检查器和基线对照表。

**v1.2.0（2026-11-16）：140 篇来源，其中 136 篇主要研究、3 篇定位文献、1 篇方法文献；截止日期为 2026-10-02。**
语料包含 91 篇评估研究和 11 篇元评估研究，报告规范为 TRG v2。
新增的 [TRG-Ref 0.1](protocol/README.md) 是可选的测量协议与离线分析工具；
示例日志仅为合成软件测试数据，不是新的语音代理实验结果。

**arXiv 替换稿仍待作者上传。** 当前在线预印本尚未与此版本同步。
Zenodo 概念 DOI 也可能仍指向 v1.1.1；复现时请固定
[v1.2.0 发布版本](https://github.com/shivamnegi92/voice-agent-eval-corpus/releases/tag/v1.2.0)
及其校验清单，参见 [发布状态](RELEASE_STATUS.md) 和 [更新记录](CHANGELOG.md)。

**无需安装即可试用：**[Hugging Face TRG 演示](https://huggingface.co/spaces/shivamnegi92/trg-voice-agent-eval)

配套论文：[Evaluating Real-Time Voice Agents: From Component Quality to Grounded Outcomes](https://arxiv.org/abs/2609.30798)（arXiv 预印本，尚未同行评审）。语料库和工具版本、来源数量及截止日期可能变化，请以[英文主 README](README.md)和版本记录为准；概念 DOI 用于查找版本系列，精确复现请使用版本标签、提交或版本 DOI；概念 DOI 为 [10.5281/zenodo.22924302](https://doi.org/10.5281/zenodo.22924302)。

## 为什么需要它

实时语音代理研究分散在语音基础模型、轮流对话研究和代理评估等领域。论文也经常只报告延迟、轮流准确率或任务成功率中的某一项，难以横向比较。本仓库提供结构化文献元数据和 TRG 报告框架，帮助揭示报告中缺失的评估维度。

## 仓库内容

- `corpus/`：CSV/JSON 元数据、字段 schema、来源核对记录、许可审计和生成的 leaderboard。
- `trg_eval/`：可安装的 Python 校验与 leaderboard 工具。
- `scripts/`：下载并校验语料副本、验证 TRG 报告和重建对照表的命令行工具。
- `trg/`：报告模板及不同系统的示例报告。
- `hf_space/`：静态 Pyodide 演示页面。

## 为什么不提供论文 PDF

仓库只发布研究元数据，不分发论文 PDF。对于来源论文，授权范围可能不允许再发布。你可以从原始来源下载，并使用仓库提供的 SHA-256 哈希核对文件：

```bash
python3 scripts/fetch_corpus.py
python3 scripts/fetch_corpus.py --verify-only
```

哈希不匹配可能是原作者更新了论文版本，并不一定是文件损坏；但它表示文件字节与本次整理时检查的版本不同。请阅读 `corpus/licence_audit.csv` 与英文 README 的许可说明。论文、数据集及模型各自保留其原有许可。

## TRG：时序、恢复与有依据的结果

TRG 要求在适用情况下同时报告各维度，而不是只选择最有利的一项：

| 维度 | 报告要求 |
|:--|:--|
| **T — Timing（时序）** | 报告延迟、时钟锚点、单位和统计方式；适用时说明上下文相关的响应时机及测量协议。 |
| **R — Recovery（恢复）** | 在观察到中断后，单独报告对话或任务状态的恢复情况，避免与无中断表现混为一谈。 |
| **G — Grounded outcome（有依据的结果）** | 通过外部证据核验已授权的结果；包括合理的不采取行动，以及资格政策和动作/状态证据。 |
| **M — Multiparty（多方，条件适用）** | 多个参与者均有正当权限时，报告发言与沉默是否恰当、是否漏掉介入，以及披露/行动是否遵循权限。 |

检查器验证报告结构，不会验证证据真实性、分数质量，也不能覆盖完整的安全与治理审查。TRG 规定需呈现哪些维度，并不指定唯一指标；未报告的适用项目不能靠虚构数值补齐。

### 校验报告

```bash
cp trg/trg_report_template.yaml my_report.yaml
# 编辑 my_report.yaml
python3 scripts/validate_trg.py my_report.yaml
```

合规时退出码为 0，不合规时为 1，可用于 CI。也可以安装为包：

```bash
pip install -e .
trg-validate my_report.yaml
trg-leaderboard
```

已有示例报告保留来源中的旧格式和警告；不会为了让维度看起来完整而凭空补造测量值。

## 基线对照表

仓库提供不同语音代理的 TRG 报告覆盖情况与可比数值。对照表不把所有系统压成一个总分；比较时应确认系统是否在相同条件下测量，并留意哪些维度没有数据。完整生成表见 [`corpus/leaderboard.md`](corpus/leaderboard.md)。

## 来源、完整性与研究限制

语料库记录来源元数据、标识符和哈希，并通过人工核验降低自动匹配错误。搜索流程结合候选文献、定向文献追踪和数据库查询，但**不是对所有数据库的穷尽式统计**。来源数量、纳入范围和研究截止日期请以英文主 README、`corpus/reconciliation.md` 和当前发布版本为准。

## 引用与许可

- 论文仍是**尚未同行评审的 arXiv 预印本**；引用格式见英文版 [Citing](README.md#citing) 和 `CITATION.cff`。
- `corpus/` 数据采用 **CC BY 4.0**。
- `scripts/` 代码采用 **MIT**，详见 `LICENSE-CODE`。
- 本仓库许可不改变来源论文自身的使用条款。

## 参与贡献

欢迎纠正语料条目、提交 TRG 报告或讨论尚未覆盖的评估维度。可从 [GitHub Discussions](https://github.com/shivamnegi92/voice-agent-eval-corpus/discussions) 开始。完整字段、发布历史和研究细节请参阅[英文版 README](README.md)。
