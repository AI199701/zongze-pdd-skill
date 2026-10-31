# -*- coding: utf-8 -*-
"""Round 4 (dim8): add short rationale for key thresholds, based on judge feedback."""
from pathlib import Path

ROOT = Path(__file__).parent.parent
SKILLS = ROOT / "skills"

RATIONALE = {
"qilian-sanjieduan": [
 "500 曝光：系统给新链接的最小测试池，低于它无法判断赛道宽度。",
 "3 天沉淀：平台数据有 3 天滞后，短于 3 天会把波动当成趋势。",
 "保本 85%：留出提投产回本空间，又不至于深亏到无法修正。",
],
"qilian-wuxiang-zhunbei": [
 "上下 10% 毛利：覆盖相邻价格带，又不至于跨档导致数据失真。",
 "五项串行：后一步依赖前一步的数据，跳步会把测试结果误判。",
],
"ceijia-celianjie": [
 "3% 降毛利：约等于一个价格档位的最小可测差；降定价会放大毛利波动。",
 "3 天间隔：给系统重新匹配赛道的时间，短于 3 天测不出真实反应。",
],
"chujia-xingshi-xuanze": [
 "成交出价买精度：转化率优先，适合带功能性的非标品。",
 "投产比买 GMV：适合成型后收割，起链接期直接用会丢精度托底。",
],
"lengqidong-chujia-fudu": [
 "5% × 4h：小幅高频，避免被系统判定为异常操作。",
 "8% × 1.5 天：多次小幅无效后，用更大间隔换探索空间。",
],
"xiane-shezhi-fangdakai": [
 "100–150 / 250–300 / 400+：亏损越深限额越低，先控速再谈放量。",
 "由小变大：只有临近保本才敢多放，防止一次性花冒。",
],
"chesun-juece-baoben": [
 "85–90% 微亏：离保本近，掉量风险小，回本只需一轮提投产。",
 "75–80% 一般亏：仍保留回本空间，适合多数中腰部。",
 "50% 巨亏：接近一半利润，只适合资金极厚的冲量或清仓。",
],
"titouchan-jiezou": [
 "5–10%：幅度太大会被判定异常操作，太小则提不动。",
 "花费降幅 ≥ 幅度×3：超过等比例掉量，才说明赛道真的站住。",
 "3 天观测：平台数据有滞后，短于 3 天容易把波动当趋势。",
],
"cuofeng-lache": [
 "1.05–1.2 倍：覆盖净扣费波动区间，又不至于在错峰期亏太多。",
 "28 天：给系统重新学习出价与人群的时间。",
],
"zhitongche-shuju-zhibiao": [
 "前期转化 / 中期占比 / 后期点击率：对应比价机制的三个阶段。",
 "五项指标：覆盖量、质、成本、转化、出价竞争力，缺一项就会误判。",
],
"zongze-pdd-quanxitu": [
 "最多 2 张能力卡：避免上下文过载与多卡结论冲突。",
],
}


def main():
    changed = 0
    for slug, items in RATIONALE.items():
        p = SKILLS / slug / "SKILL.md"
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        if "## 参数依据" in text:
            continue
        block = "\n## 参数依据（为什么是这些数）\n\n" + "\n".join(f"- {x}" for x in items) + "\n"
        p.write_text(text.rstrip() + "\n" + block, encoding="utf-8")
        changed += 1
    print(f"round 4: {changed} skills updated")


if __name__ == "__main__":
    main()
