# -*- coding: utf-8 -*-
"""Darwin optimization rounds for the Zongze skill pack.

Usage: python darwin/optimize.py <round>
  round 1 -> dim3 failure branches (if-then table)
  round 2 -> dim9 anti-pattern blacklist
  round 3 -> dim4 explicit checkpoints
"""
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SKILLS = ROOT / "skills"

IF_THEN = {
"qilian-sanjieduan": [
 ("三天沉淀后仍无 500 曝光", "查内功、定价、主图底稿原创度", "仍无 → 换链接，不加大车损"),
 ("出价降到很低仍不到 400/天", "确认是否属付费激活失败", "仍不到 → 放弃该链接"),
 ("转投产比后掉量", "回退到保本 85% 观察两天", "仍掉 → 守投产底线换链接"),
],
"qilian-wuxiang-zhunbei": [
 ("找品阶段全是难起品", "换类目或换品重筛", "仍无 → 放弃该批，不硬起"),
 ("竞品价格带不清晰", "扩样本到 10+ 竞品", "仍不清 → 先小规模测试再定档"),
 ("测款没有可主推的品", "提高投产再测一轮", "仍无 → 换品"),
],
"ceijia-celianjie": [
 ("精筛降 3% 毛利后花费无明显上升", "再降 3% 毛利", "两次无变化 → 当前定价即可"),
 ("裂变条数超额度", "收敛到 3×3", "仍超 → 分两批测"),
 ("测链接花费平均无法选择", "选曝光最大的链接集中花费", "无差异 → 按精泛比例与占比选"),
],
"chujia-xingshi-xuanze": [
 ("成交出价跑不动", "查低客单集中与 SKU 配置", "仍不动 → 提价或改投产比"),
 ("转投产比后精度流失", "回退成交出价延长托底", "仍流失 → 换素材重测"),
 ("款式型品用成交出价无效果", "改投产比低走高", "仍无 → 换主图底稿"),
],
"lengqidong-chujia-fudu": [
 ("5%×4h×3 次仍无 500 曝光", "切 8%×1.5 天间隔", "仍无 → 查内功或换链接"),
 ("曝光开始自我放大", "停止加价", "继续加 → 会浪费预算并打乱节奏"),
 ("弱考核期内未起量", "按既定节奏走", "不要为快强行加大车损"),
],
"xiane-shezhi-fangdakai": [
 ("实际花费超设置值", "小幅选区间内更低限额值", "幅度大 → 直接压限额"),
 ("限额下午就花完", "视为正常，不加限额", "连续 3 天 → 提投产"),
 ("投产接近保本仍花不完", "限额放到 400+", "仍花不完 → 查出价是否过低"),
],
"chesun-juece-baoben": [
 ("车损起链接断流", "查限额与节奏是否配合", "仍断 → 降一档车损"),
 ("临近保本提投产掉量", "守投产底线，延长观测", "仍掉 → 换链接"),
 ("巨亏两天无付费速率", "该舍则舍", "不要追加投入"),
],
"titouchan-jiezou": [
 ("提投产 5% 后掉量", "观测 3 天再看", "连续两轮掉 → 换链接"),
 ("花费降幅远大于提投产×3", "继续提投产", "降幅不足 → 守底线不加"),
 ("提投产不畅", "用错峰解决", "仍不畅 → 回退到上一档"),
],
"cuofeng-lache": [
 ("错峰连续两次无效", "隔 28 天再试", "仍无效 → 转拉扯"),
 ("当前是成交出价形式", "无法错峰，直接拉扯", "拉扯无效 → 回退出价形式"),
 ("每笔利润低于 4 元", "不能错峰", "只能拉扯或提投产"),
],
"zhitongche-shuju-zhibiao": [
 ("五项指标互相矛盾", "用平衡变量法找主核心指标", "仍矛盾 → 拉长观测周期"),
 ("转化率异常高", "查智能优惠券占花费比例", "仍高 → 查是否赛道极窄"),
 ("高点击低转化", "查专题位无用流量", "仍低 → 查内功与定价"),
],
"zongze-pdd-quanxitu": [
 ("路由表无命中", "查 references/capability-index.md", "仍无 → 明确告知超出范围"),
 ("一个问题命中多个能力", "最多加载 2 张能力卡", "仍冲突 → 拆成两个子问题"),
 ("缺少保本投产", "停止给限额与车损建议", "要求先核算保本"),
],
}

BLACKLIST = {
"qilian-sanjieduan": ["不要未过 500 曝光就加大车损", "不要把准备期数据当成起链接表现", "不要在三天沉淀期内频繁改价", "不要把 400/天 当成所有类目的固定值"],
"qilian-wuxiang-zhunbei": ["不要把五项准备当成起链接本身", "不要无竞品分析就直接定价", "不要照搬同行统一价策略", "不要用趋势品思路做标品"],
"ceijia-celianjie": ["不要降 3% 定价（要降 3% 毛利）", "不要在测价阶段改主图底稿", "不要测价未完成就测链接", "不要一次裂变超过额度"],
"chujia-xingshi-xuanze": ["不要用投产比直接替代标准推广", "不要长期用成交出价跑一般商品", "不要忽略 SKU 配置直接加价", "不要在低客单链接上硬用成交出价"],
"lengqidong-chujia-fudu": ["不要一天加价超过 3 次", "不要为快跳过三天沉淀", "不要在曝光放大时继续加价", "不要在弱考核期强行加大车损"],
"xiane-shezhi-fangdakai": ["不要把设置值当真实限额", "不要一次性大幅放开限额", "不要在亏损时放高限额", "不要因为花得快就加限额"],
"chesun-juece-baoben": ["不要碰货损", "不要为起链接强行加深车损", "不要在临近保本时才提投产", "不要在没有止损线时做巨亏起链接"],
"titouchan-jiezou": ["不要基于原值算提投产幅度", "不要一次不畅就不敢再提", "不要在观测期内频繁改动", "不要用单日数据判定站住"],
"cuofeng-lache": ["不要在成交出价形式下错峰", "不要每笔利润低于 4 元还错峰", "不要只试一档倍数就放弃", "不要把错峰当长期出价形式"],
"zhitongche-shuju-zhibiao": ["不要只看单一指标下结论", "不要用长周期尺看短周期数据", "不要在节流后 3 天内优化", "不要忽略智能优惠券对转化率的干扰"],
"zongze-pdd-quanxitu": ["不要硬套不适用的能力卡", "不要在缺数据时宣称已验证", "不要一次加载超过 2 张能力卡", "不要回答非拼多多平台的问题"],
}

CHECKPOINTS = {
"qilian-sanjieduan": ["🔴 转投产比前：确认已到保本 85%，否则 STOP", "🛑 连续两轮无 500 曝光：STOP，回退查内功，不得加大车损"],
"qilian-wuxiang-zhunbei": ["🔴 进入起链接前：五项均有结论，否则 STOP", "🛑 任一步缺数据：STOP，不得带病起链接"],
"ceijia-celianjie": ["🔴 精筛前：确认初筛已完成", "🛑 花费明显上升：STOP，不再降毛利"],
"chujia-xingshi-xuanze": ["🔴 切换出价形式前：确认当前阶段与精度需求", "🛑 精度连续下滑：STOP，回退成交出价"],
"lengqidong-chujia-fudu": ["🔴 第二段加价前：确认已沉淀 3 天", "🛑 曝光开始放大：STOP 加价"],
"xiane-shezhi-fangdakai": ["🔴 放限额前：确认当前投产位置", "🛑 实际花费超设置值 20%：STOP，压限额"],
"chesun-juece-baoben": ["🔴 定车损档位前：确认保本投产", "🛑 两天无付费速率：STOP，放弃该链接"],
"titouchan-jiezou": ["🔴 提投产前：确认当前值与保本投产", "🛑 连续两轮掉量：STOP，换链接"],
"cuofeng-lache": ["🔴 错峰前：确认主推广是投产比且每笔利润 ≥4 元", "🛑 连续两次错峰无效：STOP，转拉扯"],
"zhitongche-shuju-zhibiao": ["🔴 下结论前：确认五项指标齐全", "🛑 指标互相矛盾：STOP，先平衡变量"],
"zongze-pdd-quanxitu": ["🔴 给限额/车损建议前：确认保本投产", "🛑 意图超出范围：STOP，明确告知"],
}


def apply_round(n: int):
    changed = 0
    for slug, rows in IF_THEN.items():
        p = SKILLS / slug / "SKILL.md"
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")

        if n == 1:
            if "失败分支（if-then）" in text:
                continue
            table = ["\n### 失败分支（if-then）\n", "| 触发条件 | 一线修复 | 仍失败兜底 |", "|---|---|---|"]
            for a, b, c in rows:
                table.append(f"| {a} | {b} | {c} |")
            block = "\n".join(table) + "\n"
            if "## B — 边界" in text:
                text = text.replace("## B — 边界", block + "\n## B — 边界", 1)
            else:
                text = text.rstrip() + "\n" + block
        elif n == 2:
            if "## 反模式黑名单" in text:
                continue
            items = BLACKLIST.get(slug, [])
            block = "\n## 反模式黑名单\n\n" + "\n".join(f"- {x}" for x in items) + "\n"
            text = text.rstrip() + "\n" + block
        elif n == 3:
            if "## 执行检查点" in text:
                continue
            items = CHECKPOINTS.get(slug, [])
            block = "\n## 执行检查点\n\n" + "\n".join(f"- {x}" for x in items) + "\n"
            text = text.rstrip() + "\n" + block
        else:
            raise SystemExit("round must be 1, 2 or 3")

        p.write_text(text, encoding="utf-8")
        changed += 1
    print(f"round {n}: {changed} skills updated")


if __name__ == "__main__":
    apply_round(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
