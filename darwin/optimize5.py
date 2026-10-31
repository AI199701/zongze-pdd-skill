# -*- coding: utf-8 -*-
"""Round 5 (dim1): add English trigger lines to frontmatter descriptions."""
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
SKILLS = ROOT / "skills"

EN = {
"zongze-pdd-quanxitu": "Use when a question involves Pinduoduo paid traffic: launching a listing, price testing, bid type, budget caps, loss tolerance, ROAS raising, off-peak switching, ad metrics, price competition, listing splits, or custom/wholesale bidding.",
"qilian-sanjieduan": "Use when launching a new Pinduoduo listing: the three stages (link recognition -> bid recognition -> paid activation) and their pass criteria (500 impressions, 400/day spend, 85% of break-even).",
"qilian-wuxiang-zhunbei": "Use before launching a listing: five serial preparations (product screening, competitor price bands, product testing, price testing, listing testing) and what each step must output.",
"ceijia-celianjie": "Use when testing price versus testing listing: price test holds everything but price equal, listing test varies everything but price; refine with 3% gross-margin cuts every 3 days.",
"chujia-xingshi-xuanze": "Use when choosing a bid type: conversion bid buys precision, ROAS bid buys GMV; pick the direction (low-to-high or high-to-low) and the switch point.",
"lengqidong-chujia-fudu": "Use for cold-start bid steps: 5% every 4 hours up to 3 times a day, then 8% every 1-1.5 days when 500 impressions are not reached.",
"xiane-shezhi-fangdakai": "Use for budget caps: 100-150 below 70% of break-even, 250-300 at 85%, 400+ near break-even; release caps from small to large.",
"chesun-juece-baoben": "Use when deciding loss tolerance: profit > break-even > slight loss (85-90%) > normal loss (75-80%) > heavy loss (50%); never touch product cost.",
"titouchan-jiezou": "Use when raising ROAS: 5-10% per step, observe 3 days (2-5), keep going if spend drop is at least 3x the raise, otherwise hold the floor.",
"cuofeng-lache": "Use for off-peak switching versus pull-push: switch the worst-spend hours to conversion bid at 1.05-1.2x net CPC; after two failures wait 28 days or use pull-push.",
"zhitongche-shuju-zhibiao": "Use for ad data priorities: spend rate, impressions, CTR, CVR, paid-impression share; early CVR/share, mid share, late CTR.",
}

changed = 0
for slug, line in EN.items():
    p = SKILLS / slug / "SKILL.md"
    if not p.exists():
        continue
    text = p.read_text(encoding="utf-8")
    if line in text:
        continue
    m = re.search(r"(description: \|\n(?:  .+\n)+)", text)
    if not m:
        continue
    block = m.group(1)
    new_block = block + "  " + line + "\n"
    text = text.replace(block, new_block, 1)
    p.write_text(text, encoding="utf-8")
    changed += 1

print(f"round 5: {changed} skills updated")
