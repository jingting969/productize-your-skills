# productize-your-skills

> 从个人经历与能力证据生成可试卖产品、三级定价和首批销售验证方案。

## 这是什么

一个 Codex Agent Skill。给 Codex 装上之后，你就可以用对话方式把“自己会的东西”转成可售卖、可验证、可试卖的产品方案。

它**不**替你：
- 设计课程
- 搭建网站
- 写营销文案
- 承诺收入或成交

它**做**这两件事：
1. 用证据驱动的教练式对话，帮你从「我觉得自己会」走到「这是能卖的产品」
2. 提供一个可持续迭代的案例库，让你以后看到好的产品能直接拆解并归档

## 安装

把 `productize-your-skills/` 复制到 Codex 的 Skill 根目录之一：

- Codex 全局：`~/.codex/skills/`
- Codex 项目：`<project>/.codex/skills/`
- Codex desktop：`~/Library/Application Support/Codex/skills/`

完成后重启 Codex。Skill 会以 **能力产品化** 的名字出现在 Skill 列表中。

## 两种使用模式

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

## 案例库使用

### 录入

```bash
# 1. 准备一份 case.json（参考 references/case-template.md）
# 2. 写入案例并自动重建索引
python3 scripts/add_case.py /path/to/case.json
python3 scripts/validate_case.py
```

### 校验

```bash
python3 scripts/validate_case.py
```

### 用例约定

- 每次只读取最相关的少量案例
- 用户自身证据永远优先于案例
- 案例不能替代需求访谈和付费验证

## 开发与验证

```bash
# 单元测试
python3 -m unittest discover -s tests -v

# 案例库与索引
python3 scripts/validate_case.py

# Codex Skill 官方校验（需要 PyYAML）
python3 /path/to/skill-creator/scripts/quick_validate.py .
```

前向行为测试用例见 `tests/prompts.md`。

## 设计原则

- **证据优先** — 不把兴趣或自我评价直接当成产品
- **先验证后重投入** — 试卖前不开发课程、不建网站
- **用户自身证据 > 案例库** — 案例只用于类比，不直接照抄
- **不做结果承诺** — 所有市场、支付意愿、价格判断在未验证前都标记为假设

## 项目结构

```text
productize-your-skills/
├── SKILL.md                    # Skill 入口和路由
├── agents/
│   └── openai.yaml             # Codex UI 元数据
├── references/
│   ├── framework.md            # 9 步产品化框架
│   ├── evidence-and-scoring.md # 证据等级 E0–E5 + 五维评分
│   ├── product-patterns.md     # 6 种产品形态选择
│   ├── output-template.md      # 正式 / 试卖 / 探索实验输出模板
│   ├── case-template.md        # 案例 JSON 模板
│   ├── case-index.md           # 案例索引（自动生成）
│   └── cases/                  # 案例存放（自动生成）
├── scripts/
│   ├── case_library.py         # 案例库核心
│   ├── add_case.py             # 写入案例 + 重建索引
│   └── validate_case.py        # 案例库校验
├── tests/
│   ├── test_case_library.py
│   ├── prompts.md              # 前向行为测试
│   └── fixtures/               # 测试用 JSON
├── LICENSE
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
└── .gitignore
```

## 贡献

欢迎贡献：

- 新的产品案例（按 `references/case-template.md` 提供 JSON）
- 改进证据评分规则
- 增加前向测试用例
- 修复 Bug

请阅读 `CONTRIBUTING.md` 后再提 PR。

## License

MIT © dashuai
