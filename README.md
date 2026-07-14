# productize-your-skills

> **通用 Agent Skill**：从个人经历与能力证据生成可试卖产品、三级定价和首批销售验证方案。
> **遵循 [Agent Skills 开放标准](https://agentskills.io)**。Codex / Claude Code / Cursor / Trae / OpenCode 全部原生支持。

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue)
![Standard](https://img.shields.io/badge/standard-Agent%20Skills-purple)

## 它解决什么问题

你工作了很多年，会运营、写作、社群、项目管理、设计、咨询……你知道自己**会**很多东西，但回答不了"我能卖什么"。

这个 Skill 不替你设计课程、不替你建网站、不替你写营销文案。它做两件事：

1. **能力产品化模式**：用证据驱动的对话，把"我觉得自己会"变成"这是能卖的产品"
2. **案例学习模式**：把看到的成熟产品拆解、归档、积累成你的个人案例库

## 它能在哪些 AI 工具里用？

**所有支持自定义指令的 AI 工具都能用。** 下面是已经实测过的清单：

| AI 工具 | 支持 | 安装路径 |
| --- | :-: | --- |
| **Codex**（CLI / App / Desktop） | ✅ | `~/.codex/skills/` |
| **Claude Code** | ✅ | `~/.claude/skills/` 或 `.claude/skills/` |
| **Cursor** | ✅ | `.cursor/skills/` 或 `.cursor/rules/` |
| **Trae** | ✅ | `.trae/skills/` |
| **OpenCode** | ✅ | `~/.opencode/skills/` |
| **GitHub Copilot** | ✅ | 仓库 Copilot Instructions |
| **Windsurf** | ✅ | Global Rules |
| **ChatGPT**（Custom GPT / Projects） | ✅ | Custom Instructions |
| **其他任何工具** | ✅ | 粘贴 `SKILL.md` |

> **好消息**：Claude Code 官方明确说 Skills 遵循 **Agent Skills 开放标准**——这意味着 Claude Code、Codex、Cursor 等工具正在向同一套规范靠拢。本 Skill 正是按这个标准实现的。

---

## 安装（按工具分）

### Codex

```bash
git clone https://github.com/jingting969/productize-your-skills.git
cp -R productize-your-skills ~/.codex/skills/
```

重启 Codex，Skill 列表里会出现「能力产品化」。

> Skill 根目录支持三种：
> - 全局：`~/.codex/skills/`
> - 项目：`<project>/.codex/skills/`
> - Desktop：`~/Library/Application Support/Codex/skills/`

### Claude Code ✅ 推荐

Claude Code 官方把这种能力叫 **Skills**，**遵循 Agent Skills 开放标准**。

```bash
# 个人全局（跨项目可用）
mkdir -p ~/.claude/skills
cp -R productize-your-skills ~/.claude/skills/productize-your-skills

# 或项目级别（仅当前项目可用）
mkdir -p .claude/skills
cp -R productize-your-skills .claude/skills/productize-your-skills
```

Claude Code 会自动读取 `SKILL.md` 的 frontmatter（`name` + `description`）作为 Skill 元信息，并在需要时自动加载，或者你可以通过 `/productize-your-skills` 直接调用。

> **关于旧的 `.claude/commands/`**：Claude Code 已经把自定义命令合并到 Skills 体系，但旧文件**仍然兼容**。

### Cursor

```bash
# 项目级别（推荐：每个项目有自己的产品化规则）
mkdir -p .cursor/skills
cp -R productize-your-skills .cursor/skills/productize-your-skills

# 或全局（在家所有项目都用同一套）
mkdir -p ~/.cursor/skills
cp -R productize-your-skills ~/.cursor/skills/productize-your-skills
```

> Cursor 同时支持两种方式：
> - **Skills 模式（推荐）**：`SKILL.md` 入口，会按需读取 references/
> - **Rules 模式（仅限精简场景）**：`cp SKILL.md .cursor/rules/productize.mdc`，只复制主入口
>
> Cursor 规则是「每次回答都自动读取」，所以 Rules 模式下**只复制 `SKILL.md`**，不要把整个目录搬过去。

### Trae

```bash
# 项目级别
mkdir -p .trae/skills
cp -R productize-your-skills .trae/skills/

# 或全局
mkdir -p ~/.trae/skills
cp -R productize-your-skills ~/.trae/skills/
```

### OpenCode

```bash
mkdir -p ~/.opencode/skills
cp -R productize-your-skills ~/.opencode/skills/
```

### 其他工具的通用方法

**只要你的工具支持"自定义系统提示"或"项目规则"**，按下面三步来：

**第 1 步**：把 `SKILL.md` 内容复制下来：

```bash
cat productize-your-skills/SKILL.md
```

**第 2 步**：粘进工具的相应位置：

- **GitHub Copilot** → 仓库 Settings → Copilot → Instructions → 粘贴
- **Windsurf** → Settings → Rules → Global Rules → 粘贴
- **ChatGPT** → 创建 Custom GPT → Instructions → 粘贴；或 Project → Instructions → 粘贴
- **Cline / Continue / Roo Code** → `.clinerules` / `.continuerules` → 粘贴
- **Zed** → `.zed/rules` → 粘贴
- **JetBrains AI Assistant** → Settings → AI Assistant → 项目规则 → 粘贴

**第 3 步**：在对话里说：

> 按 SKILL.md 的工作流，帮我做能力产品化。

**只要 `SKILL.md` 被读到，这个 Skill 就生效。** `references/` 下的方法论是 AI 按需读取的补充材料，不是必需。

---

## 使用

### 能力产品化模式

适用：

- "我不知道自己能卖什么"
- "我会很多事，但不知道怎么收费"
- "帮我设计咨询 / 陪跑 / 课程 / 订阅"

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

- "这是我设计好的产品，帮我拆解并加入案例库"

Skill 会：

1. 先确认来源和保存、引用许可
2. 按统一模板拆解为 16 个字段
3. 区分可迁移结构与不可照搬条件
4. 你确认后写入 `references/cases/` 并重建索引

### 案例库 CLI（可选，跨工具通用）

```bash
# 录入新案例
python3 scripts/add_case.py /path/to/case.json

# 校验案例库
python3 scripts/validate_case.py
```

---

## 为什么是「通用」？

大多数 AI 工具都支持某种形式的"自定义指令"（Skill / Agent / Rule / Command），但叫法和目录不一样。这个 Skill 的做法：

- **`SKILL.md` = 一份自包含的入口提示词**，任何 AI 工具读到它，都能启动能力产品化工作流
- **`references/` = 按需加载的方法论**，避免污染上下文
- **`scripts/` = 案例库 CLI**，与 AI 工具无关，可独立运行

**Claude Code 官方明确说 Skills 遵循 Agent Skills 开放标准**——这意味着跨工具的标准正在收敛。本 Skill 直接对齐这个标准，让 Codex / Claude Code / Cursor 都能"开箱即用"。

---

## 项目结构

```text
productize-your-skills/
├── SKILL.md                    # ⭐ 主入口（所有 AI 工具都读这个）
├── agents/
│   └── openai.yaml             # Codex UI 元数据
├── references/                 # 按需读取的方法论
│   ├── framework.md            # 9 步产品化框架
│   ├── evidence-and-scoring.md # 证据等级 E0–E5 + 五维评分
│   ├── product-patterns.md     # 6 种产品形态选择
│   ├── output-template.md      # 完整 / 试卖 / 探索实验输出模板
│   ├── case-template.md        # 案例 JSON 模板
│   ├── case-index.md           # 案例索引（自动生成）
│   └── cases/                  # 案例存放
├── scripts/                    # 案例库 CLI（Python，跨工具）
├── tests/                      # 单元测试 + 前向测试
├── LICENSE                     # MIT
├── README.md                   # 你正在看的这个
├── CHANGELOG.md
├── CONTRIBUTING.md
└── .gitignore
```

---

## 设计原则

- **证据优先** — 不把兴趣或自我评价直接当成产品
- **先验证后重投入** — 试卖前不开发课程、不建网站
- **用户自身证据 > 案例库** — 案例只用于类比，不直接照抄
- **不做结果承诺** — 所有市场、支付意愿、价格判断在未验证前都标记为假设
- **工具中立** — 核心是一份提示词 + 一组方法论，不绑定任何 AI 工具
- **遵循开放标准** — 对齐 Agent Skills 开放标准，跨工具兼容

---

## 开发与验证

```bash
# 单元测试
python3 -m unittest discover -s tests -v

# 案例库与索引
python3 scripts/validate_case.py

# Codex Skill 官方校验（可选，需要 PyYAML）
pip install PyYAML
python3 /path/to/skill-creator/scripts/quick_validate.py .
```

前向行为测试用例见 `tests/prompts.md`。

---

## 贡献

欢迎贡献：

- 新的产品案例（按 `references/case-template.md` 提供 JSON）
- 改进证据评分规则
- 增加前向测试用例
- **适配更多 AI 工具的安装教程**（如果你在某个工具里实测成功，欢迎补充 README）
- Bug 修复

请阅读 `CONTRIBUTING.md` 后再提 PR。

---

## 参考资料

- [Agent Skills 开放标准](https://agentskills.io)
- [Claude Code Skills 文档](https://docs.claude.com/en/docs/claude-code/skills)
- [Codex Skills 文档](https://github.com/openai/codex)

---

## License

MIT © dashuai
