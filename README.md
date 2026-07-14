# productize-your-skills

> 一个**通用** Agent Skill：从个人经历与能力证据生成可试卖产品、三级定价和首批销售验证方案。
> 适用于 Codex / Claude Code / Cursor / Trae / OpenCode 等支持自定义指令的 AI 工具。

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue)
![Platforms](https://img.shields.io/badge/platforms-Codex%20%7C%20Claude%20%7C%20Cursor%20%7C%20Trae%20%7C%20OpenCode-purple)

## 这是什么

一个跨 AI 工具的**通用 Agent Skill**。把它装进任何一个支持自定义指令的 AI 工具里，你就拥有了：

1. **能力产品化模式**：用证据驱动的教练式对话，把「我觉得自己会」转成「这是能卖的产品」
2. **案例学习模式**：把看到的成熟产品拆解、归档、积累为个人案例库

它的核心交付是 **9 步产品化工作流 + 6 维产品形态选择 + 证据等级评分 + 三级定价 + 首次销售验证**，而不是替你设计课程、建网站或写营销文案。

## 为什么是「通用」

大多数 AI 工具都支持某种形式的"自定义指令"（skill / agent / rule / command），但叫法和目录不一样。本 Skill 的做法：

- 把**核心工作流**写在 `SKILL.md` 里（一份自然语言提示词）
- 把**结构化方法论**拆到 `references/`（按需读取，不污染上下文）
- 把**案例库**做成 Markdown + Python CLI（任何工具都能读）

所以无论你用什么 AI 工具，**只要把 `SKILL.md` 喂给它**，它就具备能力产品化的能力。

## 安装（按工具选择）

### 🟢 Codex（CLI / App / Desktop）

复制整个目录到 Codex 的 Skill 根目录之一：

```bash
git clone https://github.com/jingting969/productize-your-skills.git
cp -R productize-your-skills ~/.codex/skills/
```

或者只复制单 Skill：

```bash
mkdir -p ~/.codex/skills
cp -R productize-your-skills ~/.codex/skills/
```

Skill 根目录支持：

- 全局：`~/.codex/skills/`
- 项目：`<project>/.codex/skills/`
- Desktop：`~/Library/Application Support/Codex/skills/`

重启 Codex，Skill 会以 **能力产品化** 名字出现。

### 🟣 Claude Code

Claude Code 不叫 Skill，叫 **Subagent**（`.claude/agents/`）或 **Slash Command**（`.claude/commands/`）。

#### 作为 Subagent（推荐）

```bash
mkdir -p ~/.claude/agents
cp -R productize-your-skills ~/.claude/agents/productize-your-skills
```

Claude Code 会自动读取 `SKILL.md` 的 frontmatter（`name` + `description`）作为 agent 的元信息。在对话里输入：

> 用 productize-your-skills 帮我做能力产品化

或者通过 `/agents` 命令查看它。

#### 作为 Slash Command（更轻量）

如果你只想要一个简单的指令入口：

```bash
mkdir -p ~/.claude/commands
cp productize-your-skills/SKILL.md ~/.claude/commands/productize.md
```

用法：在 Claude Code 输入 `/productize` 触发。

### 🔵 Cursor

Cursor 用 `.cursorrules` 或 `.cursor/rules/*.mdc`，**只支持简单规则文本**，不支持多文件引用。

```bash
# 项目级别（推荐）
mkdir -p .cursor/rules
cp productize-your-skills/SKILL.md .cursor/rules/productize.mdc
```

Cursor 不会主动调用，需要在对话中显式引用：

> @productize 我不知道自己能卖什么

#### 限制说明

Cursor 的规则是「每次回答都会自动读取」，所以请**精简使用**——只复制 `SKILL.md` 主入口，不要把 `references/` 也搬过去。

### 🟡 Trae

Trae 的 Skill 系统对自定义指令的支持**以官方文档为准**。通用做法：

```bash
# 在 Trae 项目里
mkdir -p .trae/skills
cp -R productize-your-skills .trae/skills/
```

如果 Trae 弹窗没有自动识别，请在 Trae 设置里手动指定 Skill 目录为 `.trae/skills/`。

### 🟠 OpenCode

```bash
# OpenCode 的 skill 目录通常在项目根或 ~/.opencode/
mkdir -p ~/.opencode/skills
cp -R productize-your-skills ~/.opencode/skills/
```

具体路径以你安装的 OpenCode 版本为准；详见 `opencode --help`。

### 🔧 其他任何 AI 工具

只要工具支持「自定义系统提示 / 项目说明 / 自定义指令」，都可以用：

```bash
# 把 SKILL.md 的内容作为「自定义指令」粘贴进工具设置
cat productize-your-skills/SKILL.md
```

`SKILL.md` 本身就是一份**自包含**的入口提示词，会告诉 AI 该读哪些参考文件、按什么流程工作。

## 使用

### 能力产品化模式

适用：

- “我不知道自己能卖什么”
- “我会很多事，但不知道怎么收费”
- “帮我设计咨询 / 陪跑 / 课程 / 订阅”

Skill 会按 9 步走：

1. 建立目标
2. 广泛盘点
3. 证据提取
4. 候选方向（最多 3 个）
5. 五维评分
6. 选择并产品化
7. 三级定价
8. 首次销售验证
9. 分级交付

### 案例学习模式

适用：

- “这是我设计好的产品，帮我拆解并加入案例库”

Skill 会：

1. 先确认来源和保存、引用许可
2. 按统一模板拆解为 16 个字段
3. 区分可迁移结构与不可照搬条件
4. 你确认后写入 `references/cases/` 并重建索引

### 案例库 CLI（可选）

`scripts/` 提供三个 Python 命令，与具体 AI 工具无关，可以独立运行：

```bash
# 录入新案例
python3 scripts/add_case.py /path/to/case.json

# 校验案例库
python3 scripts/validate_case.py
```

## 项目结构

```text
productize-your-skills/
├── SKILL.md                    # 主入口（所有 AI 工具都读这个）
├── agents/
│   └── openai.yaml             # Codex UI 元数据
├── references/                 # 方法论（按需读取）
│   ├── framework.md            # 9 步产品化框架
│   ├── evidence-and-scoring.md # 证据等级 E0–E5 + 五维评分
│   ├── product-patterns.md     # 6 种产品形态选择
│   ├── output-template.md      # 正式 / 试卖 / 探索实验输出模板
│   ├── case-template.md        # 案例 JSON 模板
│   ├── case-index.md           # 案例索引（自动生成）
│   └── cases/                  # 案例存放
├── scripts/                    # 案例库 CLI
├── tests/                      # 单元测试 + 前向测试
├── LICENSE
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
└── .gitignore
```

## 设计原则

- **证据优先** — 不把兴趣或自我评价直接当成产品
- **先验证后重投入** — 试卖前不开发课程、不建网站
- **用户自身证据 > 案例库** — 案例只用于类比，不直接照抄
- **不做结果承诺** — 所有市场、支付意愿、价格判断在未验证前都标记为假设
- **工具中立** — 核心是一份提示词 + 一组方法论，不绑定任何 AI 工具

## 开发与验证

```bash
# 单元测试
python3 -m unittest discover -s tests -v

# 案例库与索引
python3 scripts/validate_case.py

# Codex Skill 官方校验（需要 PyYAML，可选）
pip install PyYAML
python3 /path/to/skill-creator/scripts/quick_validate.py .
```

前向行为测试用例见 `tests/prompts.md`。

## 贡献

欢迎贡献：

- 新的产品案例（按 `references/case-template.md` 提供 JSON）
- 改进证据评分规则
- 增加前向测试用例
- 适配更多 AI 工具的安装教程
- Bug 修复

请阅读 `CONTRIBUTING.md` 后再提 PR。

## License

MIT © dashuai
