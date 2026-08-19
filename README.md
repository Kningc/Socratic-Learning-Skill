# Socratic Learning

一个遵循开放 [Agent Skills](https://agentskills.io/) 规范的通用苏格拉底学习 Skill。它不依赖特定模型、Agent、IDE、工具或运行时，可以围绕教材、论文、笔记、代码、题目、图像或音视频资料，通过自适应提问、分级提示、检索练习和迁移测试帮助学习者形成可验证的理解。

The core skill is agent-agnostic and written in the portable `SKILL.md` format. The same package works with hosts that implement Agent Skills, with a context-loading fallback for other agents.

## 特点

- 以用户资料为主要课程，并标明资料内外的信息边界
- 每轮聚焦一个认知动作，依据回答动态调整难度
- 支持概念、数理与代码、论证文本、论文数据、语言记忆、多媒体和项目材料
- 卡住时逐级增强提示；需要时直接讲解，不把“苏格拉底式”变成障碍
- 通过解释、迁移、辨析和延迟回顾判断掌握情况
- 可选的整本书/长期课程模式，包含课程地图、复习队列、实验记录和累计评估
- 单次学习默认不持久化；长期状态仅在用户要求或同意后创建
- 首次启动先推断上下文，只逐个询问真正影响路线或写入权限的信息
- 版本化课程状态，支持并发冲突检测、迁移、暂停、导出、重置和删除
- 将教材与网页中的指令性文字视为学习材料，防止提示注入越权
- 用证据类型和提示支持程度校准掌握判断
- 核心协议不包含任何平台专用工具名称或调用语法

## 支持的 Agent

同一份 Skill 可原生用于：

- OpenAI Codex
- Claude Code and Claude Agent SDK
- Cursor
- GitHub Copilot coding agent, CLI, and IDE agent mode
- Gemini CLI
- Windsurf Cascade
- Cline
- OpenCode

这些宿主采用相同的 `SKILL.md` 核心格式，仅安装目录和手动调用语法有所不同。完整路径见[兼容与安装指南](references/compatibility.md)。

## 安装

把仓库克隆到目标 Agent 的 skills 根目录，并确保最终目录名为 `socratic-learning`：

```bash
git clone https://github.com/Kningc/Socratic-Learning-Skill.git <skills-root>/socratic-learning
```

覆盖最多宿主的个人级安装位置是：

```bash
git clone https://github.com/Kningc/Socratic-Learning-Skill.git ~/.agents/skills/socratic-learning
```

`.agents/skills` 目前可被 Cursor、GitHub Copilot、Gemini CLI、Windsurf 和 OpenCode 发现。Claude Code、Codex、Cline 等宿主可使用兼容指南中的原生目录。

## 使用

安装后可通过宿主的自动发现机制或 Skill 名称调用。以下自然语言请求在所有宿主中都适用：

```text
Use the socratic-learning skill to help me learn the attached chapter. I want to understand it well enough to apply it, and please teach in Chinese.
```

例如：“根据这篇论文，用苏格拉底学习法带我理解实验设计。”

如果 Agent 尚未原生支持 Skills，请把本仓库作为上下文提供，并要求它先读取 `SKILL.md`。无需转换核心提示词。

## 验证

运行跨平台结构验证：

```bash
python3 scripts/validate_skill.py
```

验证器检查 Skill/状态版本一致性、状态 Schema、相对链接以及行为案例格式。`evals/cases.json` 定义了可用于各 Agent 实际前向评测的输入、环境、必须行为、禁止行为和预期写入；验证器本身不会假装判断模型输出是否合格。

## 文件

- `SKILL.md`：跨 Agent 的核心教学协议
- `references/material-playbooks.md`：不同资料类型的适配策略
- `references/long-form-course.md`：整本书和长期课程的编排、复习、实验及评估协议
- `references/state-management.md`：状态 Schema、迁移、并发写入和数据生命周期
- `references/mastery-rubrics.md`：掌握证据、支持程度和完成判定标准
- `references/safety-and-source-boundaries.md`：材料提示注入、命令和隐私边界
- `references/evidence.md`：设计依据与来源说明
- `references/compatibility.md`：各主流 Agent 的安装与调用方式
- `assets/course-state/`：获准启用长期跟踪时复制使用的状态模板
- `evals/`：跨 Agent 行为验收案例、运行方法和结果模板
- `scripts/validate_skill.py`：确定性的结构与一致性验证器
- `agents/openai.yaml`：可选的 OpenAI/Codex UI 元数据；其他 Agent 会忽略它

## 许可证

[MIT License](LICENSE)
