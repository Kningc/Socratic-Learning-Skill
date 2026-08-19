# Socratic Learning

一个面向 Codex 的通用苏格拉底学习 Skill。它可以围绕教材、论文、笔记、代码、题目、图像或音视频资料，通过自适应提问、分级提示、检索练习和迁移测试帮助学习者形成可验证的理解。

## 特点

- 以用户资料为主要课程，并标明资料内外的信息边界
- 每轮聚焦一个认知动作，依据回答动态调整难度
- 支持概念、数理与代码、论证文本、论文数据、语言记忆、多媒体和项目材料
- 卡住时逐级增强提示；需要时直接讲解，不把“苏格拉底式”变成障碍
- 通过解释、迁移、辨析和延迟回顾判断掌握情况

## 使用

将本仓库作为 Skill 安装后，可以这样调用：

```text
Use $socratic-learning to help me learn the attached chapter. I want to understand it well enough to apply it, and please teach in Chinese.
```

也可以直接提出自然语言请求，例如：“根据这篇论文，用苏格拉底学习法带我理解实验设计。”

## 文件

- `SKILL.md`：Skill 入口和核心教学协议
- `references/material-playbooks.md`：不同资料类型的适配策略
- `references/evidence.md`：设计依据与来源说明
- `agents/openai.yaml`：Codex UI 元数据

本 Skill 受 [OSTEP Socratic Tutor](https://github.com/lmonkt/ostep-socratic-tutor) 启发，并结合教育研究重新设计为材料无关、平台无关的学习流程。

## 许可证

[MIT License](LICENSE)
