# Zongze PDD · Full-Stack Paid-Traffic Playbook (Agent Skill Pack)

> English | [中文](README.md)

An Agent Skill pack distilled from **525 long-form videos** (900k characters of transcribed speech) by the Douyin creator **@宗泽PDD实战** (Zongze, Pinduoduo operations coach).

- **1 router skill**: `zongze-pdd-quanxitu` — dispatches intents to 18 capability cards
- **10 promoted skills**: high-frequency capabilities callable on their own
- **18 capability cards**: each with R / I / A1 / A2 / E / B sections (evidence / interpretation / original case / transfer / execution contract / boundaries)

## What's inside

```
zongze-pdd-skill/
├── README.md                       # Chinese
├── README_EN.md                    # English (this file)
├── LICENSE
├── manifest.json
├── skills/
│   ├── zongze-pdd-quanxitu/        # router + 18 capability cards in references/
│   ├── qilian-sanjieduan/          # Three stages of launching a listing
│   ├── qilian-wuxiang-zhunbei/     # Five pre-launch preparations
│   ├── ceijia-celianjie/           # Price testing vs. listing testing
│   ├── chujia-xingshi-xuanze/      # Bid type: conversion bid vs. ROAS
│   ├── lengqidong-chujia-fudu/     # Cold-start bid step size
│   ├── xiane-shezhi-fangdakai/     # Budget caps and release cadence
│   ├── chesun-juece-baoben/        # Loss tolerance and break-even floor
│   ├── titouchan-jiezou/           # ROAS-raising cadence and observation
│   ├── cuofeng-lache/              # Off-peak switching and pull-push
│   └── zhitongche-shuju-zhibiao/   # Ad data observation priorities
└── docs/
    └── DIGEST.md                   # Long-form digest + parameter cheat sheet
```

## Install

### Claude Code / Claude Desktop (Skills)

```bash
# User level (available in every project)
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/

# Or project level
mkdir -p .claude/skills
cp -r skills/* .claude/skills/
```

### Codex / OpenAI Agents

Copy the folders under `skills/` into your skills directory (usually `~/.codex/skills/` or a project-level `skills/`), or feed `skills/zongze-pdd-quanxitu/SKILL.md` into the model as part of the system prompt.

### Cursor

```bash
mkdir -p .cursor/rules
cp skills/zongze-pdd-quanxitu/SKILL.md .cursor/rules/zongze-pdd.mdc
```

### WorkBuddy

```bash
# User level
cp -r skills/* ~/.workbuddy-ai/skills/
# Or project level
cp -r skills/* .workbuddy-ai/skills/
```

### Any model that accepts a system prompt

Inject the full text of `skills/zongze-pdd-quanxitu/SKILL.md` as the system prompt. The router table tells the model which file under `references/capabilities/` to load. For single-file setups, use one capability card directly (e.g. `references/capabilities/titouchan-jiezou.md`).

## Usage examples

- "My new Pinduoduo listing won't take off. What's step one?" → `qilian-sanjieduan`
- "Break-even ROAS is 2.8 — how much loss should I accept?" → `chesun-juece-baoben`
- "Is a 300/day budget cap right?" → `xiane-shezhi-fangdakai`
- "I raised ROAS by 5% and volume dropped. Should I roll back?" → `titouchan-jiezou`
- "High CTR but no orders — which metrics matter?" → `zhitongche-shuju-zhibiao`

## Parameter cheat sheet

| Stage | Value |
|---|---|
| Base impressions / paid threshold | 500/day, 400/day |
| Bid phase 1 / phase 2 | 5% × 4h × 3 per day / 8% × 1–1.5 days |
| Settling period | 3 days (observe 2–5 days) |
| Budget caps | below 70% of break-even: 100–150; at 85%: 250–300; near break-even: 400+ |
| Switch to ROAS | ≥85% of break-even, cap = 1.2× forecast spend, target 1.25× |
| ROAS raise | 5–10% per step; spend drop ≈ 3× the raise |
| Price-test refinement | cut gross margin by 3% (not price), 3-day interval |
| Off-peak switching | 1.05–1.2× net CPC; after two failures wait 28 days |

## Notes

- The methodology belongs to the original creator **@宗泽PDD实战**. This pack is a structured, engineering-oriented reorganization of publicly available video content.
- All numeric parameters are rule-of-thumb values from the videos. Calibrate them against your own category and ad account.
- For personal study and research only. Do not resell or use commercially.
- Nothing here is business or investment advice. Use at your own risk.
