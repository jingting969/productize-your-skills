# 更新日志

所有值得注意的变更都会记录在这里。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

## [0.1.3] - 2026-07-14

### 修正

- **Claude Code 章节修正**：从「Subagent / Slash Command」改为「Skills」，路径用 `~/.claude/skills/<name>/SKILL.md`
- 删除 `.claude/agents/` 和 `.claude/commands/` 旧说法（Claude Code 官方已合并到 Skills）
- 顶部声明加上「遵循 Agent Skills 开放标准」并链接 https://agentskills.io
- Cursor 改为 `.cursor/skills/`（保留 `.cursor/rules/` 作为精简场景备选）
- 新增「参考资料」章节，链接 Claude Code 官方 Skills 文档
- 设计原则新增「遵循开放标准」一条

## [0.1.2] - 2026-07-14

### 变更

- README 重写为「先回答能不能用，再回答怎么用」
- 新增工具支持矩阵表

## [0.1.1] - 2026-07-14

### 变更

- README 从「Codex 专属」改为「跨工具通用 Skill」

## [0.1.0] - 2026-07-14

### 新增

- 能力产品化模式：9 步产品化流程
- 案例学习模式：可持续迭代的产品案例库
- 证据等级 E0–E5 与五维评分
- 三级定价（试卖 / 标准 / 升级）
- 完整产品方案 / 试卖方案 / 最小可测试产品输出模板
- 7 项单元测试 + 5 组前向行为测试
- 案例库 CLI（add / validate）和自动索引

[0.1.0]: https://github.com/jingting969/productize-your-skills/releases/tag/v0.1.0
[0.1.1]: https://github.com/jingting969/productize-your-skills/releases/tag/v0.1.1
[0.1.2]: https://github.com/jingting969/productize-your-skills/releases/tag/v0.1.2
[0.1.3]: https://github.com/jingting969/productize-your-skills/releases/tag/v0.1.3
