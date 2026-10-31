# 宗泽PDD实战 · 拼多多强付费运营全体系（Agent Skill 包）

> 中文 | [English](README_EN.md)

把抖音 @宗泽PDD实战 的 **525 条长视频口播**（90 万字转写）蒸馏成的一套可独立调用、可组合使用、可压力测试的 AI Skill 工具包。

- **1 个路由入口**：`zongze-pdd-quanxitu`（按意图分发到 18 张能力卡）
- **10 个晋级 Skill**：可单独调用的高频能力
- **18 张能力卡**：每张含 R/I/A1/A2/E/B 六段（依据 / 解读 / 原案例 / 迁移 / 执行契约 / 边界）

## 目录结构

```
zongze-pdd-skill/
├── README.md
├── LICENSE
├── manifest.json
├── skills/
│   ├── zongze-pdd-quanxitu/        # 路由入口（含 18 张能力卡 references）
│   ├── qilian-sanjieduan/          # 起链接三阶段
│   ├── qilian-wuxiang-zhunbei/     # 起链接前五项准备
│   ├── ceijia-celianjie/           # 测价与测链接
│   ├── chujia-xingshi-xuanze/      # 出价形式选择
│   ├── lengqidong-chujia-fudu/     # 冷启动出价幅度
│   ├── xiane-shezhi-fangdakai/     # 限额设置与放开
│   ├── chesun-juece-baoben/        # 车损决策与保本底线
│   ├── titouchan-jiezou/           # 提投产节奏
│   ├── cuofeng-lache/              # 错峰与拉扯
│   └── zhitongche-shuju-zhibiao/   # 直通车数据优先级
└── docs/
    └── DIGEST.md                   # 精华长文 + 精确参数速查表
```

## 安装到各 AI 工具

### Claude Code / Claude Desktop（Skills）

```bash
# 用户级（所有项目可用）
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/

# 或项目级
mkdir -p .claude/skills
cp -r skills/* .claude/skills/
```

### Codex / OpenAI Agents

把 `skills/` 下的目录放入你的 skills 目录（通常是 `~/.codex/skills/` 或项目内 `skills/`），
或直接把 `skills/zongze-pdd-quanxitu/SKILL.md` 作为系统提示的一部分喂给模型。

### Cursor

```bash
mkdir -p .cursor/rules
# 把路由入口转成 rule（或直接把 SKILL.md 内容粘进 .cursorrules）
cp skills/zongze-pdd-quanxitu/SKILL.md .cursor/rules/zongze-pdd.mdc
```

### WorkBuddy

```bash
# 用户级
cp -r skills/* ~/.workbuddy-ai/skills/
# 或项目级
cp -r skills/* .workbuddy-ai/skills/
```

### 通用（任何支持 system prompt 的模型）

把 `skills/zongze-pdd-quanxitu/SKILL.md` 全文作为系统提示注入，
模型会按其中的路由表去 `references/capabilities/*.md` 取对应能力卡。
单文件场景可直接把某张能力卡（如 `references/capabilities/titouchan-jiezou.md`）作为提示。

## 使用示例

- 「拼多多新链接起不来，第一步该做什么？」→ 路由到 `qilian-sanjieduan`
- 「保本 2.8，车损应该给到多少？」→ 路由到 `chesun-juece-baoben`
- 「限额设 300 合适吗？」→ 路由到 `xiane-shezhi-fangdakai`
- 「提投产提了 5% 掉量，要不要降回去？」→ 路由到 `titouchan-jiezou`
- 「点击率高但不出单，看什么数据？」→ 路由到 `zhitongche-shuju-zhibiao`

## 精确参数速查

| 环节 | 参数 |
|---|---|
| 基础曝光 / 付费阈值 | 500/天、400/天 |
| 出价第一段 / 第二段 | 5%×4h×日3次 / 8%×1–1.5天 |
| 沉淀期 | 3 天（观测 2–5 天） |
| 限额分档 | 保本70%↓：100–150；85%：250–300；保本附近：400+ |
| 转投产比 | ≥保本85%，限额=预估花费1.2倍，终点1.25倍 |
| 提投产 | 5–10%/次，花费降幅≈幅度×3 |
| 测价精筛 | 3%降毛利（非降定价），间隔3天 |
| 错峰 | 净扣费1.05–1.2倍，两次无效隔28天 |

## 说明

- 内容蒸馏自公开视频，**方法论归原作者 @宗泽PDD实战**，本包仅为结构化整理与工程化封装。
- 参数为口播经验值，需按类目与账户实测校准。
- 仅供个人学习研究，请勿商用或二次售卖。
