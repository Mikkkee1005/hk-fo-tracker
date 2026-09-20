#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 HK 前台求职追踪站(单文件 HTML)"""
import json, io

# func: IBD / ECM / S&T / RES / BUY / QUANT
# org:  BB / EB / CN / BUY / QUANT / VC
# st:   open / soon / watch
R = []
def add(**k): R.append(k)

# ============ 外资投行 Summer 2027 ============
add(firm="Goldman Sachs", org="BB", role="2027 APEJ Summer Analyst — Global Investment Research",
    func="RES", typ="Summer", loc="香港", url="https://higher.gs.com/roles/170819", st="open",
    ddl="2026-10-04", ddl_txt="10/4(APAC 官方统一截止)", opened="2026-07-01",
    pay="未公开;Glassdoor HK IB SA 中位约 HK$64k/月(自报,低样本)", dur="9–11 周(官方)",
    lang="官方未写语言硬性要求", visa="未提及", gpa="posting 无 GPA 数字",
    proc="前台条线通常无笔试 → HireVue 录播(约30分钟,3–6题,每题约30秒准备/1.5–2分钟作答,常可重录1–3次)→ Superday 2–5 场面试(香港多为现场)",
    pat="APEJ 惯例 6月底–7月初集中放岗;2026年7月1日一批全部上线;2026届 Asia 截止在 10月5日",
    note="⚠️ GS 每个 cycle 最多投 4 个 business×location 组合,选岗即是取舍。<b>9/20 复核:官方 APAC 2027 Summer Analyst 项目页原文「Applications are now open and will close on Sunday, October 4, 2026」——10/4 统一截止口径未变,只剩两周。</b>⚠️ 本条 role 页(170819)本次抓取受限、无法逐字证实仍在挂,但第三方在招列表里仍能看到 GS 香港的 Global Investment Research Summer Analyst,倾向仍开。")
add(firm="Goldman Sachs", org="BB", role="2027 APEJ Summer Analyst — Investment Banking, Classic",
    func="IBD", typ="Summer", loc="香港", url="https://higher.gs.com/roles/170772", st="open",
    ddl="2026-10-04", ddl_txt="10/4(APAC 官方统一截止)", opened="2026-08(约)",
    pay="未公开;Glassdoor HK IB SA 中位约 HK$64k/月(自报,低样本)", dur="9–11 周(官方)",
    lang="官方未写语言硬性要求", visa="未提及", gpa="posting 无 GPA 数字",
    proc="HireVue 录播 → Superday 2–5 场面试(香港多为现场)",
    pat="2026 届的对应岗是 roles/150841;2027 届比 7月1日第一批晚了约七周才补挂",
    note="★★ 8/24 挂出:GS 香港投行部的「正统」IBD 入口,页面标题「2027 | APEJ | Hong Kong | Investment Banking, Classic | Summer Analyst」,当时 Apply 按钮实测有效。⚠️ 与 Capital Solutions Group(170773)是两份独立申请,各占 GS 那 4 个额度中的一个。统一 10/4 截止,<b>只剩两周</b>。<br>⚠️ <b>9/20 需要你亲自确认一次:</b>本次 170772 这个 role 页抓取受限读不到,而且<b>两个第三方在招列表里都没有出现 GS 香港的 IB Classic</b>(其余几个 GS 香港岗在列表里都能看到)。这既可能是第三方收录不全,也可能是它已经招满下架。本表没有证据判它关闭,状态维持已开,<b>但这是本周风险最高的一条,优先手动核一次</b>。")
add(firm="Goldman Sachs", org="BB", role="2027 APEJ Summer Analyst — FICC and Equities, Sales & Trading",
    func="S&T", typ="Summer", loc="香港", url="https://higher.gs.com/roles/169893", st="open",
    ddl="2026-10-04", ddl_txt="10/4(APAC 官方统一截止)", opened="2026-07-01",
    pay="同上", dur="9–11 周", lang="未写硬性要求", visa="未提及", gpa="无 GPA 数字",
    proc="同 GS 流程:HireVue → Superday", pat="同上",
    note="★ 9/20 直读官方 role 页复核:标题「2027 | APEJ | Hong Kong | FICC and Equities, Sales and Trading | Summer Analyst」,正文完整、<b>Apply 链接有效指向 Oracle 申请门户,确认仍开</b>。归属 Global Banking & Markets (Public)。10/4 截止,只剩两周。")
add(firm="Goldman Sachs", org="BB", role="2027 APEJ Summer Analyst — IBD, Capital Solutions Group",
    func="ECM", typ="Summer", loc="香港", url="https://higher.gs.com/roles/170773", st="open",
    ddl="2026-10-04", ddl_txt="10/4(APAC 官方统一截止)", opened="2026-07-01",
    pay="同上", dur="9–11 周", lang="未写硬性要求", visa="未提及", gpa="无 GPA 数字",
    proc="同 GS 流程", pat="同上",
    note="CSG = 融资/资本方案条线(ECM-DCM-LevFin 相邻)。★ 9/20 直读官方页复核:标题「2027 Summer Analyst, Investment Banking, Capital Solutions Group」,Hong Kong,<b>Apply 链接有效,确认仍开</b>。⚠️ 在 IB Classic(170772)本周无法证实的情况下,<b>这是 GS 投行侧目前唯一有硬证据还开着的香港入口</b>。10/4 截止。")
add(firm="Goldman Sachs", org="BB", role="2027 APEJ Summer Analyst — Asset Management, Alternatives / Private Investing",
    func="BUY", typ="Summer", loc="香港", url="https://higher.gs.com/roles/171427", st="open",
    ddl="2026-10-04", ddl_txt="10/4(APAC 官方统一截止)", opened="2026-07-01",
    pay="同上", dur="9–11 周", lang="未写硬性要求", visa="未提及", gpa="无 GPA 数字",
    proc="同 GS 流程", pat="同上",
    note="★ 全香港极少数对 penultimate 本科开放的「银行系真买方投资岗」(私募信贷/私募股权/实物资产)。另有 AM Client Solutions 岗但那是分销不是投资。9/20:role 页抓取受限无法逐字证实,但第三方在招列表仍列出 GS 香港这个岗,倾向仍开。10/4 截止。")
add(firm="Goldman Sachs", org="BB", role="APEJ Off-Cycle Internship — Global Investment Research(Industrial Tech)",
    func="RES", typ="Offcycle", loc="香港", url="https://higher.gs.com/roles/171082", st="watch",
    ddl="", ddl_txt="疑已下架", opened="",
    pay="未公开", dur="3–12 个月", lang="未写", visa="未提及", gpa="无 GPA 数字",
    proc="同 GS 流程", pat="GS APEJ off-cycle 按台子零散上新,全年可见",
    note="⚠️ 9/20 降为待观察:该 role 页现在返回空 body。本次做了对照实验——已知过期的 roles/150841(2026 HK IB Classic)同样返回空 body,而在挂的 169893/170773 返回完整正文+Apply 链接,所以「空页」= 已下架而非 JS 渲染问题。另外搜索索引里它的标题其实是「<b>2026</b> | APEJ | Hong Kong | GIR, Industrial Tech | Off-cycle」——本来就是 2026 批不是 2027 批。GS 的 off-cycle 通常还需要学校批准 leave of absence。")

add(firm="Morgan Stanley", org="BB", role="2027 IBD — Industrial Placement / Summer Analyst",
    func="IBD", typ="双轨", loc="香港/新加坡/首尔", url="https://morganstanley.tal.net/vx/candidate/so/pm/1/pl/1/opp/21290", st="open",
    ddl="2026-09-27", ddl_txt="R1 已过 · R2 9/27(终轮)", opened="2026-07-07",
    pay="未官方公开;Glassdoor 折年约 HK$56–65万(21份自报)≈ HK$4.7–5.4万/月",
    dur="Summer 10–12 周;Industrial Placement 六个月(2027年1月中–7月中)",
    lang="官方:必须英文流利,亚洲语言优先", visa="posting 未提及", gpa="posting 无 GPA 数字",
    proc="线上测试(候选人称 OT,供应商未确认)→ HireVue 录播 → 香港 Superday",
    pat="2027 批香港九个项目 2026年7月7日同批上线,统一 9月27日截止;耶鲁 OCS 7月8日发公告",
    note="★★ 同一个 requisition 里含「六个月 Industrial Placement(2027年1–7月,全职,base 香港)」——目前市面上规格最高的免费六个月 HK off-cycle。毕业窗口 2027年10月–2028年7月。<b>9/20 复核:R2 = 2026年9月27日 23:55 HKT / SGT / 22:55 KST,未变——只剩 7 天,而且这是终轮。</b>官方同时写明滚动审(「We recruit on an ongoing basis」),别掐点交。")
add(firm="Morgan Stanley", org="BB", role="2027 Institutional Equity Division — IP / Summer Analyst",
    func="S&T", typ="双轨", loc="香港/新加坡", url="https://morganstanley.tal.net/vx/candidate/so/pm/1/pl/1/opp/21266", st="open",
    ddl="2026-09-27", ddl_txt="9/27(滚动)", opened="2026-07-07",
    pay="同上", dur="Summer 10–12 周 / IP 六个月", lang="英文必须,亚洲语言优先", visa="未提及", gpa="无 GPA 数字",
    proc="同上", pat="同上",
    note="MS 香港本轮没有单独品牌化的 Equity Research 暑期岗——香港的研究曝光走 IED 和 FID 这两个入口。<b>9/20 直读官方页复核:原文「Application deadline #2: Sunday, September 27, 2026 at 23:55 HKT / SGT」,未变。</b>")
add(firm="Morgan Stanley", org="BB", role="2027 Fixed Income Division — IP / Summer Analyst",
    func="S&T", typ="双轨", loc="香港/新加坡", url="https://morganstanley.tal.net/vx/candidate/so/pm/1/pl/1/opp/21318", st="open",
    ddl="2026-09-27", ddl_txt="9/27(滚动)", opened="2026-07-07",
    pay="同上", dur="Summer 10–12 周 / IP 六个月", lang="英文必须", visa="未提及", gpa="无 GPA 数字",
    proc="同上", pat="同上",
    note="含信用与宏观研究曝光。学历要求:本科/硕士,2027年10月–2028年7月毕业,不限专业。⚠️ <b>9/20:MS 五个香港岗里唯一没能复核到的一个</b>——opp 21318 的页面本次读不到,也找不到任何 posting 级镜像。「9/27 仍有效」是从 MS 官方全线口径(耶鲁、USC 等多所学校转载的 MS 官方通知都写 9月27日关)推定的,<b>不是这一页的实证</b>。只剩 7 天,自己点开确认一次。")
add(firm="Morgan Stanley", org="BB", role="2027 Global Capital Markets — IP / Summer Analyst",
    func="ECM", typ="双轨", loc="香港", url="https://morganstanley.tal.net/vx/candidate/so/pm/1/pl/1/opp/21294", st="open",
    ddl="2026-09-27", ddl_txt="9/27(滚动)", opened="2026-07-07",
    pay="同上", dur="Summer 10–12 周 / IP 六个月", lang="英文必须", visa="未提及", gpa="无 GPA 数字",
    proc="同上", pat="同上",
    note="★ GCM = ECM/DCM/杠杆融资。这是与 IBD 完全独立的一份申请——投了 IBD 不会进这个池子,而且历年相对不饱和。")
add(firm="Morgan Stanley", org="BB", role="2027 IED Quantitative Finance — Summer Analyst / Associate",
    func="QUANT", typ="Summer", loc="香港", url="https://morganstanley.tal.net/vx/mobile-0/brand-0/candidate/so/pm/1/pl/1/opp/21270-2027-Institutional-Equity-Division-Quantitative-Finance-Summer-Analyst-Associate-Program-Hong-Kong/en-GB", st="open",
    ddl="2026-09-27", ddl_txt="R1 已过 · R2 9/27(终轮)", opened="2026-07-07",
    pay="同 MS 其余香港岗", dur="Summer 10–12 周",
    lang="英文必须", visa="未提及",
    gpa="posting 无 GPA 数字,但要求数理/CS/工程背景与编程能力",
    proc="同 MS 流程:线上测试 → HireVue 录播 → 香港 Superday",
    pat="与 IBD/IED/FID/GCM 同批 7月7日上线,共用 R1 8/16 + R2 9/27 双轮",
    note="★ 第五个 MS 香港岗。官方原文「penultimate year of a Bachelor's, Master's, or PhD... expected graduation between September 2027 and June 2028」——本科 penultimate 明确可投。⚠️ 与普通 IED 岗(21266)是两份独立申请,做量化方向的别只投 IED。<b>9/20 直读官方页复核:原文「Application deadline #2: Sunday, September 27, 2026 at 23:55 HKT」,未变。只剩 7 天。</b>")

add(firm="J.P. Morgan", org="BB", role="2027 CIB — Global Investment Banking Summer Analyst",
    func="IBD", typ="Summer", loc="香港", url="https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210749752", st="open",
    ddl="2026-09-29", ddl_txt="9/29(滚动审;原记 9/30,按早的算)", opened="2026-06-01",
    pay="Glassdoor 自报 HK$53,000/月", dur="9 周(官方:含5天 orientation 与培训)",
    lang="官方:英文流利", visa="未提及", gpa="无 GPA 数字、无强制成绩单",
    proc="HireVue 录播(暑期岗常见 3–5 题)→ Superday",
    pat="2027 批香港全部岗位 2026年6月1日上线,统一 9月30日截止——比其他 BB 早整整一个月",
    note="⚠️ 开得最早=池子最深。滚动审意味着 9月投的和 6月投的不是同一个竞争面。<b>★ 9/20 更正:两处独立的第三方汇总(foundit、Extern)都把 JPM 的 Investment Banking 一条列为 <b>9月29日</b>截止,而 Markets / AM / 两个私行岗才是 9/30。</b>JPM 的 Oracle 岗位页正文要 JS 渲染、抓不到原文,无法直接证实到底哪天,所以本表按早的 9/29 对待。<b>别掐 9/30 那天交这一份。</b>")
add(firm="J.P. Morgan", org="BB", role="2027 CIB — Markets Summer Analyst",
    func="S&T", typ="Summer", loc="香港", url="https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210747060", st="open",
    ddl="2026-09-30", ddl_txt="9/30(滚动审)", opened="2026-06-01",
    pay="同上", dur="9 周", lang="英文流利", visa="未提及", gpa="无 GPA 数字", proc="同上", pat="同上", note="")
add(firm="J.P. Morgan", org="BB", role="2027 CIB — Markets Summer Analyst · Research",
    func="RES", typ="Summer", loc="香港", url="https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210747391", st="open",
    ddl="2026-09-30", ddl_txt="9/30(滚动审)", opened="2026-06-01",
    pay="同上", dur="9 周", lang="英文流利", visa="未提及", gpa="无 GPA 数字", proc="同上", pat="同上",
    note="★ 独立 requisition,但挂在「Markets」目录下而不是「Research」——用 research 关键词搜是搜不到的,这是最常被漏掉的研究岗之一。")
add(firm="J.P. Morgan", org="BB", role="2027 Asset Management Program — Summer Internship",
    func="BUY", typ="Summer", loc="香港", url="https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210743031", st="open",
    ddl="2026-09-30", ddl_txt="9/30(滚动审)", opened="2026-06-01",
    pay="同上", dur="—", lang="英文流利", visa="未提及", gpa="无 GPA 数字", proc="同上", pat="同上",
    note="覆盖 JPMAM 香港的投资侧条线。另有 Global Private Bank Investment Solutions 岗,但那是方案/顾问不是组合管理。")

add(firm="Bank of America", org="BB", role="Global Investment Banking Summer Analyst 2027",
    func="IBD", typ="Summer", loc="香港", url="https://careers.bankofamerica.com/en-us/students/job-detail/14367/global-investment-banking-summer-analyst-2027-hong-kong-hong-kong-hong-kong", st="open",
    ddl="2026-09-30", ddl_txt="9/30", opened="2026-06-30",
    pay="未公开", dur="10 周(官方)", lang="官方:英文流利必须,额外亚洲语言「highly advantageous」",
    visa="未提及", gpa="仅写 outstanding academic achievement,无数字",
    proc="官方口径为「电话/视频/现场面试组合」;录播视频环节存在但平台未公开确认(网传的 Suited 未被证实用于 BofA)",
    pat="2027 批香港七个岗位 2026年6月30日同日上线", note="转正指向 2028 全职。")
add(firm="Bank of America", org="BB", role="Global Capital Markets Summer Analyst 2027",
    func="ECM", typ="Summer", loc="香港", url="https://careers.bankofamerica.com/en-us/students/job-detail/14375/global-capital-markets-summer-analyst-2027-hong-kong-hong-kong-hong-kong", st="open",
    ddl="2026-09-30", ddl_txt="9/30", opened="2026-06-30",
    pay="未公开", dur="10 周", lang="同上", visa="未提及", gpa="无数字", proc="同上", pat="同上",
    note="★ 与 GIB(job 14367)是两份独立申请,覆盖 ECM/DCM/杠杆融资承做——纯 IBD 关键词搜索的经典盲区。")
add(firm="Bank of America", org="BB", role="Global Markets Sales & Trading Rotational Summer Analyst 2027",
    func="S&T", typ="Summer", loc="香港", url="https://careers.bankofamerica.com/en-us/students/job-detail/14366/global-markets-sales-trading-rotational-summer-analyst-2027-hong-kong-hong-kong-hong-kong", st="open",
    ddl="2026-09-30", ddl_txt="9/30", opened="2026-06-30",
    pay="未公开", dur="10 周", lang="同上", visa="未提及", gpa="无数字", proc="同上", pat="同上", note="轮岗制,跨台子。")
add(firm="Bank of America", org="BB", role="Global Corporate Banking Summer Analyst 2027",
    func="IBD", typ="Summer", loc="香港", url="https://careers.bankofamerica.com/en-us/students/job-detail/14384/global-corporate-banking-summer-analyst-2027-hong-kong-hong-kong-hong-kong", st="open",
    ddl="2026-09-30", ddl_txt="9/30", opened="2026-07(约)",
    pay="未公开", dur="10 周",
    lang="官方:英文流利必须,另一门亚洲语言「highly advantageous」", visa="未提及",
    gpa="posting 写 outstanding academic achievement,无数字",
    proc="同 BofA 其余香港岗", pat="与 IBD(14367)、GCM(14375)、Global Markets(14366)同批",
    note="★ 8/24 新收录:BofA 香港的第四个前台岗,此前漏收。官方原文 penultimate year、2028 届可转正。属客户覆盖/公司银行条线(不是 M&A 执行),但客户面工作、与 IBD 协作紧密,收进主表。与另外三个 BofA 岗各自独立申请。")

add(firm="Citi", org="BB", role="Markets – Sales and Trading, Summer Analyst, Hong Kong – 2027",
    func="S&T", typ="Summer", loc="香港", url="https://jobs.citi.com/job/hong-kong/markets-sales-and-trading-summer-analyst-hong-kong-2027/287/97603330976", st="open",
    ddl="2026-10-30", ddl_txt="10/30 23:59 HKT(滚动审)", opened="2026-07-10",
    pay="Glassdoor 自报 HK$5.0–5.4万/月", dur="10 周", lang="HK IBD posting 未特别写", visa="未提及", gpa="无 GPA 数字",
    proc="Plum(即坊间说的 Citi Assessment / Plum Discovery Survey)→ 录播视频面 → 终面",
    pat="Citi 的规律是 Markets 先开、Banking 晚 1–3 个月:2027 Markets 7月10日开,Banking 8月上旬如期跟上",
    note="★ 9/20 更新:这个岗原本<b>不写截止日</b>(本表记 until filled),现在官方页已明确写出「Applications closes 30 October, 23:59 HKT」——<b>Citi 香港 Banking / Markets / Private Bank 四个岗的截止日至此统一为 10/30</b>(唯一例外是新发现的 Citigold 岗,11/30)。⚠️ 官方口径:APAC 每人最多申 3 个 summer 项目,组合投法要提前想好。")
add(firm="Citi", org="BB", role="Banking – Investment Banking, Summer Analyst, Hong Kong – APAC, 2027",
    func="IBD", typ="Summer", loc="香港", url="https://jobs.citi.com/job/hong-kong/banking-investment-banking-summer-analyst-hong-kong-apac-2027/287/98836110080", st="open",
    ddl="2026-10-30", ddl_txt="10/30(滚动审)", opened="2026-08(约)",
    pay="参照 Markets 岗:Glassdoor 自报 HK$5.0–5.4万/月", dur="10 周(2027年6月起)", lang="英文", visa="未提及", gpa="无 GPA 数字",
    proc="Plum 测评 → 录播视频面 → 终面",
    pat="按历年规律 Banking 晚于 Markets 1–3 个月,本轮 8 月上旬挂出、10/30 截止",
    note="★ 8/10 核验:如期开闸,滚动审。同批还有 Corporate Banking Summer Analyst(req 98836109936),对企业银行覆盖条线有兴趣的可作第三选项。⚠️ APAC 每人最多申 3 个 summer 项目。")
add(firm="Citi", org="BB", role="Banking – Capital Markets, Summer Analyst, Hong Kong – APAC, 2027",
    func="ECM", typ="Summer", loc="香港", url="https://jobs.citi.com/job/hong-kong/banking-capital-markets-summer-analyst-hong-kong-apac-2027/287/98836109888", st="open",
    ddl="2026-10-30", ddl_txt="10/30(同批,滚动审)", opened="2026-08(约)",
    pay="同上", dur="10 周", lang="英文", visa="未提及", gpa="无 GPA 数字",
    proc="同上", pat="与 Banking-IBD 同批 8 月上旬挂出",
    note="★ ECM/DCM 承做条线,与 IBD 是独立申请——只搜 investment banking 会漏。计入「最多 3 个项目」额度。")

add(firm="UBS", org="BB", role="2027 Summer Internship — Global Banking(IBD)",
    func="IBD", typ="Summer", loc="香港", url="https://jobs.ubs.com/TGnewUI/Search/home/HomeWithPreLoad?partnerid=25008&siteid=5131&PageType=JobDetails&jobid=348161", st="open",
    ddl="2026-08-06", ddl_txt="8/6 硬截止", opened="2026-07-04",
    pay="未官方公开", dur="10 周(官方:paid)",
    lang="★官方硬性:需掌握 普通话/印地语/泰语/越南语/印尼语 之一", visa="香港岗未写", gpa="无 GPA 数字",
    proc="UBS 线上测评套件 → 官方明示的录播视频面 → 终面",
    pat="2027 批 7月4日上线、8月6日截止——UBS 走的是硬截止而非 until-filled,窗口只有约五周,是所有 BB 里最短的",
    note="8/10 核查:8/6 硬截止已过,未见任何延期公告,按已截止对待(官方措辞本有「may remain open until filled」,真想投的可以从 jobs.ubs.com 搜索页亲测一下,但别抱期望)。")
add(firm="UBS", org="BB", role="2027 Summer Internship — Global Markets",
    func="S&T", typ="Summer", loc="香港", url="https://jobs.ubs.com/TGnewUI/Search/home/HomeWithPreLoad?partnerid=25008&codes=IUNICAREERS&siteid=5131&PageType=JobDetails&jobid=347860", st="open",
    ddl="2026-08-06", ddl_txt="8/6 硬截止", opened="2026-07-04",
    pay="未公开", dur="10 周", lang="同上", visa="未写", gpa="无 GPA 数字", proc="同上", pat="同上",
    note="⚠️⚠️ 同为 8/6 硬截止。")
add(firm="UBS", org="BB", role="2027 Summer Internship — Asset Management",
    func="BUY", typ="Summer", loc="香港", url="https://jobs.ubs.com/TGnewUI/Search/home/HomeWithPreLoad?partnerid=25008&siteid=5131&PageType=JobDetails&jobid=348591", st="open",
    ddl="2026-08-06", ddl_txt="大概率同批 8/6(未官方确认)", opened="2026-07-18(约)",
    pay="未公开", dur="10 周", lang="同 UBS 香港批(普通话等亚洲语言之一)", visa="未写", gpa="无 GPA 数字",
    proc="同 UBS 流程:线上测评 → 录播视频面 → 终面",
    pat="与 GB/GM 同为 2027 香港批,7 月中旬后补挂",
    note="★ 8/3 新发现:此前漏收的 UBS 香港买方侧暑期岗(jobid 348591)。与同批 GB/GM 均为 8/6 硬截止,此岗大概率同期——按 8/6 对待,立即投。UBS 深链常误显示 expired,从 jobs.ubs.com 搜索页进入。")
add(firm="UBS", org="BB", role="2027 Off-Cycle Internship — Global Wealth Management, Solutions",
    func="BUY", typ="Offcycle", loc="香港", url="https://hk.linkedin.com/jobs/view/2027-off-cycle-internship-global-wealth-management-solutions-hk-at-ubs-4436463723", st="watch",
    ddl="", ddl_txt="⚠️ 8/24 官方职位库查无此岗", opened="",
    pay="未公开", dur="通常 6 个月(项目范围 3–12 个月)",
    lang="APAC off-cycle 资格:倒数第二年在读、<2年工作经验、实习结束后 6–12 个月内毕业", visa="未写", gpa="无 GPA 数字",
    proc="同 UBS 流程", pat="2027 off-cycle 与 summer 同批(7月)上线,按台子分别发布、全年补挂",
    note="⚠️ 8/24 降级为待观察:UBS 官方 jobs.ubs.com 上搜不到这个香港岗,只有第三方聚合站(LinkedIn / ExpatJobBoard)还留着页面。同批多个 UBS off-cycle 的 jobid 实测都已返回「posting has expired」——UBS 这一轮 off-cycle 整体在收口。链接先留着自己点一次确认,别当作确定在挂。")
add(firm="UBS", org="BB", role="2027 Off-Cycle Internship — Global Research(新加坡)",
    func="RES", typ="Offcycle", loc="新加坡", url="https://jobs.ubs.com/TGnewUI/Search/home/HomeWithPreLoad?partnerid=25008&siteid=5131&PageType=JobDetails&jobid=348322", st="watch",
    ddl="", ddl_txt="⚠️ 8/24 实测已过期", opened="",
    pay="未公开", dur="3–12 个月", lang="—", visa="—", gpa="无 GPA 数字", proc="同上", pat="同上",
    note="⚠️ 8/24 实测:该 jobid 页面已显示「The job posting you are looking for has expired or the position has already been filled」,香港的 Global Research off-cycle(jobid 348319)同样已过期。UBS 本轮 APAC 研究 off-cycle 到此为止;UBS 香港的暑期三岗也已于 8/6 硬截止——UBS 这条线目前基本无可投项。")

add(firm="Barclays", org="BB", role="Investment Banking Summer Internship Programme 2027",
    func="IBD", typ="Summer", loc="香港", url="https://search.jobs.barclays/job/hong-kong/investment-banking-summer-internship-programme-2027-hong-kong/13015/97173677136", st="open",
    ddl="", ddl_txt="Until filled(滚动)", opened="2026-06-30",
    pay="未公开", dur="10 周",
    lang="★官方硬性:投香港岗必须「中文书写 + 普通话口语」流利", visa="需在申请时申报是否需要 Barclays 担保签证",
    gpa="「Ideally… GPA of 3.2 or above」——ideally 措辞,非硬卡",
    proc="线上测评(供应商未公开)→ 录播视频面 → 终面",
    pat="2027 批香港四个项目 + 一个量化 off-cycle 于 2026年6月30日同日上线",
    note="毕业窗口 2027年12月–2028年6月。新加坡同岗:search.jobs.barclays/job/singapore/…/97173677392")
add(firm="Barclays", org="BB", role="Sales, Trading and Structuring Summer Internship Programme 2027",
    func="S&T", typ="Summer", loc="香港", url="https://search.jobs.barclays/job/hong-kong/sales-trading-and-structuring-summer-internship-programme-2027-hong-kong/13015/97173677952", st="open",
    ddl="", ddl_txt="Until filled(滚动)", opened="2026-06-30",
    pay="未公开", dur="10 周", lang="同上", visa="同上", gpa="ideally 3.2+", proc="同上", pat="同上",
    note="含结构化(Structuring)曝光,量化相邻。")
add(firm="Barclays", org="BB", role="Electronic Trading Associate Summer Internship Programme 2027",
    func="S&T", typ="Summer", loc="香港", url="https://search.jobs.barclays/job/hong-kong/electronic-trading-associate-summer-internship-programme-2027-hong-kong/13015/97173677472", st="open",
    ddl="", ddl_txt="Until filled(滚动)", opened="2026-06-30",
    pay="未公开", dur="10 周", lang="同上", visa="同上", gpa="ideally 3.2+", proc="同上", pat="同上",
    note="⚠️★ 8/24 重要更正:此前把 Associate 读成「只是项目名称」是错的——posting 原文明确限 postgraduate、毕业窗口 2027年12月–2028年6月,**2028 届本科 penultimate 不符合资格**,除非你走硕士路径。本科生想去 quant trading 又要留银行侧选项,应该投主 S&T 项目(Sales, Trading and Structuring)。")
add(firm="Barclays", org="BB", role="Quantitative Analytics Associate Off-Cycle Internship 2027",
    func="QUANT", typ="Offcycle", loc="香港", url="https://search.jobs.barclays/job/hong-kong/quantitative-analytics-associate-off-cycle-internship-2027-hong-kong/13015/97173677168", st="open",
    ddl="", ddl_txt="Until filled(滚动)", opened="2026-06-30",
    pay="未公开", dur="off-cycle", lang="同上", visa="同上", gpa="—", proc="同上", pat="同上",
    note="★ 目前极少数由 BB 公开发布的香港 off-cycle 量化岗,只搜 summer 完全看不到。⚠️ 8/24 更正:同样限 postgraduate,2027年6–12 月六个月制,**本科 penultimate 不符合**。硕士在读或计划读硕的留着这一枪。")

add(firm="HSBC", org="BB", role="Investment Banking Internship 2027",
    func="IBD", typ="Summer", loc="香港(中环)", url="https://apply.careers.hsbc.com/emergingtalent/job/Central-Investment-Banking-Internship-Hong/1365768357/", st="open",
    ddl="2026-10-30", ddl_txt="10/30(滚动审)", opened="2026-07-06",
    pay="Glassdoor 自报 IB SA 约 HK$71,000/月(注意:HSBC 通用项目实习的自报值只有 1.4–2万,前台与通用项目差距极大)",
    dur="10 周,2027年6月14日起", lang="官方:英文流利",
    visa="★官方明示「We will consider candidates that require visa sponsorship」,并列明接受香港学生签——是所有 BB 里签证态度最友好的",
    gpa="2026 批官方写 GPA ≥3.2/4.0(或 4.0/5.0);2027 posting 页面未见数字,建议按 3.2 预期",
    proc="HSBC Online Immersive Assessment(工作模拟式测评,视频作答环节内嵌其中)→ 终面",
    pat="2027 批香港 CIB 全套 2026年7月6日上线,统一 10月30日截止;历年也是 10月下旬关",
    note="⚠️ <b>9/20 重要:同批四个岗里已经有两个提前关闭</b>(Global Investment Research、Infrastructure Finance,页面均已改成「this position has been filled」)。本岗 9/20 实测仍开、closing date 仍是 10 月底(招聘系统显示 Oct 31,HSBC 官方项目文案写 10月30日,按 10/30 行动更安全)。<b>但 10/30 这个日期现在已经被证明不可靠——HSBC 是全表最会提前关门的,尽快投。</b>")
add(firm="HSBC", org="BB", role="Global Investment Research Internship 2027",
    func="RES", typ="Summer", loc="香港(中环)", url="https://apply.careers.hsbc.com/emergingtalent/job/Central-Global-Investment-Research-Internship-Hong/1365767957/", st="watch",
    ddl="", ddl_txt="★已提前关闭(招满)", opened="2026-07-06",
    pay="同上", dur="10 周", lang="英文流利", visa="同上", gpa="参照 3.2", proc="同上", pat="同上",
    note="❌ <b>9/20:已提前关闭。</b>官方岗位页现在显示「Sorry, this position has been filled.」——<b>比公示的 10/30 截止日整整早了 40 天</b>。这正是 HSBC posting 里那句「we recruit on a rolling basis and may close applications before the advertised date once all vacancies are filled」的实际后果。教训:HSBC 看着窗口最长,其实是全表最会提前关门的。★ 这原本是全港 2027 批仅有的三个真股票研究实习之一(另两个:GS GIR、JPM Markets-Research),现在只剩两个。")
add(firm="HSBC", org="BB", role="Markets – Sales & Trading Internship 2027",
    func="S&T", typ="Summer", loc="香港(中环)", url="https://apply.careers.hsbc.com/emergingtalent/job/Central-Markets-Sales-and-Trading-Internship-Hong/1365768857/", st="open",
    ddl="2026-10-30", ddl_txt="10/30(滚动审)", opened="2026-07-06",
    pay="同上", dur="10 周", lang="英文流利", visa="同上", gpa="参照 3.2(9/20 页面实测明写 GPA 3.2/4.0)", proc="同上", pat="同上",
    note="⚠️ 9/20 实测仍开,closing date 显示 Sat Oct 31 2026,毕业窗口 2027年11月–2028年7月。<b>但同批已有两个岗提前招满关闭,这个和 IB 综合岗是仅剩的两个,别拖到 10 月底。</b>")
add(firm="HSBC", org="BB", role="Investment Banking – Infrastructure Finance Internship 2027",
    func="ECM", typ="Summer", loc="香港(中环)", url="https://apply.careers.hsbc.com/emergingtalent/job/Central-Investment-Banking-HSBC-Infrastructure-Finance-Internship-Hong/1365767657/", st="watch",
    ddl="", ddl_txt="★已提前关闭(招满)", opened="2026-07-06",
    pay="同上", dur="10 周", lang="英文流利", visa="同上", gpa="参照 3.2", proc="同上", pat="同上",
    note="❌ <b>9/20:已提前关闭。</b>官方页同样显示「Sorry, this position has been filled.」,比公示的 10/30 早 40 天。HSBC 香港 CIB 四个前台岗本周关掉两个(本岗 + Global Investment Research),<b>只剩 Investment Banking 综合岗与 Markets S&amp;T 两个还开着——这两个也随时可能同样处理,别等 10 月底。</b>")

add(firm="Jefferies", org="BB", role="2027 Investment Banking Summer Analyst — Hong Kong",
    func="IBD", typ="Summer", loc="香港", url="https://jefferies.tal.net/vx/lang-en-GB/mobile-0/appcentre-1/brand-4/xf-c74479acfe42/candidate/so/pm/1/pl/2/opp/1814-2027-Summer-Analyst-Program-Investment-Banking-Hong-Kong/en-GB", st="open",
    ddl="", ddl_txt="在挂,官方页不写截止日", opened="2026-08(约)",
    pay="未公开", dur="posting 未写", lang="亚洲语言 a plus(无中文硬性要求)", visa="未写",
    gpa="★硬线:官方页 9/20 实测为 <b>GPA ≥ 3.6</b>(此前记 3.4,已更正)——全表最高",
    proc="候选人提到有 OA 但未指明供应商;首轮常为视频或现场约30分钟",
    pat="历年 6月底–7月放岗(2026=opp 1503,2025=opp 1240,2024=opp 940);2027 批香港晚了约一个月",
    note="★★ <b>9/20 终于复核成功,并且换上了官方直投链接。</b>上两周 tal.net 全站机器人验证读不到,这次没有拦截:Jefferies 官方 Campus 板亚洲三条齐备——<b>香港 opp 1814</b>、新加坡 1815、日本 1816,卡片链接已换成香港这条的官方申请页(不再走 LinkedIn)。<b>判定仍开的硬证据(对照组):</b>同板的芝加哥 2027 岗(opp 1729)页面明写「This opportunity is closed to applications」,香港这条没有该提示。官方页仍不写截止日。资格:penultimate,毕业窗口 2027年10月–2028年6月,10 周,<b>GPA ≥3.6</b>——注意这比本表此前记的 3.4 还高,已按官方页更正,是全表最高的硬线。")

add(firm="J.P. Morgan", org="BB", role="2026 CIB — Markets Off-Cycle Analyst Program",
    func="S&T", typ="Offcycle", loc="香港", url="https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210717757", st="open",
    ddl="", ddl_txt="未写", opened="",
    pay="未公开", dur="APAC off-cycle 惯例 3–6 个月全职", lang="—", visa="—", gpa="无 GPA 数字",
    proc="同 JPM 流程", pat="—", note="覆盖 Sales / Trading / Structuring & Origination / DCM。")

add(firm="Société Générale", org="BB", role="TRAINEE: Investment Banking(ref 26000C7D)",
    func="IBD", typ="Offcycle", loc="香港", url="https://careers.societegenerale.com/en/job-offers/trainee-investment-banking-26000C7D-en", st="open",
    ddl="", ddl_txt="未写", opened="",
    pay="未公开", dur="香港 trainee 合同惯例 6–12 个月", lang="未公开", visa="未公开", gpa="—",
    proc="未公开", pat="—", note="同期在港开放的还有 Fixed Income Structuring trainee(26000BKU)等。")

add(firm="Deutsche Bank", org="BB", role="2027 Summer Internship Programme — Investment Banking & Capital Markets",
    func="IBD", typ="Summer", loc="香港", url="https://db.recsolu.com/external/requisitions/cplr7_vfWqWirluwSqtQew", st="open",
    ddl="2026-09-30", ddl_txt="9/30 23:45 HKT(滚动审)", opened="2026-08(约)",
    pay="未公开", dur="未写", lang="未写", visa="★明确接受「香港学生签」", gpa="无 GPA 数字",
    proc="DB 站内测评套件 → 官方明示的录播视频面 → 终面",
    pat="2027 批 8 月中挂出、9/30 截止,与历史「秋季开、10月底关」的节奏相比略提前收窗",
    note="★ <b>9/20 直读官方 req 页复核:原文「30 September 2026, 11.45pm HKT」,Apply 按钮有效,截止日未变——只剩 10 天。</b>资格:2027年12月1日–2028年7月31日之间完成学业,相关全职经验 ≤12 个月,明确接受香港学生签。做 M&A 建模、行业分析、live deal。<br>另:DB 香港 2027 批本周新出现的是 <b>Fixed Income &amp; Currencies Graduate Programme</b>(全职毕业生岗,面向 2027 届,不是实习),<b>没有</b>新挂的香港 2027 暑期 Global Markets 实习。")
add(firm="Nomura", org="BB", role="2027 Investment Banking Summer Internship — Hong Kong",
    func="IBD", typ="Summer", loc="香港", url="https://nomuracampus.tal.net/candidate/jobboard/vacancy/1/adv/", st="open",
    ddl="2026-09-30", ddl_txt="9/30", opened="2026-08(约)",
    pay="未公开", dur="未公开", lang="未公开", visa="未公开", gpa="美国岗写 strong GPA,无数字;香港未写",
    proc="Nomura Global Campus(tal.net)投递;官方口径为「仅部分候选人被邀请视频面」",
    pat="按预期 8 月上线;与 Global Markets、IWM 同批,均 9/30 截止",
    note="★ 9/20 官方板直读复核(本次无人机验证):<b>opp 1492,原文「Please apply before 11:55pm, Wednesday 30 Sep 2026 (HKT)」,截止日未变</b>。单岗深链仍未被索引,从职位板入口进入后选 Hong Kong 岗申请。同板另有 Global Markets Graduate Internship HK(opp 1488)、Finance Graduate HK(opp 1526,10/31)等非前台/非本批岗,别投错。")
add(firm="Nomura", org="BB", role="2027 Global Markets Summer Internship — Hong Kong",
    func="S&T", typ="Summer", loc="香港", url="https://nomuracampus.tal.net/candidate/jobboard/vacancy/1/adv/", st="open",
    ddl="2026-09-30", ddl_txt="9/30", opened="2026-08(约)",
    pay="未公开", dur="未公开", lang="未公开", visa="未公开", gpa="香港未写",
    proc="同上", pat="与 IB、IWM 同批上线",
    note="★ 9/20 官方板直读复核:<b>opp 1485,原文「Please apply before 11:55pm, Wednesday 30 September 2026 (HKT)」,未变</b>。从板内进入申请。")
add(firm="Nomura", org="BB", role="2027 International Wealth Management Summer Internship — Hong Kong",
    func="PB", typ="Summer", loc="香港", url="https://nomuracampus.tal.net/candidate/jobboard/vacancy/1/adv/", st="open",
    ddl="2026-09-30", ddl_txt="9/30 23:55 HKT", opened="2026-08(约)",
    pay="未公开", dur="未公开", lang="未公开", visa="未公开", gpa="香港未写",
    proc="同上;官方原文另写「interviews can be arranged prior to the application deadline」——会在截止前就开始面",
    pat="与 IB、GM 同批上线,三岗同为 9/30",
    note="★★ <b>9/20 待观察解除,恢复「已开放」。</b>上次是因为 Nomura 官方板全站人机验证、五种 URL 形态都读不到内容才降级的;这次官方职位板没有拦截,<b>直接读到了原文:opp 1474,「Please apply before 11:55pm, Wednesday 30 September 2026 (HKT)」</b>——2027 版确实存在且在收。公开挂牌的香港私行暑期岗仍是 JPM(两个)、Citi、DB、Nomura 这几家。⚠️ 只剩 10 天,且官方明说会在截止前就安排面试。")
add(firm="Standard Chartered", org="BB", role="Global Banking Intern Hong Kong 2027(job 59126)",
    func="IBD", typ="Summer", loc="香港", url="https://jobs.standardchartered.com/job/Global-Banking-Intern-Hong-Kong-2027/59126-en_GB/", st="open",
    ddl="2026-12-31", ddl_txt="12/31 挂牌结束(10 月起面,会提前招满)", opened="2026-08-17",
    pay="未公开", dur="10 周(2027年6月起)",
    lang="未写硬性要求",
    visa="⚠️★ 官方硬性:「must possess the permanent legal right to work in Hong Kong」——学生签不符合,非本地生慎投",
    gpa="★官方:不设 GPA,「we welcome students from all degree disciplines」,strengths-based",
    proc="★pymetrics 游戏化测评(官方确认)→ 单向录播视频面 → 评估中心(官方:2026年10月起开始)",
    pat="2027 批 8月17日上线,posting end 12/31;转正后全职 2027年7月起",
    note="★★ 2027 批 8/17 上线,9/20 复核仍在挂(req 59126,closing date 31/12/2026)。业务覆盖资本市场、地产融资、基建融资。⚠️ 两个硬约束:① 必须有香港永久工作权(不是学生签),这是全表少见的国籍/身份硬门槛;② 官方限「六个月内只能投一份申请」——渣打三个香港岗只能三选一。页面没有写申请截止日,只有 posting end 12/31,但评估中心 10 月就开始,按滚动对待。")
add(firm="Standard Chartered", org="BB", role="Coverage Banking Intern Hong Kong 2027(job 59110)",
    func="IBD", typ="Summer", loc="香港", url="https://jobs.standardchartered.com/job/Central-Coverage-Banking-Intern-Hong-Kong-2027/1369586957/", st="open",
    ddl="2026-12-31", ddl_txt="12/31 挂牌结束(10 月起面)", opened="2026-08-17",
    pay="未公开", dur="10 周(2027年6月起)", lang="未写硬性要求",
    visa="⚠️★ 同上:须有香港永久工作权",
    gpa="不设 GPA,strengths-based",
    proc="同上:pymetrics → 录播面 → 评估中心", pat="与 Global Banking 同批 8/17 上线",
    note="★ 分到 Corporate Coverage、Financial Institutions Coverage、M&A 三个组之一——★ 想做 M&A 的走这个入口,不是 Global Banking。⚠️ 与 Global Banking / 新开的 Markets Intern 共用「六个月内只能投一份」的限制,三选一。<br>⚠️ <b>9/20 复核不到:</b>搜索引擎未索引到 59110 的页面,也找不到镜像,只查到 2026 批的旧页(当时叫 Client Coverage Internship Programme)。同批的 Global Banking(59126)仍在挂,所以它大概率也还在,<b>但本表拿不到证据,不做断言</b>——渣打官方站内搜索用新名「Coverage Banking Intern」自己确认一次。")
add(firm="Standard Chartered", org="BB", role="★ Markets Intern Hong Kong 2027(即原 Financial Markets,已改名)",
    func="S&T", typ="Summer", loc="香港", url="https://jobs.standardchartered.com/", st="open",
    ddl="2026-10-02", ddl_txt="10/2(镜像口径)· 官方同批写 12/31,按早的算", opened="2026-09-01",
    pay="未公开", dur="10 周(2027年6月起)", lang="未写", visa="⚠️★ 官方硬性:须有香港永久工作权(同渣打其余香港岗)",
    gpa="不设 GPA,strengths-based;官方原文「You must be a penultimate-year student, available to intern from June」",
    proc="pymetrics 游戏化测评 → 单向录播视频面 → 评估中心(10 月开始)",
    pat="2026 批叫 Financial Markets Internship Programme;2027 批改名 Markets Intern,且比 CIB 三岗(8/17)晚两周、9/1 才上线",
    note="★★ <b>9/20 本周最重要的新开放:渣打的 Financial Markets 香港 2027 已经挂出来了,只是改了名字。</b>上两周查不到不是因为没开,是因为<b>渣打 2027 批把岗位名全改了</b>——「Financial Markets Internship Programme」→「<b>Markets Intern</b>」,「Client Coverage」→「Coverage Banking」。用旧名搜永远搜不到。业务线原文写明是「Financial Markets within Corporate &amp; Investment Banking」,分 Sales / Trading / Structuring / Financing Risk / Research / Risk-Modelling-Analytics-Product-XVA 六个方向。<br>⚠️ <b>截止日有冲突,本表按早的算:</b>校招镜像页写 closing date <b>10月2日</b>(只剩不到两周),而渣打官方同项目新加坡版(Markets Intern SG 2027, req 61050)官方页写的是 12/31。10/2 很可能是校方端的 posting expiry 而非渣打自己的截止日,但<b>没法证实,所以当 10/2 是硬截止来准备</b>。⚠️ 另外注意渣打「六个月内只能投一份申请」——这个岗和 Global Banking / Coverage Banking 三选一,现在多了一个选项但额度没变。本表不给伪造深链:到 jobs.standardchartered.com 搜「Markets Intern Hong Kong 2027」。")
add(firm="BNP Paribas", org="BB", role="2027 APAC Long Internship(1–6月,六个月制)— Global Banking APAC",
    func="IBD", typ="Offcycle", loc="香港", url="https://group.bnpparibas/en/careers/job-offer/2027-apac-long-internship-jan-jun-global-banking-apac-hong-kong", st="open",
    ddl="", ddl_txt="页面未写截止,滚动收(尽快投)", opened="2026-08-17",
    pay="未公开", dur="★六个月(2027年1月–6月),全职", lang="官方:英文口笔流利必须,其他语言加分",
    visa="官方:欢迎各国籍申请,但视来源国可能有签证限制",
    gpa="Long Internship 页面未写 GPA(Graduate 线才写 3.3/4.0 硬线)",
    proc="未公开测评供应商;官方口径为「多数情况下先电话或视频面」",
    pat="2027 批香港站 8月17日批量上线,共 9 个岗(4 个 Long Internship + 5 个 Graduate)",
    note="★★ 8/24 核验:BNP 兑现了「8 月开申」——职位页 last update 就是 8/17,你 8/17 当天没看到是因为当天稍晚才上。含 M&A / ECM / DCM / Coverage 等 stream。⚠️★ 官方原文:「Candidates with more than one application will not be processed」——BNP 全集团只让投一份,跨条线跨地点都算,投多份直接不处理。投前先在 Global Banking / Global Markets / Wealth Management 之间选定。")
add(firm="BNP Paribas", org="BB", role="2027 APAC Long Internship(1–6月,六个月制)— Global Markets",
    func="S&T", typ="Offcycle", loc="香港", url="https://group.bnpparibas/en/careers/job-offer/2027-apac-long-internship-jan-jun-global-markets-hong-kong", st="open",
    ddl="", ddl_txt="页面未写截止,滚动收", opened="2026-08-17",
    pay="未公开", dur="六个月(2027年1月–6月),全职", lang="英文流利必须", visa="同上",
    gpa="页面未写", proc="同上", pat="与 Global Banking 同批 8/17 上线",
    note="★ 8/24 新收录。⚠️ 与其余 BNP 岗共用「只能投一份」的限制。")
add(firm="BNP Paribas", org="BB", role="2027 APAC Long Internship(1–6月,六个月制)— Wealth Management",
    func="PB", typ="Offcycle", loc="香港", url="https://group.bnpparibas/en/careers/job-offer/2027-apac-long-internship-jan-jun-wealth-management-hong-kong", st="open",
    ddl="", ddl_txt="页面未写截止,滚动收", opened="2026-08-17",
    pay="未公开", dur="六个月(2027年1月–6月),全职", lang="英文流利必须", visa="同上",
    gpa="页面未写", proc="同上", pat="与 Global Banking 同批 8/17 上线",
    note="★ 8/24 新收录:私行条线的六个月 off-cycle,全港同规格的很少。⚠️ 与其余 BNP 岗共用「只能投一份」的限制。")
add(firm="Wells Fargo", org="BB", role="★ 2027 APAC Banking Summer Analyst — Hong Kong(R-571608)",
    func="IBD", typ="Summer", loc="香港", url="https://www.wellsfargojobs.com/en/jobs/r-571608/2027-apac-banking-summer-analyst-hong-kong/", st="open",
    ddl="2026-10-30", ddl_txt="10/30(Posting End Date;可能提前关)", opened="2026-09(约)",
    pay="未公开", dur="约 10 周", lang="未公开", visa="未公开",
    gpa="官方:penultimate year,毕业窗口 2028年1–6月——2028 届正对口",
    proc="未公开", pat="上一批(2026)12月19日才挂出、1月29日截止;<b>2027 批提前了整整三个月</b>",
    note="★★ <b>9/20 本周最大的意外:Wells Fargo 提前了三个月开闸。</b>本表一直把它记作「全表最晚的 BB,12 月中才开」,当作错过秋季主窗口后的最后一枪——结果 2027 批现在就已经挂出,而且<b>截止日 10月30日,只剩五周半</b>。页面另注「Job posting may come down early due to volume of applicants」。⚠️ Banking 与 Markets 是<b>两份独立申请</b>(Markets 见下一条)。新加坡对应岗是 R-571603 / R-571606,同样 10/30。<b>如果你原本把 Wells Fargo 排在 12 月的计划里,现在要把它挪到 10 月。</b>")
add(firm="Wells Fargo", org="BB", role="★ 2027 APAC Markets Summer Analyst — Hong Kong(R-571605)",
    func="S&T", typ="Summer", loc="香港", url="https://www.wellsfargojobs.com/en/jobs/r-571605/2027-apac-markets-summer-analyst-hong-kong/", st="open",
    ddl="2026-10-30", ddl_txt="10/30(Posting End Date;可能提前关)", opened="2026-09(约)",
    pay="未公开", dur="约 10 周", lang="未公开", visa="未公开",
    gpa="官方:penultimate year,毕业窗口 2028年1–6月",
    proc="未公开", pat="与 Banking 岗同批提前挂出",
    note="★★ 9/20 新开放。与上面的 Banking 岗是<b>两个独立项目、两份申请</b>,别以为投了一个就覆盖了。同样 10/30 截止、同样注明可能因申请量提前关闭。")
add(firm="Macquarie", org="BB", role="Macquarie Capital Summer / Off-Cycle(香港,不定期)",
    func="IBD", typ="Offcycle", loc="香港", url="https://recruitment.macquarie.com/en_US/careers/SearchJobs/", st="watch",
    ddl="", ddl_txt="不定", opened="",
    pay="未公开", dur="未公开", lang="未公开", visa="未公开", gpa="—", proc="未公开",
    pat="香港系列历年复现(2025 req 13755、2024 req 7452、2026 京港 off-cycle req 20541)但均不公开开放日期",
    note="另有 Off-cycle Algo Quant Strategy(job 22742,6个月,9月起)在挂,但面向硕博。")
add(firm="Mizuho 瑞穗", org="BB", role="2027 Summer Internship Program — 香港前台分岗(待开)",
    func="ECM", typ="Summer", loc="香港", url="https://mizuhogroup.wd102.myworkdayjobs.com/External", st="soon",
    ddl="", ddl_txt="预计 2026 年底–2027 年初开", opened="",
    pay="未公开", dur="未公开", lang="未公开", visa="未公开", gpa="未设",
    proc="未公开", pat="2026 批在 Workday 挂过香港前台三岗:ECM/Corporate Finance(JR100384)、Debt Syndication(JR100369)、Equities(JR100370)",
    note="★ 8/10 新增收录:日资行里在港有成建制前台暑期项目的一家,按台子分岗(ECM/债券承销/股票)。9/20 复核仍未挂 2027 批:索引里能查到的香港岗<b>全部是 2026 批</b>(ECM/Corporate Finance JR100384、JR100388,Debt Syndication JR100369,Equities JR100370,Structured Finance JR100381)。Workday 板确认是 JS 渲染、静态抓取读不到任何职位,所以「未发现」是索引层面的结论——用浏览器打开筛 Hong Kong + Internship 自己看一眼更稳。")
add(firm="Crédit Agricole CIB 东方汇理", org="BB", role="★ 香港前台岗(注意:一律叫「Trainee」,不叫 internship)",
    func="S&T", typ="双轨", loc="香港", url="https://jobs.ca-cib.com/offre-de-emploi/liste-toutes-offres.aspx?lcid=2057&facet_Country=1693", st="watch",
    ddl="", ddl_txt="现有岗批次错配;2027 暑期批待开", opened="",
    pay="未公开", dur="Trainee 多为一年期合约;另有 10 周正规暑期项目(2026 批存档可见)",
    lang="未写", visa="未写",
    gpa="⚠️ 现挂的 Trainee 岗多要求 2027 年前毕业——2028 届不匹配",
    proc="未公开", pat="法资行在港的惯例:前台学生岗一律叫 Trainee + one year contract,用 internship/summer analyst 关键词永远搜不到",
    note="★ <b>9/20 新增收录,本周「藏在非直觉目录」的最大发现。</b>CACIB 香港现有 14 个在招岗,前台的有六个:Global Markets Off-cycle Intern(Jan–Apr 2027)、Global Markets Trainee–DCM、Global Markets Trainee–FX &amp; Rates Macro FI Sales、Global Markets Research Trainee、Coverage Trainee–FIG、Trainee–Energy &amp; Infrastructure。<br>⚠️ <b>但批次对 2028 届错配,所以本表先记为待观察而不是可投:</b>逐个核过两个——Off-cycle Intern (Jan–Apr 2027) 截止 10月31日,但资格写的是「2027 年夏季毕业、能于 2027 年 8 月入职 Graduate Program」;FIG Coverage Trainee 要求 2026 年 9 月前毕业。这些一年期 Trainee 基本是 graduate-level。<b>真正该等的是它的 10 周正规暑期项目</b>(2026 批存档页可查),2027 版尚未挂出。<b>收录它的意义在于:每次核查都要翻一遍它的香港岗位总目录,别用 internship 关键词搜。</b>")
add(firm="SMBC 三井住友", org="BB", role="Summer Intern Programme 2027(新加坡,⚠️ 不在香港)",
    func="IBD", typ="Summer", loc="新加坡", url="https://careerasia.smbc.co.jp/SMBC/job/SMBC-Summer-Intern-Programme-2027/1426851233/", st="open",
    ddl="2026-09-30", ddl_txt="9/30(滚动审)", opened="2026-08(约)",
    pay="未公开", dur="10 周(2027年5月起)", lang="英文", visa="未写",
    gpa="★官方:四年制本科第三年、<b>2028 年毕业</b>——和你这届逐字吻合",
    proc="未公开", pat="覆盖 Corporate & Investment Banking 与 Global Markets 两条线",
    note="★ <b>9/20 新增收录,破例收一个新加坡岗,两个理由:</b>① SMBC 是本表完全没有的大行,而它的资格写的是「4 年制本科第 3 年、2028 年毕业」——比大多数岗位的表述都更精准地命中你这届;② <b>9月30日截止,只剩 10 天</b>。地点在新加坡 CapitaSpring,不是香港。<br>⚠️ 另外查了 SMBC 香港分行的独立招聘站:15 个在招岗全是 VP/AVP/Associate 级别,<b>香港确实没有对应的学生项目</b>——所以这条要去新加坡才能用。接受去 SG 的,本周就投。")

# ============ 精品行 / 独立顾问 ============
add(firm="Houlihan Lokey", org="EB", role="Off-Cycle Internship — Corporate Finance(R3228)",
    func="IBD", typ="Offcycle", loc="香港", url="https://hl.wd1.myworkdayjobs.com/en-US/Campus/job/Hong-Kong-China/Off-Cycle-Internship---Corporate-Finance_R3228", st="open",
    ddl="", ddl_txt="滚动", opened="",
    pay="未公开", dur="香港 CF off-cycle 历年为 6 个月", lang="香港 CF 岗通常要求中英", visa="未公开", gpa="未设",
    proc="部分地区有 OA,香港未确认", pat="香港岗不在 hl.com 的 early-careers 页(该页只有美国/欧洲),只能从 Workday Campus board 找",
    note="")
add(firm="Houlihan Lokey", org="EB", role="Off-Cycle Intern — Financial and Valuation Advisory(R3096)",
    func="IBD", typ="Offcycle", loc="香港", url="https://hl.wd1.myworkdayjobs.com/en-US/Campus/job/Off-Cycle-Intern--Financial-and-Valuation-Advisory--Hong-Kong-_R3096", st="open",
    ddl="", ddl_txt="滚动", opened="",
    pay="未公开", dur="即时起", lang="英文必须", visa="需持香港工作权利(学生签可)", gpa="未设",
    proc="—", pat="香港 FR/FVA off-cycle 每半年循环一次",
    note="偏好有 Big4 或投行实习经历者。9/20 复核:R3096 仍在挂(此前记的 R3228 Corporate Finance 已不在在挂列表里)。HL 用 Workday,正文 JS 渲染,读不到截止日。")
add(firm="Houlihan Lokey", org="EB", role="★ Summer Financial Analyst 2027 — Financial Restructuring, Hong Kong(R3488)",
    func="IBD", typ="Summer", loc="香港", url="https://hl.wd1.myworkdayjobs.com/Campus/job/Hong-Kong-China/Summer-Financial-Analyst-2027---Financial-Restructuring--Hong-Kong_R3488", st="open",
    ddl="", ddl_txt="在挂,Workday 页读不到截止日", opened="2026-09(约)",
    pay="未公开", dur="暑期", lang="香港岗通常要求中英", visa="需持香港工作权利", gpa="未设",
    proc="—", pat="此前本表只记录 HL 香港的 off-cycle;这是 2027 批第一次出现正式的香港暑期岗",
    note="★ <b>9/20 新收录:HL 香港开了一个 2027 正式暑期岗,不是 off-cycle。</b>方向是 Financial Restructuring(破产重组/债务重组)——这是 HL 全球最强的产品线,香港能挂出暑期岗少见。⚠️ Workday 纯 JS 渲染,读不到截止日和完整 JD,请自己打开确认。")
add(firm="PJT Partners", org="EB", role="★ 2027 Summer Analyst (Strategic Advisory & Restructuring) — Hong Kong",
    func="IBD", typ="Summer", loc="香港", url="https://pjtpartners.wd1.myworkdayjobs.com/Students", st="open",
    ddl="", ddl_txt="窗口内:官方口径 10 月内关,无具体日",
    opened="2026-09(约)",
    pay="未公开", dur="未公开", lang="★官方:英文流利 + 至少一门亚洲语言", visa="未公开",
    gpa="未写数字;毕业窗口 Winter 2027 – Summer 2028——2028 届对口",
    proc="★PJT 官方要求做 Suited 测评;流程偏关系/networking 主导,无标准化 OA",
    pat="官方 Students 页原文:「open in September of the year prior to the program and close in October」——窗口极短",
    note="★★ <b>9/20:香港岗确认存在,而且正在窗口里。</b>岗位全名「2027 Summer Analyst (Strategic Advisory &amp; Restructuring) Hong Kong」,JD 覆盖 Strategic Advisory / Restructuring &amp; Special Situations / Private Capital Solutions 三条线,毕业窗口写的是 Winter 2027–Summer 2028。这是本表跟了两个月的岗,前几周查到的 2027 Summer Analyst 全是美国岗,这次终于出现香港条目。<br>⚠️ <b>但本表拿不到可用直链,不给伪造链接:</b>PJT 用 Workday,纯 JS 渲染,抓取只能拿到 meta 标签(本次用一个已收录的 PJT 职位页做过对照实测确认),香港这条的 req 号也没被搜索引擎收录。证据来自第三方完整转载的 JD 原文 + 官方 Students 页的时间口径。<b>请自己打开 Workday Students 板,按 Hong Kong 筛选。</b>官方只说 10 月关、不写具体日,窗口可能只有两三周——本周就去。")
add(firm="Moelis & Company", org="EB", role="Hong Kong Summer Analyst",
    func="IBD", typ="Summer", loc="香港", url="https://www.moelis.com/careers/explore-opportunities/", st="watch",
    ddl="", ddl_txt="官方称香港通常 5 月开", opened="",
    pay="未公开", dur="10 周", lang="未公开", visa="未公开", gpa="未公开",
    proc="无 OA;技术面偏重", pat="各大 tracker 均无香港 req 记录,公开讨论的 Moelis SA 2027 都是美国",
    note="9/20 复核:官方 tal.net 学生岗位板当前 7 类岗位<b>全部在美国</b>(NY/Houston/LA/Chicago/Boston/SF),<b>没有任何亚洲岗</b>;香港最近一次挂出还是 2024 批。按 networking 通道对待。")
add(firm="Rothschild & Co", org="EB", role="Global Advisory Summer Internship(香港)",
    func="IBD", typ="Summer", loc="香港", url="https://www.rothschildandco.com/en/careers/students-and-graduates/opportunities/", st="watch",
    ddl="", ddl_txt="未公布", opened="",
    pay="未公开", dur="未公开", lang="未公开", visa="未公开", gpa="未公开", proc="未公开",
    pat="香港项目每年复现(2026=opp 899,2025=opp 328)但页面从不写开放日期与截止",
    note="⚠️ <b>9/20 第三周复核,香港仍然没有岗。</b>2027 批的「Register Your Interest — Global Advisory Summer Analyst」登记页这次找回来了(上次消失),但<b>地点栏只写 Manchester 一个英国城市</b>,deadline 标 Ongoing;官方真正挂出的 2027 岗只有 Global Financing Solutions &amp; Restructuring(英国)。香港仍只有 2026 批那个老页面。连续三周无进展——Rothschild 香港今年的节奏明显慢于往年,但历年香港项目每年都复现(2026=opp 899,2025=opp 328),继续盯。")
add(firm="BDA Partners", org="EB", role="M&A Analyst Intern(六个月制,1H / 2H 两批)",
    func="IBD", typ="Offcycle", loc="香港", url="https://www.bdapartners.com/careers/students-graduates/", st="watch",
    ddl="", ddl_txt="滚动 / 不定期", opened="",
    pay="未公开", dur="★六个月(1–6月 或 6/7–12月),起止日期可绕课表",
    lang="★硬性:英文 + 中文(普通话和/或粤语)流利",
    visa="★硬门槛,但对本地学生有利:只招 香港永久居民 / 香港高校在读学生 / 持 IANG 签证者——不担保签证",
    gpa="未设 GPA;优先 penultimate;有金融实习经历者优先",
    proc="未公开", pat="无固定窗口,以 LinkedIn 单发 req 形式出现,需持续盯",
    note="★ 对港校学生最友好的六个月精品行通道,而且明写优先 penultimate。⚠️ <b>9/20 复核:官方 Students &amp; graduates 页七个地点(含香港)的 M&A Analyst Internship 状态全部是 Closed</b>,香港列出的 intake 周期只到 2026 年 Q4(9–12月),<b>没有 2027 批</b>。等它开下一批(按惯例对应 2027 年 1–6 月那档)。")
add(firm="Somerley 新百利", org="EB", role="speculative 直投(无公开实习岗)",
    func="IBD", typ="Offcycle", loc="香港", url="https://www.somerleycapital.com/en/careers/", st="watch",
    ddl="", ddl_txt="常年", opened="",
    pay="未公开", dur="—", lang="★全职 CF 岗要求 粤语+英文+普通话 三语流利,实习可参照", visa="未写", gpa="未设",
    proc="邮件直投 careers@somerley.com.hk", pat="—",
    note="香港最头部的独立财务顾问之一;careers 页目前只挂有经验岗,但邮箱就是入口。")
add(firm="Anglo Chinese 英高", org="EB", role="speculative 直投(官网开放 open application)",
    func="IBD", typ="Offcycle", loc="香港", url="https://www.anglochinesegroup.com/careers", st="watch",
    ddl="", ddl_txt="常年", opened="",
    pay="未公开", dur="—", lang="中文能力「advantageous」", visa="未写", gpa="未设",
    proc="邮件 careers@anglochinesegroup.com(附 CV 与薪酬期望);官方口径:三周内无回复即未通过", pat="—", note="")
add(firm="Altus Capital", org="EB", role="Summer Internship / Graduate Programme(IPO 保荐人)",
    func="IBD", typ="Offcycle", loc="香港", url="https://www.altus.com.hk/?page_id=428", st="open",
    ddl="", ddl_txt="★滚动收", opened="",
    pay="未公开", dur="8–10 周(暑期);graduate 全年", lang="要求中英文书面口语流利", visa="未写",
    gpa="写「excellent academics」,无数字", proc="邮件 careers@altus.com.hk(CV + cover letter)", pat="常年滚动",
    note="本身是港股 IPO 保荐人,做过 A 股/港股 IPO 的人在这里叙事最顺。公司承担考牌/会计培训费用。")
add(firm="Asian Capital", org="EB", role="Summer / Winter Internship — Corporate Financial Advisory",
    func="IBD", typ="Offcycle", loc="香港", url="https://www.asiancapital.com.hk/en/careers.php", st="open",
    ddl="", ddl_txt="★滚动收,冬夏两批", opened="",
    pay="未公开", dur="4–10 周", lang="要求英文 + 中文 + 普通话俱佳", visa="未写", gpa="未设",
    proc="邮件 careers@asiancapital.com.hk", pat="常年滚动",
    note="工作内容为客户材料与信息搜集(pitchbook 类)。本科硕士均可。")
add(firm="Admiralty Harbour 鐘港资本", org="EB", role="Internship Program(期末向管理层汇报)",
    func="IBD", typ="Offcycle", loc="香港", url="https://www.ahfghk.com/recruitment.php", st="open",
    ddl="", ddl_txt="★常年", opened="",
    pay="未公开", dur="未写", lang="未写",
    visa="★官方:为合资格的海外候选人安排 training visa——少数明确愿意办签证的本地行",
    gpa="未设(申请需附成绩单)", proc="邮件 hr@ahfghk.com(CV + 成绩单)", pat="常年",
    note="官方写明「open to all undergraduate and postgraduate students」,背景要 金融/会计/商科/数学/统计。")

# ============ 中资在港 ============
add(firm="中金公司 CICC(香港)", org="CN", role="香港 项目实习生(如东南亚组 J16945、研究部印度组)",
    func="IBD", typ="Offcycle", loc="香港", url="https://isd.pku.edu.cn/en/detail.php?id=401", st="open",
    ddl="", ddl_txt="滚动", opened="",
    pay="未公开", dur="至少 3 个月,全职优先或每周 3 天以上到岗",
    lang="中英双语,英文为工作语言", visa="未写", gpa="未设",
    proc="内地岗用 北森(Beisen)测评;香港项目实习生走邮件直投,无标准 OA",
    pat="★重要:香港日常实习不走 cicc.zhiye.com(那是内地校招/暑期),而是经 公众号「中金公司招聘」、高校就业网、团队邮件流转",
    note="★ 官方 portal 明文警告付费内推类中介。内地暑期项目 2026 批为 2月12日–3月15日,地点只有北京/上海/深圳,不含香港。")
add(firm="中金公司 CICC", org="CN", role="内地 暑期实习生(投行/研究/股票/固收/私募股权/资管 九个部门)",
    func="IBD", typ="Summer", loc="北京/上海/深圳", url="https://cicc.zhiye.com/", st="soon",
    ddl="", ddl_txt="预计 2027年2月中–3月中", opened="",
    pay="未公开", dur="未公开", lang="中文", visa="—", gpa="未设",
    proc="北森测评 + 笔试 + 面试", pat="★规律稳定:2026 批 2月12日–3月15日;2025 批 2月28日–3月30日",
    note="2027 批预计面向 2027年9月–2028年8月毕业者。")
add(firm="CITIC CLSA 中信里昂", org="CN", role="Internship Programme(8 周,6–8月)",
    func="RES", typ="Summer", loc="香港", url="https://citicclsa.wd3.myworkdayjobs.com/External", st="soon",
    ddl="", ddl_txt="预计 10–11月开,12/31 关", opened="",
    pay="未公开", dur="8 周(官方,中资里最短)", lang="posting 未特别写", visa="未提及",
    gpa="未设", proc="未公开",
    pat="项目每年复现(Jun–Aug,横跨 13 个国家),但申请窗口从不公开日期;2026 批截止 12月31日",
    note="★ 官方明确面向 penultimate 本科生,前台条线含 Sales / Sales Trading / Research。历史上「一年期实习」经 HKU CEDARS 等校园渠道发布——校内渠道要一起刷。<b>9/20 复核:仍未开。</b>Workday 板确认是 JS 渲染、读不到列表(是读不出,不是没岗位);官网实习页仍是无年份无日期的通用文案(6–8 月、两个月、13 国);<b>搜索索引里 2026 批那条已于 2025年12月30日下架(当时截止 12/31)</b>,没有 2027 条目。按未开处理,<b>10–12 月是主窗口</b>。")
add(firm="华泰国际 Huatai", org="CN", role="Project Intern, IBD / Equity Derivatives Intern / Institutional Equity Sales Intern",
    func="IBD", typ="Offcycle", loc="香港", url="https://htsc.wd102.myworkdayjobs.com/Huatai_Careers", st="open",
    ddl="", ddl_txt="滚动", opened="",
    pay="未公开", dur="未公开(香港实习惯例 3–6 个月、每周 3 天以上)", lang="IBD 岗需中英", visa="未写", gpa="未设",
    proc="未公开", pat="Workday 常年滚动补挂,无固定窗口",
    note="中资里目前在挂岗位最多的一家。板面为 JS 渲染,需用浏览器打开并筛 Internship + Hong Kong。")
add(firm="招银国际 CMBI", org="CN", role="项目实习生(20+ 部门含 IBD)",
    func="IBD", typ="Offcycle", loc="香港/深圳/上海/北京/新加坡", url="https://www.cmbi.com.hk/en-US/practice", st="open",
    ddl="", ddl_txt="滚动", opened="",
    pay="未公开", dur="3–6 个月(页面按「三天」到「六个月」分档筛选)", lang="要求中英文书面口语俱佳", visa="未写",
    gpa="项目实习生未设(SIP 要求 3.3+)", proc="未公开", pat="常年滚动",
    note="★ 本科生走这条通道,而不是 SIP。⚠️ 9/20 复核:部门筛选里确实含投资银行部、财富管理客户部、财富管理总部,<b>但职位列表为空且疑似 JS 动态加载,本环境无法证实现在是否真的在收</b>。用浏览器自己打开看一眼。")
add(firm="招银国际 CMBI", org="CN", role="Summer Internship Program(SIP,10 周)",
    func="IBD", typ="Summer", loc="香港", url="https://www.cmbi.com.hk/en-US/campus", st="soon",
    ddl="", ddl_txt="预计 10月中–11月中", opened="",
    pay="未公开", dur="10 周(官方)", lang="★硬性:中英文书面口语俱佳",
    visa="未写", gpa="★GPA ≥3.3",
    proc="未公开(站内能力测试,供应商未披露)",
    pat="2026 批:10月中投递–11月中截止,2月起发 offer",
    note="⚠️ 资格很窄:官方写「待入学硕士生或在读硕士生」——本科生原则上不符,走上面的项目实习生通道。<b>9/20 复核:仍未启动。</b>校园页时间轴一字未动,还是「Campus Recruitment Seminars(Oct–Nov 2025)」「Application Opens(Mid Oct–Mid Nov 2025)」「Offer Release(Feb 2026 Onwards)」,咨询邮件主题模板仍写「Enquiry - 2026 SIP」。按这个时间轴,2027 批应在 <b>10 月中</b>启动,下次核查重点盯。")
add(firm="海通国际 Haitong Intl", org="CN", role="Summer Internship Program",
    func="IBD", typ="Summer", loc="香港", url="https://htisec.wd3.myworkdayjobs.com/en-US/hti_careers", st="soon",
    ddl="", ddl_txt="预计 2027年初", opened="",
    pay="未公开", dur="未公开", lang="未公开", visa="未公开", gpa="未设", proc="未公开",
    pat="2026 批 req 编号为 R25000212(2025年提的需求),推断上一年末开",
    note="母公司已并入 国泰海通;2027 批可能与国君国际合并招聘,两边都要盯。")
add(firm="国泰君安国际 GTJAI", org="CN", role="Internship(滚动补挂)",
    func="IBD", typ="Offcycle", loc="香港", url="https://www.gtjai.com/en/career", st="watch",
    ddl="", ddl_txt="不定", opened="",
    pay="未公开", dur="未公开", lang="未公开", visa="未公开", gpa="未设", proc="—",
    pat="官网目前只挂有经验 Analyst 岗", note="实习多为 ad hoc,可投 recruitment@gtjas.com.hk。")
add(firm="中银国际 BOCI", org="CN", role="Summer / 招聘平台岗位",
    func="IBD", typ="Summer", loc="香港", url="https://boci.recruitmentplatform.com/", st="watch",
    ddl="", ddl_txt="不定", opened="",
    pay="未公开", dur="未公开", lang="未公开", visa="未公开", gpa="未设", proc="—",
    pat="无公开规律", note="平台上目前多为正式 Analyst/Associate 岗。")
add(firm="招商证券国际 CMS", org="CN", role="Summer Internship / 校园招聘",
    func="IBD", typ="Summer", loc="香港", url="https://www.cmschina.com.hk/Career/CampusRecruit", st="watch",
    ddl="", ddl_txt="预计 2–4月", opened="",
    pay="未公开", dur="未公开", lang="中英", visa="未写", gpa="未设",
    proc="历年经 公众号 + 邮箱收简历", pat="—", note="简历可直投 recruit@cmschina.com.hk。")

# ============ 买方 / 对冲基金 / 量化 ============
add(firm="Point72", org="BUY", role="2027 Point72 Academy Investment Analyst Summer Internship",
    func="BUY", typ="Summer", loc="香港(新加坡另有岗)", url="https://job-boards.greenhouse.io/point72/jobs/8491055002", st="open",
    ddl="", ddl_txt="两波:5月中(早批 AC)/ 夏–秋中(晚批 AC)", opened="",
    pay="未公开", dur="8 周(2027年6–8月,官方)",
    lang="官方:需具备一门亚洲语言的优秀书面与口头表达能力", visa="未写",
    gpa="未设数字,但★申请需提交 成绩单 + 入学考试成绩 + 命题作文",
    proc="站内 OA → 与 Academy 团队远程一对一面试 → Assessment Centre",
    pat="开得极早、跑得极长:早批 5月中截、晚批到秋中",
    note="★ 全球只能投一份(HK 或 SG 二选一)。毕业窗口 2027年12月–2028年7月。官方明令禁止用生成式 AI 写申请。<b>9/20 复核:仍开,卡片链接已换成可直接投递的 Greenhouse 页(job code CPA-0014708),比原来的 careers.point72.com 转跳页好用。</b>官方仍不写具体截止日,只说两个 AC 窗口——现在属于第二个(夏末至秋中),<b>也就是说晚批窗口正在走,别拖到 11 月</b>。")
add(firm="Citadel", org="BUY", role="International Equities — Intern (Asia)",
    func="BUY", typ="Summer", loc="香港/新加坡", url="https://www.citadel.com/careers/details/international-equities-intern-asia/", st="open",
    ddl="", ddl_txt="在挂,页面带完整申请表单", opened="2026-07-25",
    pay="未公开", dur="全球惯例 11 周(香港未确认)", lang="未写", visa="未写", gpa="未设",
    proc="技术类走 HackerRank 式 OA / CoderPad;★不用录播视频,全程真人面试",
    pat="按台子滚动挂,无固定窗口——7/25 上线、一周左右即从站内列表消失,印证 Citadel 关得极快",
    note="★ <b>9/20:恢复「已开放」——上次的「疑似下架」没有复现。</b>本次直接打开原链接,页面正常渲染且<b>带完整申请表单</b>,地点写明 Hong Kong + Singapore,实习期以 6–8 月为主、另可选 9–12 月或 1–4 月。8/3 那次很可能是站内列表的临时抓取问题而非真下架。⚠️ 注意 Citadel 的页面不按「2027」命名,是常驻岗位页,所以无法从标题判断批次;也不写截止日,按「说关就关」对待。技术类走 HackerRank 式 OA,★全程真人面试不用录播。")
add(firm="Citadel Securities", org="QUANT", role="2027 Quantitative Research Analyst Intern (BS/MS), Asia",
    func="QUANT", typ="Summer", loc="香港/新加坡", url="https://www.citadelsecurities.com/careers/details/quantitative-research-analyst-intern-bs-ms-asia/", st="open",
    ddl="", ddl_txt="滚动,关得早", opened="",
    pay="未公开", dur="11 周(6–8月)", lang="未写", visa="未写", gpa="未设",
    proc="同上:HackerRank 式 OA → 真人技术面(概率/统计/编程)", pat="按角色滚动",
    note="要强数理 + Python/C++。全部在挂岗位见 citadel.com/careers/internships。")
add(firm="Millennium", org="BUY", role="Off-Cycle Trading Intern — Quantitative Researcher(REQ-27841)",
    func="QUANT", typ="Offcycle", loc="香港", url="https://career.mlp.com/careers/job/755953995891-off-cycle-trading-intern-quantitative-researcher-hong-kong-hong-kong?domain=mlp.com", st="watch",
    ddl="", ddl_txt="❌ 已下架(链接 404)", opened="",
    pay="未公开", dur="3–6 个月,全职", lang="未写", visa="未写", gpa="未设",
    proc="★因岗而异,官方明说没有统一组合", pat="香港 off-cycle 岗全年不定期上新",
    note="❌ <b>9/20:已下架。</b>原链接返回 <b>404</b>,且 career.mlp.com 香港现有的 10 个岗位里<b>没有任何实习岗</b>(全是 Paralegal、Market Data Engineer、Risk Controls Manager 这类正式岗)——两条证据一致。从可投列表下掉。★ 内容曾是亚太股票统计套利研究,要 Python/C++、熟悉 ML/LLM。Millennium 的校园批(下一条)不受影响,仍在收;off-cycle 岗全年不定期上新,可继续盯 career.mlp.com。")
add(firm="Millennium", org="BUY", role="2027 Internship Program(★8/3 已开放,香港 10 个岗上线)",
    func="QUANT", typ="Summer", loc="香港/新加坡等", url="https://campusjobs.mlp.com/careers?domain=mlp.com&microsite=campus-site", st="open",
    ddl="", ddl_txt="滚动审,无硬截止", opened="2026-08-03",
    pay="未公开", dur="未公开", lang="未写", visa="未写", gpa="未设",
    proc="因岗而异", pat="官网原文「roles will be filled on a rolling basis」——滚动补位,先到先得",
    note="★★ 9/20 核验:香港<b>仍是 11 个岗,无关闭迹象</b>,REQ 号已核到:2027 Quantitative Researcher(REQ-30209)、Execution Trading(REQ-30188)、Quantitative Developer(REQ-30359)、Data &amp; Research Strategy(REQ-30493)、Sector Specialist(REQ-30210)、Trading Services(REQ-30211)、Applied AI Engineer(REQ-30169)、Corporate Access Services(REQ-30182)、Operations &amp; Middle Office(REQ-30199)等,另有一个 2026 off-cycle(AI Engineering,REQ-30687)。前台相关度最高的是 Sector Specialist、Execution Trading、Corporate Access Services、Quantitative Researcher。⚠️ <b>官方原文确认「individuals may only submit up to two (2) applications, including applications for different locations」——最多两份,跨地点也算。</b>无公布截止日,滚动补位,<b>已经开了七周了,再拖就是抢剩下的坑</b>。")
add(firm="Schonfeld", org="BUY", role="2027 Summer Internships — Express Your Interest(含香港)",
    func="BUY", typ="Summer", loc="香港/纽约/伦敦等", url="https://job-boards.greenhouse.io/schonfeld/jobs/7635430", st="open",
    ddl="", ddl_txt="登记池已开,具体岗位陆续放出", opened="2026-08(约)",
    pay="未公开", dur="12–16 周", lang="未写", visa="未写", gpa="申请表需填 GPA(未设数字线)",
    proc="先登记 → 具体岗位上线后官方提示尽快申请", pat="多策略对冲基金,按岗位滚动放出",
    note="★ 8/10 新增收录:办公地点明确列出香港。目前是提前登记池(类似 Fidelity 的 register interest),投资/量研/数据方向的正式 req 会陆续放出——先登记占位。eligibility 细则页面未写清,登记后以后续岗位 JD 为准。")
add(firm="Schroders 施罗德", org="BUY", role="Asia Internship Programme(香港,penultimate,待开)",
    func="BUY", typ="Summer", loc="香港", url="https://www.schroders.com/en-hk/hk/institutional/about-us/careers/internships-and-placements/", st="soon",
    ddl="", ddl_txt="⚠️ 窗口已到(官方:9 月开申),香港岗未证实", opened="",
    pay="未公开", dur="暑期(次年 6 月入职)", lang="未写", visa="未写", gpa="未设",
    proc="未公开", pat="官方口径:penultimate 年 9 月申请、次年 6 月入职",
    note="★ 老牌英资资管,官网明示亚洲实习面向 penultimate、9 月开申。<b>⚠️ 9/20:窗口就是现在,但本表无法证实香港岗是否已上架——这条需要你自己点一次。</b>官方 FAQ 原文仍是「Applications <b>open in September each year</b>. We recruit on a <b>rolling basis</b>」「Our internships are for <b>penultimate year undergraduate students only</b>」,口径完全对口;但香港实习页上只有一个 Apply now 按钮、不写年份也不写截止日,搜索也没命中任何 Schroders 香港 2027 职位页。<b>建议直接点那个 Apply now 看跳转后的职位列表</b>——滚动招聘意味着早投有实质优势。")
add(firm="Jane Street", org="QUANT", role="Quantitative Researcher — Summer Internship",
    func="QUANT", typ="Summer", loc="香港", url="https://www.janestreet.com/join-jane-street/open-roles/", st="watch",
    ddl="", ddl_txt="⚠️ 已提前关闭", opened="",
    pay="未官方公开(美国口径约 US$4.8k/周);暑期通常提供住宿", dur="10–12 周(5–9月),另有 off-cycle",
    lang="未写", visa="未写(官方注明已毕业者也可参加实习)", gpa="未设",
    proc="★电话/线上心算速度筛 → 全程真人面试(概率、心算、交易游戏),不用异步录播",
    pat="香港按角色错峰关闭,滚动收——本轮验证:实际关闭远早于索引页显示的日期",
    note="⚠️ 8/3 核验:官网已把此岗转到 closed 页,原文「not currently accepting applications」——比原记的 8/18 提前两周以上关闭。想收开放通知可在官网 closed 页点 Notify Me。")
add(firm="Jane Street", org="QUANT", role="Sales and Trading — Summer Internship",
    func="S&T", typ="Summer", loc="香港", url="https://www.janestreet.com/join-jane-street/position/8630687002/", st="open",
    ddl="", ddl_txt="无官方截止,滚动收、随时关", opened="",
    pay="同上", dur="10–12 周(5–8月)", lang="未写", visa="未写", gpa="未设", proc="同上", pat="同上",
    note="★★ <b>9/20 复核:仍开,但 job ID 变了,卡片链接已更新。</b>现行官方在挂版本是 position <b>8630687002</b>(旧的 8093915002 已不是当前版本),页面有 Apply 按钮,<b>目标毕业年份写的是 2028——正好是你这届</b>。QR 与 QT 两个香港岗仍然关着(QT 的官方 URL 路径现在直接叫 closed-internship),所以<b>这依然是 Jane Street 香港唯一还开的暑期前台岗</b>。不写截止日,按「说关就关」对待。")
add(firm="Jane Street", org="QUANT", role="Quantitative Trader — Summer Internship",
    func="QUANT", typ="Summer", loc="香港", url="https://www.janestreet.com/join-jane-street/open-roles/", st="watch",
    ddl="2026-07-30", ddl_txt="7/30 已关(官网确认)", opened="",
    pay="同上", dur="10–12 周", lang="未写", visa="未写", gpa="未设", proc="同上", pat="同上",
    note="8/3 核验已关闭。<b>9/20 复核仍关:官方 URL 路径现在直接是 <code>/closed-internship/quantitative-trader-may-august-hkg/</code></b>——连 URL 都改成 closed 了。QR 香港同样仍关(搜索只返回伦敦的 closed 页)。想收开放通知,在官网 closed 页点 Notify Me。")
add(firm="Qube Research & Technologies", org="QUANT", role="Internship / Graduate — Quantitative Research & Trading",
    func="QUANT", typ="Offcycle", loc="香港/新加坡/上海", url="https://job-boards.greenhouse.io/quberesearchandtechnologies/jobs/8021267002", st="open",
    ddl="", ddl_txt="滚动", opened="",
    pay="未公开", dur="★3–6 个月,申请表里自选时长与起始月",
    lang="未写", visa="未写", gpa="未设(要求 penultimate 或 final year 本硕博)",
    proc="HackerRank 式在线测评 → 实习岗有视频面", pat="滚动",
    note="★ 天然的 offcycle 结构:自己填想做多久、几月开始。可转正。<b>9/20 复核:QRT 官方 Greenhouse 板现有 6 个 2027 实习岗,香港全覆盖</b>——Quantitative Research &amp; Trading(港/新/沪/京)、Data Engineering、Infrastructure Engineering、FPGA Engineering(仅香港)、Security Engineer(仅香港)、Software Engineer。均无截止日。前台口径下重点是第一个。")
add(firm="BlackRock", org="BUY", role="2027 Summer Internship Program — APAC",
    func="BUY", typ="Summer", loc="香港/新加坡/东京", url="https://careers.blackrock.com/job/hong-kong-sar/2027-summer-internship-program-apac/45831/90599500992", st="open",
    ddl="", ddl_txt="滚动", opened="2026-06",
    pay="未公开", dur="posting 未写", lang="未写", visa="未提及",
    gpa="未设;要求 penultimate,2027年9月–2028年8月毕业",
    proc="★站内录播式 pre-interview assessment,必须在收到邮件后 5 天内完成,否则申请自动作废;技术岗另有编程测评",
    pat="★req 早在 2026年1月中就挂出,但明写「香港与新加坡 2026年6月开放申请」——早看到不等于早能投",
    note="★ 最多可投 2 个 function。覆盖组合管理、投资产品策略与方案等投资侧条线。")
add(firm="Blackstone", org="BUY", role="Summer Analyst / Off-cycle(香港岗按台子单发)",
    func="BUY", typ="Summer", loc="香港/上海/新加坡", url="https://blackstone.wd1.myworkdayjobs.com/Blackstone_Campus_Careers", st="open",
    ddl="", ddl_txt="滚动", opened="",
    pay="未公开", dur="Summer 约 10 周;off-cycle 六个月", lang="未写", visa="未写", gpa="未设",
    proc="无标准化 OA;技术面 + fit 都很重",
    pat="⚠️ 香港岗不走统一 APAC 窗口,而是按团队零散上线(如 2026 Credit/ICS Summer Analyst HK、2025 Business Finance off-cycle HK),需全年盯板",
    note="部分 2027 岗 2026年1月就开了、可能已满。板内需自行筛 Hong Kong。★ 上周那条「可能改名」的线索本周已坐实,见下一条独立卡片。")
add(firm="Blackstone", org="BUY", role="★ 2027 Transaction Finance Off-cycle Intern (Jan–Jun) — Hong Kong(req 44171)",
    func="BUY", typ="Offcycle", loc="香港", url="https://blackstone.wd1.myworkdayjobs.com/Blackstone_Campus_Careers/job/Hong-Kong/XMLNAME-2027-Transaction-Finance-Off-cycle-Intern--January-to-June--Hong-Kong_44171", st="open",
    ddl="", ddl_txt="在挂,Workday 页读不到截止日", opened="2026-09(约)",
    pay="未公开", dur="★六个月(2027年1–6月)", lang="未写", visa="未写", gpa="未设",
    proc="无标准化 OA;技术面 + fit 都很重",
    pat="历年叫 Business Finance 六个月 off-cycle,2027 批改名 Transaction Finance",
    note="★★ <b>9/20:跟了一个多月的那个岗坐实了——Blackstone 香港的六个月 off-cycle 确实改名叫「Transaction Finance」,而且已经在挂,req 44171。</b>上周只是第三方聚合站的未证实线索,本周该聚合站(当日更新)列出的 Blackstone 香港唯一岗位就是它。<br>⚠️ Blackstone 用 Workday,纯 JS 渲染,本环境读不到正文和截止日,<b>链接按聚合站列出的官方 Workday 路径给出,投前请自己打开确认</b>。对 2028 届来说,六个月 off-cycle(1–6月)意味着要请一个学期的假,想清楚再投。")
add(firm="Blackstone", org="BUY", role="2027 Real Estate Summer Analyst — Shanghai/Hong Kong",
    func="BUY", typ="Summer", loc="上海/香港", url="https://blackstone.wd1.myworkdayjobs.com/en-US/Blackstone_Campus_Careers/job/XMLNAME-2027-Blackstone-Real-Estate-Summer-Analyst---Shanghai-Hong-Kong_40595", st="open",
    ddl="", ddl_txt="滚动(Blackstone 惯例关得早)", opened="2026-07(约)",
    pay="未公开", dur="约 10 周", lang="覆盖大中华区,实操需中英", visa="未写", gpa="未设",
    proc="无标准化 OA;技术面 + fit 都很重",
    pat="Blackstone 香港 2027 校招板 7 月起上新,此岗为首批",
    note="★ 8/3 新发现:Blackstone 2027 香港校招板的第一个前台岗——地产投资条线。地点上海/香港双选。⚠️ <b>9/20 复核:倾向已下架,但证据不足以断言。</b>官方 Workday URL 仍被搜索索引(JS 渲染读不到正文),但第三方聚合站的在挂列表里<b>亚洲只剩东京两个和新加坡一个(44960),req 40595 已不在列</b>,另一个镜像返回 404。<b>投前务必自己登录 Workday 亲眼确认</b>——同板的 Transaction Finance off-cycle(见上一条)确认在挂,说明板子本身是活的。")
add(firm="KKR", org="BUY", role="2027 Summer Analyst Program(含亚太)",
    func="BUY", typ="Summer", loc="含亚太", url="https://www.kkr.com/careers/student-careers/student-career-opportunities", st="open",
    ddl="", ddl_txt="滚动", opened="",
    pay="未公开", dur="未公开", lang="未写", visa="未写", gpa="未设", proc="未公开",
    pat="无香港 dated 证据;历史上香港 off-cycle(如 PE 8–12月批)在春季挂",
    note="board 内需自行筛 Hong Kong / Singapore。")
add(firm="Fidelity International", org="BUY", role="Hong Kong Internship — Register Your Interest",
    func="BUY", typ="Summer", loc="香港", url="https://fidelityinternational.tal.net/vx/mobile-0/brand-0/candidate/so/pm/2/pl/6/opp/1258-Register-Your-Interest-2026-Internship-Programme-Hong-Kong/en-GB", st="open",
    ddl="", ddl_txt="登记常年开", opened="",
    pay="未公开", dur="10 周", lang="未写", visa="未写", gpa="未设",
    proc="站内 OA(认知 + 性格)→ 官方:视频面是与用人经理的第一次见面",
    pat="采用「先登记、开放再通知」模式,无公开窗口",
    note="今天顺手登记,开放时自动通知。官方明确面向 penultimate。")
add(firm="Flow Traders", org="QUANT", role="Trading Intern(APAC)",
    func="QUANT", typ="Summer", loc="香港", url="https://www.flowtraders.com/careers/job-description/8102618", st="open",
    ddl="", ddl_txt="招满即止(2027年6–7月批)", opened="",
    pay="★官方口径「competitive internship salary」,并为录取的海外申请者提供机票与住宿(非数字)",
    dur="6 周(2024 批 6月17日起,全表最短)",
    lang="未写", visa="要求人在或将返回亚太地区", gpa="未设",
    proc="★邮件发来的自研在线测评(心算/逻辑),再进面试",
    pat="滚动、招满即止,无固定月份;香港岗是与纽约岗分开的独立 req",
    note="★ <b>9/20 更新:2027 批香港岗已明确,卡片链接已换成新 req(8102618)。</b>官方页写明 intake 为 <b>2027年6–7月 或 2027年12月–2028年1月</b>,6 周带薪,海外申请者提供机票住宿——<b>此前担心的「2028 届超窗」问题在这一批不存在了</b>。无截止日,滚动招满即止。要 Python/MATLAB/R。")
add(firm="Eclipse Trading", org="QUANT", role="Trading Intern(香港,年度批次)/ 现挂 Junior Trading Analyst",
    func="QUANT", typ="Summer", loc="香港", url="https://www.eclipsetrading.com/all-jobs", st="soon",
    ddl="", ddl_txt="预计 9–10月开下一批", opened="",
    pay="交易岗未公开(Levels.fyi 有 SWE 实习约 US$22/小时,非前台)", dur="未公开",
    lang="未写", visa="未写", gpa="未设", proc="未公开", pat="常年滚动,无公开窗口",
    note="香港本土期权做市商。⚠️ 9/20 复核:仍未开。官方 Greenhouse 上 2027 批只有 <b>Graduate Trader | 2027 Intake,而且地点是悉尼</b>;Trading Intern 最新被收录的仍是 2026 Summer Intake。注意官方 all-jobs 页是 JS 渲染读不到正文,所以不排除有未被索引的新岗——但<b>没有任何 2027 实习岗的证据</b>。按规律 9–10 月开,继续盯。")
add(firm="IMC Trading", org="QUANT", role="★ Quantitative Trader Intern 2027 — Hong Kong",
    func="QUANT", typ="Summer", loc="香港", url="https://www.imc.com/eu/careers/jobs/4941205101", st="open",
    ddl="", ddl_txt="在挂(官方页写 APPLICATIONS NOW OPEN),未写截止", opened="",
    pay="未公开", dur="10 周(2027年5/6月起)", lang="未写", visa="未写",
    gpa="★官方明确要求<b>已进入 penultimate year</b>——完全对口",
    proc="做市商惯例:心算/概率速度测评 → 技术面 + 交易游戏", pat="IMC 亚太实习按年度批次放,香港与阿姆斯特丹/芝加哥分开 req",
    note="★ <b>9/20 新增收录。</b>荷兰系头部做市商,香港是其亚太主场之一,和 Optiver / Flow Traders / Jane Street 同一档的量化交易台子。<b>资格原文明确写「已进入 penultimate year」,是本表少见的、把你这届写得毫不含糊的岗位。</b>项目页写着「APPLICATIONS NOW OPEN」,但不写截止日——做市商惯例是招满即止,别拖。")
add(firm="Susquehanna (SIG)", org="QUANT", role="★ Equity Analyst Internship: Summer 2027 — Hong Kong",
    func="RES", typ="Summer", loc="香港", url="https://careers.sig.com/quantitative-trading-internships-co-ops/jobs/11361?lang=en-us", st="open",
    ddl="", ddl_txt="在挂,未写截止", opened="",
    pay="未公开", dur="2027 年 6 月起", lang="未写", visa="未写",
    gpa="⚠️ 页面未写明学位层级,本科是否符合<b>未证实</b>,投前自己确认",
    proc="SIG 惯例:概率/扑克/心算类测评 → 多轮技术面",
    pat="SIG 香港把研究岗和交易岗放在同一个招聘目录下",
    note="★★ <b>9/20 新增收录,而且它本身就是一条「藏在非直觉目录」的新教训:SIG 把这个 Equity Research 岗挂在 <code>quantitative-trading-internships-co-ops</code> 路径下,不在 research 目录里</b>——和 JPM 把研究岗挂在 Markets 目录下是同一类坑。部门名就叫 Equity Research。全港 2027 批的股票研究实习本来只有三个、本周 HSBC 关掉一个只剩两个,这条把数量补了回来。⚠️ 但页面没写学位层级要求,<b>本科 penultimate 是否符合资格未证实</b>,投之前自己看清楚。")
add(firm="Susquehanna (SIG)", org="QUANT", role="Hong Kong + Singapore Discovery Program: April 2027",
    func="QUANT", typ="Offcycle", loc="香港/新加坡", url="https://careers.sig.com/jobs/11453?lang=en-us", st="open",
    ddl="", ddl_txt="在挂,未写截止", opened="",
    pay="未公开", dur="2027 年 4 月,短期", lang="未写", visa="未写",
    gpa="页面未写明,但 insight 类项目通常正是给 penultimate 的",
    proc="同上", pat="insight / spring week 类型的短期项目",
    note="★ 9/20 新增收录。覆盖 Quantitative Trading 与 Strategy 两条线的短期 insight 项目(不是正式实习),<b>这类项目的价值在于它常常是正式暑期岗的前置漏斗</b>——参加过的人在下一年的正式批里有优势。2027 年 4 月举办,港新两地。资格未写明学位层级,自己确认。")
add(firm="PIMCO", org="BUY", role="★ 2027 Summer Internship, Account Analyst — APAC(香港)",
    func="BUY", typ="Summer", loc="香港", url="https://www.pimco.com/hk/en/about-us/careers/students/internships", st="open",
    ddl="", ddl_txt="在挂,未见截止日", opened="",
    pay="未公开", dur="暑期", lang="未写", visa="未写",
    gpa="★官方:本科/硕士,<b>预计毕业 2027年12月–2028年6月</b>——精准命中 2028 届",
    proc="未公开", pat="全球最大债券资管之一,香港是其亚太客户与投资平台",
    note="★ <b>9/20 新增收录。</b>PIMCO 香港的 2027 暑期岗,资格写明毕业窗口 Dec 2027–June 2028,正好是你这届。Account Analyst 是客户投资组合方向(介于投资与客户覆盖之间的前台岗),不是纯组合管理。<br>⚠️ <b>官方 Workday 直链本次未能证实</b>(Workday 页 JS 渲染抓不到、LinkedIn 被 robots 禁抓),岗位与资格原文是从第三方完整转载页读到的。<b>所以卡片链接给的是 PIMCO 官方学生实习入口页,请从那里进去找这个岗,不给伪造的直链。</b>")
add(firm="HKMA 香港金管局", org="BUY", role="Winter Internship(储备管理部属买方投资)",
    func="BUY", typ="Offcycle", loc="香港", url="https://www.hkma.gov.hk/eng/about-us/join-us/opportunities-for-students-and-graduates-to-join-the-hkma/internship/", st="watch",
    ddl="", ddl_txt="⚠️ 9/11 挂出新公告,内容未证实", opened="2026-09-11",
    pay="未公开", dur="冬季短期", lang="中英", visa="预计限香港身份", gpa="未设",
    proc="未公开", pat="金管局实习分寒暑两批,按公告单发",
    note="★ 9/20 新增收录(线索级,未证实)。金管局 9月11日新挂了一条 Winter Internship 招聘公告,URL 真实、两次独立搜索都命中,<b>但页面是 JS 渲染,资格与截止日读不到</b>,所以只记为待观察。<b>收录它的理由:金管局的 Reserves Management Department(外汇基金投资)是香港体量最大的买方投资平台之一</b>,学生岗极少见,值得自己点开确认一次。")
add(firm="明汯投资 Minghong", org="QUANT", role="2026 quant research / quant dev / AI 算法 实习",
    func="QUANT", typ="Offcycle", loc="上海/北京/香港", url="https://www.wondercv.com/xiaozhao/minghong-investment-2026-intern-shanghai-beijing-hk-9520-1d0067", st="open",
    ddl="", ddl_txt="滚动", opened="",
    pay="未公开", dur="未公开", lang="中文", visa="—", gpa="★未设 GPA",
    proc="简历 + 面试(无标准化 OA 记录)", pat="—",
    note="★ 明写 2027 届及以后可投(2028 届符合),要 STEM + C++/Python/CUDA。走官网或邮箱,标题格式[学校-岗位-姓名]。")
add(firm="GIC", org="BUY", role="GIC Internship Programme(12 周)",
    func="BUY", typ="Summer", loc="新加坡", url="https://gic.careers/programmes/gic-internship-programme/", st="open",
    ddl="", ddl_txt="滚动审,鼓励早投", opened="2026-08(约)",
    pay="未公开", dur="12 周(官方)", lang="未写",
    visa="官方:面向任何国籍的 penultimate 与 pre-penultimate 学生", gpa="未设",
    proc="坊间报告为 Predictive Index(PI)认知测评", pat="通常 8–9月开;本轮如期",
    note="★ 8/3 核验:官网 Apply Now 通道已可用,原文「Applications are reviewed on a rolling basis…apply early」。⚠️ 页面未标批次年份,投前自行确认是 2027 暑期批;学生招聘以新加坡为主,未见香港席位——需要接受去新加坡。")
add(firm="Temasek", org="BUY", role="Summer Internship Programme 2027 — Investment Group(新加坡)",
    func="BUY", typ="Summer", loc="新加坡", url="https://jobs.temasek.com.sg/job/Temasek-Summer-Internship-Programme-2027-Investment-Group-(Singapore)-238891/1365905957/", st="open",
    ddl="2026-09-11", ddl_txt="9/11(滚动审)", opened="2026-08(约)",
    pay="未公开", dur="12 周", lang="未写", visa="未写", gpa="未设", proc="未公开",
    pat="2027 暑期批 8 月初挂出、9/11 截止;1–6月 project intern 批仍未见",
    note="★ 8/10 核验:2027 暑期批 Investment Group 岗已开放申请,滚动审。⚠️ 仍是新加坡建制,无香港席位;想做主权基金投资侧且接受 SG 的,这和 GIC 是同窗口的两枪。")

# ============ VC / Crypto ============
add(firm="Alibaba Entrepreneurs Fund", org="VC", role="Internship Program — 20 个岗位(含 Investment Analyst / Data Analyst / Quantitative Researcher)",
    func="BUY", typ="Offcycle", loc="香港", url="https://www.ent-fund.org/en/internship/positions", st="open",
    ddl="", ddl_txt="在挂", opened="",
    pay="未公开", dur="未公开", lang="多个岗位写明 中英文书写口语流利", visa="未写", gpa="★未设,任何专业",
    proc="按岗位单独申请", pat="—",
    note="★ 覆盖 AEF 本体与生态被投(Qupital、Aqumon、Gobi 等)。一个入口拿多个投资侧机会。")
add(firm="Gobi Partners", org="VC", role="Internship Programme(总部在香港)",
    func="BUY", typ="Offcycle", loc="香港 / 区域办公室", url="https://www.gobi.vc/internship-programme", st="open",
    ddl="", ddl_txt="★滚动", opened="",
    pay="未公开", dur="配合学期时间安排", lang="未写", visa="未写", gpa="未设",
    proc="邮件 careers@gobi.vc,标题写「Internship Programme」", pat="常年滚动",
    note="★ 官方明写「不要求有 VC 经验」,强调好奇心与独立工作能力。时长可绕课表。")
add(firm="Animoca Brands", org="VC", role="Investments & Strategic Partnerships(IAP/ISP)Internship",
    func="BUY", typ="Offcycle", loc="香港 / 新加坡", url="https://jobs.lever.co/animocabrands/a451e86e-b1bf-4317-bf3c-f56f84444ad6", st="open",
    ddl="", ddl_txt="滚动", opened="2026-07",
    pay="未公开", dur="2026年6–12月,全职优先,现场办公", lang="未写", visa="未写", gpa="★未设",
    proc="Lever 直投", pat="—",
    note="投资研究、Web3 尽调、投资人材料。要 Excel/PPT,Python/SQL 加分。")
add(firm="CMCC Global", org="VC", role="Credit Fund Systems and Operations Analyst(全职,可谈实习变体)",
    func="BUY", typ="Offcycle", loc="香港", url="https://www.cmcc.vc/careers", st="open",
    ddl="", ddl_txt="在挂", opened="",
    pay="未公开", dur="全职", lang="未写", visa="未写", gpa="未设",
    proc="邮件 careers@cmcc.vc(CV + cover letter),标题「Application」", pat="—",
    note="比特币信贷基金,JD 要 Excel/Python + 系统设计。HashKey / Galaxy Digital 的 2027 批建议 9–10月盯 Greenhouse。")

# ============ 私人银行 / 财富管理(前台) ============
add(firm="J.P. Morgan Private Bank", org="BB", role="2027 Global Private Bank — Advisor Program Summer Internship",
    func="PB", typ="Summer", loc="香港", url="https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210745326", st="open",
    ddl="2026-09-30", ddl_txt="9/30(滚动审)", opened="2026-06-01",
    pay="未公开", dur="9 周(2027年6–8月)", lang="英文流利", visa="未提及", gpa="无 GPA 数字",
    proc="网申 → HireVue 录播视频面(必做)→ 面试;滚动审",
    pat="与 JPM 香港其他 2027 岗同批,2026年6月1日上线、9月30日截止",
    note="★ RM / Advisor 轨,是全港最正统的私行前台暑期岗。项目主页:privatebank.jpmorgan.com/apac/en/about-us/careers/early-career-programs")
add(firm="J.P. Morgan Private Bank", org="BB", role="2027 Global Private Bank — Investment Solutions Program Summer Internship",
    func="PB", typ="Summer", loc="香港", url="https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210745269", st="open",
    ddl="2026-09-30", ddl_txt="9/30(滚动审)", opened="2026-06-01",
    pay="未公开", dur="9 周(2027年6–8月)", lang="英文流利", visa="未提及", gpa="无 GPA 数字",
    proc="同上:HireVue 录播必做 → 面试", pat="同上",
    note="★ 投资顾问 / 投资方案研究轨,比 Advisor 轨更偏投研。与上面那个是两份独立申请。")
add(firm="UBS Global Wealth Management", org="BB", role="2027 Off-Cycle Internship — GWM Solutions",
    func="PB", typ="Offcycle", loc="香港", url="https://jobs.ubs.com", st="watch",
    ddl="", ddl_txt="⚠️ 8/24 官方职位库查无此岗", opened="",
    pay="未公开", dur="通常 6 个月", lang="APAC off-cycle 要求倒数第二年在读、<2年工作经验", visa="未写", gpa="无 GPA 数字",
    proc="UBS 线上测评 → 录播视频面 → 终面", pat="2027 off-cycle 与 summer 同批 7 月上线",
    note="⚠️ 核查结论:UBS 香港本轮**没有 GWM 暑期岗**,私行学生招聘只走 off-cycle。网传的 GWM Summer(jobid 339032)是美国纽约/新泽西岗且已过期。另一个 GWM COO off-cycle 属中后台,不在本表口径内。")
add(firm="Citi Private Bank", org="BB", role="Wealth – Private Bank, Summer Analyst, Hong Kong, 2027",
    func="PB", typ="Summer", loc="香港", url="https://jobs.citi.com/job/hong-kong/wealth-private-bank-summer-analyst-hong-kong-2027/287/99664839120", st="open",
    ddl="2026-10-30", ddl_txt="10/30 23:59(滚动审)", opened="2026-08-24",
    pay="未公开", dur="★官方:10 周暑期项目,开头有集中培训",
    lang="英文", visa="未写",
    gpa="posting 未设 GPA;官方写「任何本科专业均可」「不要求丰富工作经验」",
    proc="Plum 测评 → 录播视频面 → 终面",
    pat="2026 批香港私行暑期岗已核实存在(job 84985412704),是每年复现的固定编制;2027 批 Markets 7/10 开、Banking 8/10 开、Wealth 8/24 开——三批依次相隔约六周",
    note="★★ 8/24 当天刚挂出(job ID 26988478),9/20 复核仍开、10/30 23:59 未变。官方原文:penultimate year、毕业窗口 Dec 2027–June 2028、任何本科专业。⚠️ <b>Citi 亚太限每人最多申 3 个 summer 项目,而香港现在挂着五个前台岗</b>(IBD / Capital Markets / Markets S&amp;T / Private Bank / 本周新发现的 Citigold),必须取舍。注意官方措辞按条线略有差异:Markets 写的是「within the APAC region」,Banking 写「in Asia clusters」,Private Bank 写「in Asia region」——口径都是 3 个。")
add(firm="Citi Private Bank", org="BB", role="★ Wealth – Citigold, Summer Analyst, Hong Kong, 2027",
    func="PB", typ="Summer", loc="香港", url="https://jobs.citi.com/job/hong-kong/wealth-citigold-summer-analyst-hong-kong-2027/287/99664839024", st="open",
    ddl="2026-11-30", ddl_txt="11/30 23:59 — 全 Citi 香港最晚的一个", opened="2026-08-24",
    pay="未公开", dur="10 周暑期项目", lang="英文 + 粤语/普通话对客群有价值", visa="未写",
    gpa="参照同批 Private Bank 岗:任何本科专业、penultimate",
    proc="Plum 测评 → 录播视频面 → 终面",
    pat="与 Private Bank 岗同批(job ID 相邻:26988474 / 26988478),但截止日晚整整一个月",
    note="★ <b>9/20 新收录:Citi 香港 Wealth 条线其实有两个前台暑期岗,本表此前只收了 Private Bank 那个。</b>Citigold 是花旗的富裕客群/财富管理条线(对标恒生的 Retail Banking and Wealth、渣打的 WRB),不是超高净值私行,但同属财富管理前台。<b>关键信息:截止日 11月30日,比 Citi 香港其余四个岗(全部 10/30)晚一个月,是 Citi 香港最后关门的一个</b>——如果 10/30 那批没赶上,这里还有一个月。⚠️ 但它仍然占用「最多 3 个 summer 项目」的额度。")
add(firm="Deutsche Bank Private Bank", org="BB", role="2027 Summer Internship Programme — Private Bank",
    func="PB", typ="Summer", loc="香港", url="https://db.recsolu.com/jobs/eGx9fBLq5cqdYbjz6rj-Pw?job_board_id=DT5zqeU-qZM-ltrVsIvR9Q", st="open",
    ddl="2026-09-30", ddl_txt="9/30 23:45 HKT(滚动审)", opened="2026-08-17",
    pay="未公开", dur="约 9–10 周", lang="英文(中文/粤语加分)",
    visa="★接受香港学生签", gpa="未写",
    proc="DB 站内测评 → 官方明示的录播视频面 → 终面",
    pat="2026 批含 Summer Internship – Private Bank 与 Graduate Programme – Private Bank 两个香港私行岗;2027 批香港 IBCM 与 Private Bank 分两周先后上线",
    note="★★ 8/24 挂出的香港私行岗。官方原文「Applications close on 30 September 2026, 11.45pm HKT」、滚动审;毕业窗口 2027年12月1日–2028年7月31日,相关全职经验 ≤12 个月,接受香港学生签。⚠️ <b>比 Citi 私行早整整一个月截止(9/30 vs 10/30),先做这个——只剩 10 天。</b><br>⚠️ 9/20 说明:这一条本周<b>没能复核到</b>——它的 recsolu 链接本次抓取受限,DB 官方职位板读到的分页切片里也没覆盖到它。<b>没有任何证据说它关了,也没有证据说它还开着</b>,状态按无变化维持。自己点一次链接确认。")
add(firm="BNP Paribas Wealth Management", org="BB", role="2027 APAC Graduate Programme — Wealth Management, Investment Advisory",
    func="PB", typ="Summer", loc="香港", url="https://group.bnpparibas/en/careers/job-offer/2027-apac-graduate-programme-wealth-management-investment-advisory-hong-kong", st="open",
    ddl="", ddl_txt="页面未写截止,滚动收", opened="2026-08-17",
    pay="未公开", dur="毕业生项目,2027年7月入职", lang="英文流利(中文/粤语加分)", visa="视国籍可能有签证限制",
    gpa="★硬线 3.3/4.0", proc="未公开",
    pat="2026 批叫「Wealth Management, Front Office Track」,2027 批拆成 Investment Advisory 与 Investment Services 两条",
    note="⚠️ 8/24 重要更正:「Front Office Track」这个名字 2027 批没有复用,别再等这四个字——对应岗位现在叫 Investment Advisory(multi-asset Investment Counsellor / Advisor 方向),另有一条 Investment Services。⚠️ 这是 2027年7月入职的毕业生项目,面向 2027 届;2028 届 penultimate 要投的是上面那个 Wealth Management 六个月 Long Internship。同样受「只能投一份申请」限制。")
add(firm="Barclays Private Bank", org="BB", role="Private Bank and Wealth Management Summer Internship 2027",
    func="PB", typ="Summer", loc="新加坡(香港无此岗)", url="https://search.jobs.barclays/job/singapore/private-bank-and-wealth-management-summer-internship-programme-2027-singapore/13015/97173677712", st="open",
    ddl="", ddl_txt="Until filled", opened="2026-07-01",
    pay="未公开", dur="10 周", lang="未写", visa="需申报担保需求", gpa="ideally 3.2+",
    proc="网申 → 测评 → 面试 → offer",
    pat="与 Barclays 其他 2027 岗同批 7月1日上线",
    note="⚠️ 香港没有这个岗——Barclays 的亚太私行学生招聘设在新加坡。列出是因为毕业窗口(2027年12月–2028年6月)完全吻合,愿意去 SG 就能投。")
add(firm="Goldman Sachs", org="BB", role="2027 APEJ Private Wealth Management — New Analyst(全职,非实习)",
    func="PB", typ="Summer", loc="香港", url="https://higher.gs.com/campus", st="watch",
    ddl="", ddl_txt="未公布", opened="",
    pay="未公开", dur="全职正式岗", lang="未写", visa="未写", gpa="无 GPA 数字",
    proc="每个招聘年最多投 4 个 business×location 组合,超出会被自动撤回",
    pat="2026 批香港有 PWM Summer Analyst(roles/150643),但 2027 批香港只有 New Analyst 版本",
    note="⚠️ 这是 final year 才能投的全职岗,不是 penultimate 暑期岗。<b>9/20 复核把这件事查死了:2027 批「APEJ | Hong Kong | Wealth Management, PWM | New Analyst」确实存在,但香港<b>没有</b> PWM Summer Analyst——新加坡有(roles/171428)、悉尼有(155417),唯独香港只放了全职 New Analyst。</b>所以 GS 香港私行的学生入口本轮就是只剩 PWMA 学徒计划一条;想要 GS 私行的暑期岗,只能考虑去新加坡。")

add(firm="PWMA 私人财富管理公会", org="EB", role="★ Apprenticeship Programme(全行业私行学徒计划,~45 个名额)",
    func="PB", typ="Summer", loc="香港", url="https://www.pwma.org.hk/en/apprenticeship-programme/about-the-programme/", st="soon",
    ddl="", ddl_txt="预计 11 月开(9/20 四重复核:仍是 2026 届)", opened="",
    pay="★不低于 HK$10,000/月(金管局部分资助)",
    dur="一个暑期(≥8 周)或 连续两个暑期(合计 ≥16 周)",
    lang="PWMA 未硬性规定;成员行实操上要英文 + 普通话/粤语",
    visa="限八大院校在读生", gpa="未设",
    proc="经 PWMA 申请中心投递 → Recruitment Day → 成员行发 offer",
    pat="2026 批:11月1日–12月31日投递(延期后),2月23–27日发 offer。2027 批预计同期",
    note="★★★ 本表最高性价比的一枪:一份申请覆盖 16–18 家成员行,包括 GS、UBS、DB、渣打、DBS、Julius Baer、Pictet、Bank of Singapore、LGT、EFG、BNP、CA Indosuez、中银香港、交银香港、东亚。资格是**大一到大三、任何专业**,八大院校(港大/中大/科大/城大/理大/浸大/岭大/教大)。GS、UBS、渣打、中银香港这些**不公开挂私行学生岗**的机构,这是唯一的学生入口。东亚提供「连续两个暑期」格式,等于提前锁定两年。<br><b>9/20 做了一次四重复核,结论明确:还没开,而且确实还停在 2026 届。</b>① About the Programme 页仍写「offers between 23 and 27 February 2026」、名额「around 45」;② 申请系统 pwma.tal.net 上 2026 届那条(opp 231)明写「This opportunity is closed to applications」;③ <b>tal.net 的历届 opp 编号连续可查——122(2022)、165(2023)、190(2024)、209(2025)、231(2026),不存在任何 2027 条目</b>;④ 官网新闻最新只到 8月10日的 2026 届结业礼,手册 PDF 仍挂在 2025 年的目录下。<b>按历届节奏推断:约 11 月挂出、12月31日截止(2026 届曾因故延期到 12/31)。这是推断不是官方公告——10 月起每周刷,11 月初必须重查一次,这一枪不能漏。</b>")
add(firm="FOAHK 家族办公室协会", org="VC", role="Summer Internship Programme(一份申请覆盖 16+ 家办)",
    func="PB", typ="Summer", loc="香港 / 新加坡", url="https://www.foahk.org/internship", st="soon",
    ddl="", ddl_txt="预计 2027年3月开(上轮 3/17–4/10)", opened="",
    pay="未公开", dur="6月中–8月中(约 8–9 周)", lang="未公开(服务华人 UHNW 的台子实操要中英)",
    visa="全球开放,不限八大院校", gpa="未设",
    proc="统一网申", pat="2026 批 3月17日–4月10日投递,6月29日开营,1300+ 申请、120+ 录取",
    note="★ 进入香港独立财富管理(EAM/MFO)生态的唯一系统性通道,覆盖 Leo Wealth、Carret Private、Raffles Family Office、VMS Group、Wisdom GFO、Topaz Capital 等。资格:大二以上、硕士、或毕业两年内。9/20 复核:实习页仍是 2026 届(申请期 3/17–4/10),按钮显示「Apply Closed」;官网首页新闻最新停在 2025 年,站点整体更新滞后——<b>别把「页面没动」当成「今年不办」</b>。3 月才是窗口,现在不用管,但 2 月底要开始刷。")
add(firm="FOAHK × 港大商学院", org="VC", role="Case Competition — 获奖者直通实习 fast-track",
    func="PB", typ="Offcycle", loc="香港", url="https://www.foahk.org/2026-case-competition", st="soon",
    ddl="", ddl_txt="预计 12 月报名(上轮截 12/15)", opened="",
    pay="奖金至 HK$5,000 + 推荐信", dur="12月–2月两轮,决赛一天",
    lang="英文", visa="全球开放", gpa="未设", proc="3–4 人组队(同地区)",
    pat="2026 届:12月15日 11:59pm HKT 截止报名,2月6日决赛,场地 HKU iCube;9/20 复核页面仍显示「Application Closed」,2027 届未启动",
    note="★ 低成本高杠杆:冠军与一二等奖可获 10+ 家机构的暑期实习 fast-track 面试,点名机构含 国泰海通、ARK Wealth、Fullerton Private Bank、Topaz Capital、LEO Wealth、Carret Private、Wisdom GFO、Raffles Family Office。12月做这件事,是为 2027 暑期铺路。")

add(firm="Hang Seng Bank 恒生", org="CN", role="Summer Seed Programme(10 周)",
    func="PB", typ="Summer", loc="香港", url="https://www.hangseng.com/en-hk/about/careers/internship-opportunities/", st="soon",
    ddl="", ddl_txt="预计 9–12 月开", opened="",
    pay="未公开", dur="10 周(6月–8月底)", lang="中英文",
    visa="★需香港永久居民或有效工作签,比其六个月实习更严", gpa="要求 outstanding academics",
    proc="经 HSBC 招聘系统(apply.careers.hsbc.com)投递",
    pat="2027 批预计 2026年9–12月上线;9/20 复核:实习页文案仍停在「From June to End of August 2025」,HSBC 系统里最后一个 Summer Seed pipeline(259826)已 404",
    note="★ 官方**明确面向 penultimate 年级**,是恒生的暑期分析师等价物、也是其 graduate programme 的 feeder。Retail Banking and Wealth 条线内含私行配置。⚠️ 9/20 仍未开,页面文案陈旧到还写着 2025 年——但同集团的六个月实习(下一条)2027 批确实挂过,说明恒生在走流程,只是 Summer Seed 这条还没轮到。")
add(firm="Hang Seng Bank 恒生", org="CN", role="Student Internship Programme 1H2027 — Retail Banking and Wealth(6 个月)",
    func="PB", typ="Offcycle", loc="香港(中环)", url="https://apply.careers.hsbc.com/job/Central-Student-Internship-Programme-1H2027-Retail-Banking-and-Wealth-Hang-Seng-Bank-(HK)-Hong/1369390457/", st="open",
    ddl="2026-09-11", ddl_txt="9/11 已截止(错过了)", opened="2026-08(约)",
    pay="未公开", dur="六个月全职:2027年1月–6月", lang="中英文,普通话对财富岗有价值",
    visa="需香港永久居民或有效学生签", gpa="未设",
    proc="按条线单独挂 req,建议在 apply.careers.hsbc.com 设岗位提醒",
    pat="每半年一批;1H2027 批约 8 月挂出、9月11日截止——窗口只有几周,比本表预估的「9–11 月挂」早",
    note="⚠️ <b>9/20 的坏消息:这个岗是真的存在、而且就是 2027 批,但截止日是 9月11日——已经过去 9 天了。</b>岗位页现在还挂着 Apply now 按钮,想试可以点一下,但按官方口径应判已关。<br><b>教训记在这:本表此前把它预估成「9–11 月挂」,结果它 8 月就挂出、9 月中就关,窗口只有几周。</b>恒生这条线下一批(2H2027,对应 2027年7–12月)按每半年一批的节奏约在 2027 年 2–3 月,到时别再按「预计」等,直接在 HSBC 招聘系统设提醒。恒生把 Private Banking 明确列为 Retail Banking and Wealth 条线下的配置去向。")
add(firm="南洋商业银行 NCB", org="CN", role="Summer Internship Program(★含明确的 Private Banking 条线)",
    func="PB", typ="Summer", loc="香港(中西区)", url="https://www.ncb.com.hk/nanyang_bank/eng/html/1b3b.html", st="soon",
    ddl="", ddl_txt="预计 2027年1–3月挂;简历常年可投", opened="",
    pay="未公开", dur="7–8月(约 6–8 周)",
    lang="★中英文书面口语均需,普通话流利优先", visa="需香港永久居民或有效学生签",
    gpa="未设", proc="邮件投简历至 hr@ncb.com.hk;八周内回复",
    pat="2026 批已于 7–8 月开营;2027 批预计年初挂出",
    note="★ 中资背景银行里最直接对口的一个:**Private Banking 是官方列明的本科实习配置部门**,且资格写的是大二到大四——正好覆盖 2028 届。申请只需邮件投简历,摩擦极低,现在就可以发速投信。另有 18 个月 RM Trainee(campus_recruit@ncb.com.hk,标题写 Apply Now)是毕业后的去向。<b>9/20 复核:页面仍是 2026 届(实习期写 July 2026 – August 2026,已过)。</b>注意它的投递方式是邮件而不是网申——<b>这意味着 2027 批开放时未必有醒目公告,主动发邮件问一句可能比等页面更新更快。</b>")
add(firm="建设银行(亚洲)CCB Asia", org="CN", role="Summer Internship Program 2027",
    func="PB", typ="Summer", loc="香港", url="https://www.asia.ccb.com/hongkong/aboutus/career_opportunities/graduate_opportunities/internship_programs_at_ccba.html", st="soon",
    ddl="", ddl_txt="预计 1–4 月,4月中截止", opened="",
    pay="未公开", dur="6–8月,至少 8 周",
    lang="★中英文俱佳,明确要求普通话", visa="需香港居留/工作许可",
    gpa="★GPA ≥3.3/4.0", proc="邮件投递 recruithk@asia.ccb.com,标题 Application for CCB (Asia) Summer Internship Program",
    pat="2026 批 4月15日截止;2027 批预计同期。9/20 复核:页面仍是 2026 届(截止「on or before 15 April 2026」,已过)",
    note="⚠️ 资格和时点都吻合(**大三或应届均可**),但实习开放的部门里**没有私人银行**——最接近的是 Consumer Banking。建行亚洲本身有私行业务,建议投 Consumer Banking 并在求职信里写明私行意向。表现优异者可获有条件全职 offer。")
add(firm="招银国际 CMBI", org="CN", role="项目实习生 — 财富管理部(off-cycle)",
    func="PB", typ="Offcycle", loc="香港", url="https://www.cmbi.com.hk/zh-HK/practice", st="open",
    ddl="", ddl_txt="滚动", opened="",
    pay="未公开", dur="通常 3–6 个月", lang="中英文", visa="未写",
    gpa="项目实习生未设(SIP 要求 3.3)", proc="站内投递 + 可速投 graduate@cmbi.com.hk",
    pat="全年滚动,按需挂岗",
    note="★ 绕开 SIP 硕士门槛的本科生路径:筛选器里把 部门 选「财富管理部」、地点选香港。SIP(10周)明确只收待入学或在读硕士 + GPA 3.3,本科生原则上不符。")
add(firm="招商永隆银行", org="CN", role="校园招聘 — 私人银行与财富管理 track(毕业生轨)",
    func="PB", typ="Summer", loc="香港", url="https://recruit.cmbwinglungbank.com/", st="watch",
    ddl="", ddl_txt="预计 2027年2–4月", opened="",
    pay="未公开", dur="毕业生培训生项目(非暑期实习)",
    lang="★精通中英双语,口笔俱佳", visa="未写", gpa="未设",
    proc="公众号「招商永隆微服务」为主要发布渠道",
    pat="2026 批 4月22日截止",
    note="⚠️ 只收应届毕业生,penultimate 不能投。但它是中资行在港最清晰的私行毕业生管道(八个 track 之一就叫「私人银行与财富管理」),值得从大三开始盯公众号。")
add(firm="东亚银行 BEA", org="CN", role="PWMA 学徒(★连续两个暑期格式)+ Group Management Trainee",
    func="PB", typ="Summer", loc="香港", url="https://www.hkbea.com/html/en/bea-career-mt-programme.html", st="soon",
    ddl="", ddl_txt="经 PWMA,预计 11 月", opened="",
    pay="PWMA 口径 ≥HK$10,000/月", dur="连续两个暑期,合计 ≥16 周",
    lang="MT 明确要求 英文 + 粤语 + 普通话 三语流利", visa="限八大院校在读", gpa="未设",
    proc="PWMA 统一申请;MT 流程为 网申 → 视频面 → 能力测试 → 小组 → 终面",
    pat="PWMA 2027 批预计 2026年11月开",
    note="★ 东亚是 PWMA 里仅有的四家提供「连续两个暑期」的机构之一——对 2028 届等于一次申请锁定 2027 与 2028 两个暑假,实质是毕业生管道。投 PWMA 时优先勾它。BEA 本身没有独立的暑期实习项目。")
add(firm="中银香港 BOCHK", org="CN", role="私行学生岗只能走 PWMA(自家 Gen Z 实习无私行条线)",
    func="PB", typ="Summer", loc="香港", url="https://www.pwma.org.hk/en/apprenticeship-programme/about-the-programme/", st="soon",
    ddl="", ddl_txt="经 PWMA,预计 11 月", opened="",
    pay="PWMA 口径 ≥HK$10,000/月", dur="一个暑期", lang="中英文俱佳(明确要求)",
    visa="限八大院校在读", gpa="未设", proc="经 PWMA 申请",
    pat="自家 Gen Z Internship 2026 批 4月17日截止、7月2日–8月21日开营",
    note="⚠️ 核查结论:中银香港自己的 Gen Z 实习**只有 ESG 与金融科技两个条线,没有私行**。想进中银香港私行,PWMA 是唯一学生入口。交通银行(香港)同理,也是 PWMA 一个暑期的成员行。")

add(firm="Julius Baer", org="EB", role="Internship / Graduate Programme(香港为其记账中心)",
    func="PB", typ="Offcycle", loc="全球含香港", url="https://juliusbaer.wd3.myworkdayjobs.com/en-US/External", st="watch",
    ddl="", ddl_txt="招聘通常 3 月底收官", opened="",
    pay="未公开", dur="实习约 10 周(7 月起);Graduate Programme 结构化", lang="英文", visa="未写",
    gpa="未设", proc="未公开",
    pat="目前 Workday 上无香港学生岗;需盯 External 与 Graduate 两个板",
    note="★ 实习资格很宽松:**本硕在读、大二起即可**。Graduate Programme 面向硕士,分 focus 与 flex 两轨。Julius Baer 同时是 PWMA 成员行——走 PWMA 更容易拿到香港席位。<b>9/20 复核:官方实习页明写「Positions will go live at the <b>end of March</b>」——窗口在 3 月底,现在不用刷。</b>Workday 板是 JS 渲染读不到。")
add(firm="Pictet", org="EB", role="Financial Analyst Programme(48 个月,私人银行家培养)",
    func="PB", typ="Summer", loc="香港等办公室", url="https://www.pictet.com/hk/en/careers/financial-analyst-programme", st="watch",
    ddl="", ddl_txt="每年 2–3 月挂,3–5月面,9月入职", opened="",
    pay="未公开(永久合同,支持考 CFA)",
    dur="48 个月(第1年客户关系、第2–3年投资平台、第4年财富顾问)",
    lang="英文流利,额外语言加分", visa="未写", gpa="未设",
    proc="2–3月发布 → 3–5月面试 → 6月反馈 → 9月1日入职,走 SuccessFactors",
    pat="每年 2–3 月固定发布",
    note="⚠️ 这是本表最正统的 RM 培养项目,但**不收 penultimate 本科生**:要求金融/管理硕士,或本科+3–5年经验。是 2028 毕业之后的目标,不是 2027 暑期的目标。Pictet 也是 PWMA 成员行。<b>9/20 复核:此结论未被推翻</b>——香港 Graduate 页时间轴仍是「February-March 2026: Graduate roles are posted」,且面向「最多两年工作经验」的毕业生,<b>香港没有任何面向本科 penultimate 的实习岗</b>。")
add(firm="LGT", org="EB", role="LGT Graduate Programme(18 个月)",
    func="PB", typ="Summer", loc="列支敦士登/瑞士/伦敦/亚洲办公室", url="https://www.lgt.com/hk-en/career/career-opportunities/graduate", st="watch",
    ddl="", ddl_txt="瑞士/列支岗预计 2027年2月挂", opened="",
    pay="未公开", dur="18 个月,下一批 2027年9月入职", lang="英文", visa="未写", gpa="未设",
    proc="未公开", pat="9/20:职位板共 60 个岗位、6 页,可读范围内只有墨尔本/悉尼/布里斯班/伦敦/Bendern/瓦杜兹,香港岗未出现",
    note="目标职能含 Client Relationship Officer 与 Portfolio/Investment Advisor,是真 RM 轨。但要求已完成本科/硕士,属毕业生入口。LGT 同为 PWMA 成员行。⚠️ 9/20 复核:职位板本身能读,但需在站内勾选 Hong Kong 筛选器翻页才能确认香港有没有岗——本环境没能完成这一步,<b>结论是「未证实」而不是「没有」</b>。")
add(firm="Bank of Singapore (OCBC)", org="EB", role="Wealth Management Programme(24 个月 RM 轨)",
    func="PB", typ="Summer", loc="新加坡/香港/迪拜/菲律宾", url="https://www.bankofsingapore.com/careers/students-and-graduates/wealth-management-programme.html", st="watch",
    ddl="", ddl_txt="⚠️ 已开但不收学生:要 3–5 年全职经验", opened="2026-09",
    pay="未公开", dur="24 个月(轮岗 + IBF 认证的私人银行高级证书)",
    lang="英文 + 普通话/粤语加分",
    visa="未写", gpa="★资格硬线:本科以上 + <b>3 到 5 年全职工作经验</b>——在校生不符合",
    proc="未公开",
    pat="官方承诺的「2026年9月启动 2027 批」如期兑现",
    note="⚠️ <b>9/20 重要更正:这一枪对你不适用,本表此前记错了性质。</b>好消息是官方承诺兑现了——页面已改成「Applications for the 2027 Wealth Management Programme are now open and will close on <b>31 December 2026</b>」,地点明确含香港。<b>但报名资格是「three to five years of full-time work experience」——这是经验 hire 的 RM 培养轨,不是学生岗</b>,官方项目总览页也把它归在「Graduates with 3-5 years of full-time work experience」下面。已从「即将开放」降为待观察。<br><b>那学生该看哪条?</b>同一家的两条学生线是:① <b>6-month Semester Internship 1H2027:已开放,10月31日截止</b>(页面只写新加坡办公室);② 10 周的 WEP(Wealth Excellence Programme):仍是「Applications are now closed」,<b>2027 批 11 月启动</b>——这条才是对标暑期实习的,11 月和 PWMA 一起盯。Bank of Singapore 亦为 PWMA 成员行,走 PWMA 也能够到。")
add(firm="渣打银行 Standard Chartered", org="BB", role="Wealth and Retail Banking Graduate / Summer Internship",
    func="PB", typ="Summer", loc="香港", url="https://www.sc.com/en/global-careers/early-careers/local-programmes-for-students/hong-kong-student-opportunities/", st="soon",
    ddl="", ddl_txt="⚠️ Markets 9/1 已开,WRB 仍未跟", opened="",
    pay="未公开", dur="暑期实习 / 两年制 graduate", lang="英文 + 粤语/普通话加分",
    visa="未写", gpa="★官方不设 GPA,strengths-based",
    proc="★pymetrics 游戏化测评(官方确认)→ 单向录播视频面 → 终面",
    pat="历史数据显示香港截止在 12月31日,推断秋季开",
    note="⚠️ 这是 Wealth & Retail(富裕客群),**不是纯私行**;渣打没有独立的私行学生项目。渣打是 PWMA 成员行,想进其私行走 PWMA。<b>9/20 复核:仍未证实 2027 版存在。</b>2026 批那条(req 41715)官方页现在显示「You can't view this job because it's not available at this time」,2027 版全网无痕迹。但本周已证明渣打是<b>分三批上线</b>的(8/17 CIB 三岗、8/27 新加坡 Markets、9/1 香港 Markets),而且<b>2027 批把岗位名全改了</b>——WRB 很可能也会换名字,用旧名搜不到。建议直接去 jobs.standardchartered.com 按 Hong Kong + 2027 筛一遍,别只搜「Wealth and Retail」。")

DATA = R

# ============================================================
# 顶部提醒板块 —— lv: urgent(红) / warn(黄) / info(蓝)
# 每周更新时把过期的删掉、把当前最紧的放最上面
# ============================================================
VERSION = "v1.8"
UPDATED = "2026-09-20"

NOTICES = [
 {"lv":"urgent","title":"未来 10 天是全年最密的一段:七家、十五个岗连续到期",
  "body":"<b>9/27(剩 7 天)· Morgan Stanley 全线 R2 终轮</b>——IBD / IED / FID / GCM / IED Quant Finance 五个岗,过了没有第三轮。<b>9/29(剩 9 天)· JPM 的 Investment Banking</b>——本周发现两处第三方口径都写 9/29 而非 9/30,本表已按早的算,<b>别掐 9/30 交这一份</b>。<b>9/30(剩 10 天)· JPM 其余全线、BofA 四岗、Nomura 三岗(含刚恢复的 International Wealth Management)、DB 的 IBCM 与 Private Bank、以及新收录的 SMBC 新加坡</b>。再往后是 <b>10/2 渣打 Markets、10/4 GS 全线</b>。全部滚动审。"},
 {"lv":"urgent","title":"本周三个新开放,其中两个打乱了原本的时间表",
  "body":"<b>① Wells Fargo 香港提前了三个月。</b>本表一直把它记作「12 月中才开的最后一枪」,结果 Banking(R-571608)与 Markets(R-571605)两个香港岗现在就已挂出,<b>10/30 截止</b>——原来排在 12 月的计划要挪到 10 月。<b>② 渣打的 Financial Markets 其实早就开了,只是改了名字</b>:2027 批叫「<b>Markets Intern</b>」,9/1 上线,用旧名搜永远搜不到;截止日两个口径冲突(镜像写 10/2、官方同批新加坡版写 12/31),<b>按 10/2 准备</b>。<b>③ PJT 香港 2027 Summer Analyst 确认存在</b>,正在「9 月开、10 月关」的窗口里——但 Workday 纯 JS 渲染,本表拿不到直链,请自己去 Students 板筛 Hong Kong。"},
 {"lv":"warn","title":"两个岗招满提前关门,还有一个你已经错过了",
  "body":"<b>HSBC 香港 CIB 四个前台岗关掉了两个</b>——Global Investment Research 与 Infrastructure Finance 页面均已改成「this position has been filled」,<b>比公示的 10/30 整整早了 40 天</b>;只剩 IB 综合岗和 Markets S&amp;T,别再等 10 月底。<b>恒生 Student Internship 1H2027 的截止日是 9/11,已经过去 9 天</b>——它 8 月就挂出、9 月中就关,而本表此前预估它「9–11 月挂」,这次是实打实的漏掉。另外 <b>Bank of Singapore 那个「官方承诺 9 月启动」的 Wealth Management Programme 确实开了,但要求 3–5 年全职经验,不是学生岗</b>,已降级;学生该等的是它 11 月启动的 WEP。<b>11 月还有 PWMA 学徒计划</b>(四重复核确认仍停在 2026 届,tal.net 上没有 2027 条目)——那一枪不能漏。"},
]

# ============================================================
# 更新日志 —— 最新的放最前面
# k: new(新开放) / close(已关闭) / ddl(截止变动) / add(新增收录) / info(信息)
# ============================================================
CHANGELOG = [
 {"date":"2026-09-20","ver":"v1.8","note":"隔了四周的一次核查(中间两周自动更新没跑起来):三个新开放、两个招满提前关、一个已经错过,另新增收录七家机构。",
  "items":[
    {"k":"info","t":"<b>⚠️ 先说一件事:上一次核查是 8月24日,距今 27 天,中间两周的自动更新没有跑起来。</b>页面顶部那个橙色过期警告这段时间一直在显示,所以数据没有假装是新的——但「岗位状态变了」这件事确实空窗了两周,下面有几条本来应该更早发现。已恢复正常节奏。"},
    {"k":"new","t":"<b>★★ Wells Fargo 香港两个岗已开,而且比历年提前了整整三个月。</b>本表一直把它记作「全表开放最晚的 BB,12月中开、1月底关」,当作错过秋季主窗口后的最后一枪——结果 2027 批现在就挂出来了:<b>2027 APAC Banking Summer Analyst – Hong Kong(R-571608)</b> 与 <b>2027 APAC Markets Summer Analyst – Hong Kong(R-571605)</b>,<b>两份独立申请,均 10月30日截止</b>,页面另注「may come down early due to volume」。资格写明 penultimate、毕业窗口 2028年1–6月。<b>如果你原本把 Wells Fargo 排在 12 月的计划里,现在要把它挪到 10 月。</b>"},
    {"k":"new","t":"<b>★★ 渣打的 Financial Markets 香港岗其实早就开了——9月1日,只是改了名字。</b>本表前两周报「FM 未同批上线」是被名字骗了:<b>渣打 2027 批把岗位名全改了</b>,「Financial Markets Internship Programme」→「<b>Markets Intern</b>」,「Client Coverage」→「Coverage Banking」。业务线原文仍是「Financial Markets within Corporate &amp; Investment Banking」,分 Sales / Trading / Structuring / Financing Risk / Research / RMAP-XVA 六个方向,10 周、2027年6月起、明确要 penultimate。<b>⚠️ 截止日两个口径冲突:校招镜像写 10月2日,渣打官方同项目新加坡版(req 61050)写 12/31。本表按早的 10/2 记,请按 10/2 准备。</b>⚠️ 渣打「六个月内只能投一份」仍然有效——现在是 Global Banking / Coverage Banking / Markets 三选一。"},
    {"k":"new","t":"<b>★★ PJT Partners 香港 2027 Summer Analyst 确认存在,正在窗口里。</b>岗位全名「2027 Summer Analyst (Strategic Advisory &amp; Restructuring) Hong Kong」,覆盖 Strategic Advisory / Restructuring &amp; Special Situations / Private Capital Solutions,要求英文流利 + 至少一门亚洲语言,毕业窗口 Winter 2027–Summer 2028。官方 Students 页口径仍是「9 月开、10 月关」——<b>窗口可能只有两三周</b>。⚠️ 本表拿不到可用直链、也不编造:PJT 用 Workday 纯 JS 渲染(已用另一个 PJT 职位页做过对照实测),香港这条的 req 号未被搜索引擎收录。<b>请自己打开 Workday Students 板按 Hong Kong 筛。</b>"},
    {"k":"close","t":"<b>❌ HSBC 香港招满提前关了两个岗,比公示截止日早 40 天。</b><b>Global Investment Research Internship 2027</b> 与 <b>Investment Banking – Infrastructure Finance Internship 2027</b> 的官方页现在都显示「Sorry, this position has been filled.」——而它们公示的截止日是 10月30日。这正是 HSBC posting 里那句「may close applications before the advertised date once all vacancies are filled」的实际后果。<b>HSBC 香港 CIB 四个前台岗现在只剩 Investment Banking 综合岗与 Markets S&amp;T 两个,9/20 实测仍开,但 10/30 这个日期已经被证明不可靠。</b>另外:本表此前说「全港 2027 批真正的股票研究实习只有三个」,现在少了一个。"},
    {"k":"close","t":"<b>❌ 你已经错过了一个:恒生 Student Internship Programme 1H2027(Retail Banking and Wealth)截止日是 9月11日,已经过去 9 天。</b>这个岗是真实存在的 2027 批(2027年1–6月,六个月全职,中环),页面现在还挂着 Apply now 按钮,想试可以点一下,但按官方口径应判已关。<b>本表此前把它预估成「9–11 月挂」,结果它 8 月就挂出、9 月中就关,窗口只有几周——这是本次空窗两周造成的实际损失,记在这里。</b>下一批(2H2027)按每半年一批约在 2027 年 2–3 月,到时直接在 HSBC 招聘系统设岗位提醒,别再按「预计」等。"},
    {"k":"close","t":"<b>另外两个下掉的:</b>① <b>Millennium 的 Off-Cycle Trading Intern – Quantitative Researcher 已下架</b>,原链接返回 404,且 career.mlp.com 香港现有 10 个岗位里没有任何实习岗(全是正式岗)——两条证据一致。校园批不受影响,仍是 11 个岗在挂。② <b>GS 的 Off-Cycle GIR(Industrial Tech,roles/171082)降为待观察</b>:页面返回空 body,<b>本次做了对照实验</b>——已知过期的 roles/150841 同样返回空 body,而在挂的 169893/170773 返回完整正文,所以「空页」=下架而非 JS 问题;另外它的标题其实写的是 <b>2026</b> 批,本来就不是 2027 的岗。"},
    {"k":"new","t":"<b>★ 两个「待观察」本周翻案,恢复可投:</b>① <b>Nomura 香港 International Wealth Management 2027 确认存在且在收</b>——上次是因为官方板全站人机验证才降级的,这次官方板没拦截,直读到原文:<b>opp 1474,「Please apply before 11:55pm, Wednesday 30 September 2026 (HKT)」</b>,而且官方明说会在截止前就安排面试。② <b>Citadel International Equities Intern (Asia) 的「疑似下架」没有复现</b>:页面正常渲染且带完整申请表单,地点 Hong Kong + Singapore。"},
    {"k":"ddl","t":"<b>三处截止日变动,都值得单独看一眼:</b>① <b>Citi Markets S&amp;T 香港从「无截止日」变成明确的 10/30 23:59 HKT</b>——至此 Citi 香港 Banking / Markets / Private Bank 四个岗截止日统一为 10/30。② <b>JPM 的 Investment Banking 可能是 9/29 而不是 9/30</b>:两处独立的第三方汇总都把 IB 一条列为 9月29日,而 Markets / AM / 两个私行岗才是 9/30;JPM 的 Oracle 页正文要 JS 渲染证实不了,<b>本表已按早的 9/29 记,别掐 9/30 交这一份</b>。③ <b>Jane Street 香港 S&amp;T 岗的 job ID 变了</b>(现为 position 8630687002),卡片链接已更新,页面写明目标毕业年份 2028;QR 与 QT 仍然关着。"},
    {"k":"add","t":"<b>★ 新增收录七家,其中两条是「藏在非直觉目录」的新教训:</b>① <b>Susquehanna (SIG) 香港 Equity Analyst Internship Summer 2027</b>——<b>这个股票研究岗挂在 quantitative-trading 目录下,不在 research 目录里</b>,和 JPM 把研究岗挂在 Markets 下是同一类坑(⚠️ 页面未写学位层级,本科是否符合未证实);② <b>Crédit Agricole CIB 香港</b>——<b>法资行在港把前台学生岗一律叫「Trainee」+「one year contract」,用 internship / summer analyst 搜永远搜不到</b>,现有 14 个在招岗里前台占六个(⚠️ 但批次对 2028 届错配,多要求 2027 年前毕业,先记为待观察,真正该等的是它的 10 周暑期项目)。"},
    {"k":"add","t":"<b>其余五家新收录:</b>③ <b>IMC Trading 香港 Quantitative Trader Intern 2027</b>——资格原文明写「已进入 penultimate year」,是少见的把你这届写得毫不含糊的岗;④ <b>PIMCO 香港 2027 Summer Internship, Account Analyst</b>——毕业窗口 Dec 2027–June 2028 精准命中(⚠️ 官方 Workday 直链未能证实,卡片给的是官方学生实习入口页);⑤ <b>Houlihan Lokey 香港 Summer Financial Analyst 2027 – Financial Restructuring(R3488)</b>,HL 香港第一次出现正式暑期岗而不只是 off-cycle;⑥ <b>Citi Wealth – Citigold Summer Analyst 香港 2027</b>,<b>截止 11月30日,是 Citi 香港最后关门的一个</b>;⑦ <b>SMBC Summer Intern Programme 2027</b>——破例收的新加坡岗,因为资格写「四年制本科第三年、2028 年毕业」逐字吻合,而且 <b>9/30 截止</b>(已确认 SMBC 香港分行没有对应学生项目)。另收录 <b>HKMA 金管局 Winter Internship</b> 为线索级待观察。"},
    {"k":"new","t":"<b>★ Blackstone 香港那个跟了一个多月的岗坐实了:确实改名叫「Transaction Finance」。</b><b>2027 Transaction Finance Off-cycle Intern (January to June), Hong Kong,req 44171</b>,即历年的 Business Finance 六个月 off-cycle。上周还只是未证实线索,本周聚合站(当日更新)列出的 Blackstone 香港唯一岗位就是它。⚠️ Workday JS 渲染读不到截止日,投前自己打开确认。反向的一条:<b>同板的 2027 Real Estate Summer Analyst(req 40595)倾向已下架</b>——聚合站在挂列表里亚洲只剩东京两个和新加坡一个,但证据不足以断言,投前务必自己看。"},
    {"k":"info","t":"<b>复核未变、但有细节值得知道的:</b><b>GS 官方 APAC 项目页原文确认 10月4日统一截止未变</b>,其中 FICC/Equities S&amp;T(169893)与 Capital Solutions Group(170773)两条直读官方页、Apply 有效;<b>⚠️ 但 IB Classic(170772)本周抓取受限读不到,而且两个第三方在招列表里都没有它</b>(其余 GS 香港岗都在列)——本表没有证据判它关闭、状态维持已开,<b>但这是本周风险最高的一条,优先自己核一次</b>。<b>MS 的 9/27 R2 已从两个官方页逐字证实</b>(IED 21266、IED Quant 21270),<b>唯独 FID(21318)读不到、是五个里唯一的盲点</b>。<b>BofA 四个岗全部官方页直读,「Apply by Sep 30, 2026」一字未动。</b><b>DB IBCM 官方 req 页直读确认 9/30 11:45pm HKT</b>;<b>DB Private Bank 香港本周完全没能复核到</b>(链接抓取受限、官方板分页没覆盖),无证据说开也无证据说关,状态按无变化维持。"},
    {"k":"info","t":"<b>仍未开放的,以及本周查到的确切结论:</b><b>PWMA 学徒计划做了四重复核,确认仍停在 2026 届</b>——页面仍写「offers between 23 and 27 February 2026」、申请系统上 2026 届那条明标 closed、<b>tal.net 历届编号 122/165/190/209/231 连续可查但不存在 2027 条目</b>、官网新闻最新只到 8月10日的结业礼。按历届节奏推断 11 月挂出、12月31日截止,<b>11 月初必须重查</b>。<b>Bank of Singapore 的官方承诺兑现了但性质记错了</b>:2027 WMP 确实已开、12/31 截止、含香港,<b>但要求 3–5 年全职工作经验,是经验 hire 不是学生岗</b>,已降为待观察;学生线是 6-month Semester Internship 1H2027(10/31 截止,只写新加坡)与 <b>11 月启动的 10 周 WEP</b>。<b>Rothschild 香港连续三周无进展</b>——2027 登记页找回来了但地点只写 Manchester。<b>CITIC CLSA</b>(2026 批已于去年 12/30 下架,无 2027 条目)、<b>CMBI SIP</b>(时间轴一字未动,仍写 2026 届,10 月中是窗口)、<b>FOAHK 两条</b>、<b>恒生 Summer Seed</b>(文案还停在 2025 年)、<b>Mizuho</b>(索引里全是 2026 批)、<b>Eclipse</b>(2027 批只有悉尼的 Graduate Trader)、<b>Moelis</b>(七类岗全在美国)、<b>BDA</b>(七个地点含香港全部 Closed,intake 只到 2026 Q4)均未开。"},
    {"k":"info","t":"<b>本周的核查限制,照例说明,免得你把「没查到」当成「没有」:</b>Workday 系(PJT / Blackstone / Houlihan Lokey / Moelis / Mizuho / CITIC CLSA / Julius Baer)全部纯 JS 渲染,只能拿到 meta 标签;中资券商 CICC / GTJAI / BOCI 的招聘板同样 JS 动态加载或走抓不到的外部平台;<b>海通国际、华泰国际、招商证券国际三家本周完全没核到</b>(搜索配额耗尽)。这些标「未发现 2027 岗」的都是索引层面的结论。另外三条需要你手动确认:<b>渣打 Coverage Banking(59110)</b>全网无 2027 痕迹但同批 59126 仍在、<b>渣打 WRB 香港 2027</b>(注意它很可能也换了名字,别只搜旧名)、<b>Citi 香港 Corporate Banking 2027</b>(官方 IB 分类页只列 IBD 与 Capital Markets,只找到新加坡版)。"},
  ]},
 {"date":"2026-08-24","ver":"v1.7","note":"上线以来变化最大的一周:GS IBD Classic、渣打、BNP、DB 私行、Citi 私行同期开闸,另有三条资格更正。",
  "items":[
    {"k":"new","t":"<b>★★ Goldman Sachs 香港 IBD Classic 2027 已挂出</b>——roles/170772,页面标题「2027 | APEJ | Hong Kong | Investment Banking, Classic | Summer Analyst」,Apply 按钮实测有效,统一 <b>10/4</b> 截止。这是 7月1日第一批之后晚了约七周才补挂的岗,等它的人现在可以投了。⚠️ 与 Capital Solutions Group(170773)是两份独立申请,各占 GS「每 cycle 最多 4 个 business×location」额度里的一个。"},
    {"k":"new","t":"<b>★★ 渣打香港 2027 已于 8/17 上线,但只上了 CIB 三岗</b>:<b>Global Banking Intern</b>(job 59126)、<b>Coverage Banking Intern</b>(job 59110,内含 M&A 组——想做 M&A 走这个入口)、Transaction Services Intern(job 59114,交易银行,不入主表)。10 周、2027年6月起,评估中心 <b>2026年10月</b> 就开始。⚠️ 两个硬约束:官方原文要求「permanent legal right to work in Hong Kong」(<b>学生签不符合</b>,非本地生慎投),以及<b>六个月内只能投一份申请</b>——三个岗只能三选一。<b>Financial Markets 与 Wealth &amp; Retail 未同批上线</b>,官方 sitemap 里 23 条 2027 岗位中没有这两条,是分批不是取消。"},
    {"k":"new","t":"<b>★★ BNP Paribas 香港 2027 批 8/17 批量上线</b>(上周查不到是因为当天稍晚才上,职位页 last update 正是 8/17)。前台相关的六个月 Long Internship(2027年1–6月)三个:<b>Global Banking APAC</b>(含 M&A/ECM/DCM/Coverage)、<b>Global Markets</b>、<b>Wealth Management</b>。页面均<b>未写截止日</b>,滚动收,尽快投。⚠️ 官方原文「Candidates with more than one application will not be processed」——<b>全集团只让投一份</b>,跨条线跨地点都算,投多份直接不处理。"},
    {"k":"new","t":"<b>★★ 私行本周连开两枪。① Deutsche Bank 香港 Private Bank 2027</b>——上周还只有新加坡,现在香港岗已挂(官方 Yello 板),<b>9/30 23:45 HKT</b> 截止、滚动审,毕业窗口 2027/12/1–2028/7/31,接受香港学生签。<b>② Citi 香港 Wealth – Private Bank Summer Analyst 2027</b>——job ID 26988478,<b>posting date 就是 8/24 当天</b>,搜索引擎还没索引到,<b>10/30 23:59</b> 截止,10 周、任何本科专业、毕业窗口 Dec 2027–June 2028。⚠️ Citi 亚太限每人最多申 3 个 summer 项目,香港现在有 IBD / Capital Markets / Markets S&amp;T / Private Bank 四个前台岗在挂,必须取舍。"},
    {"k":"add","t":"补收三个此前漏掉的岗:<b>Morgan Stanley 香港 IED Quantitative Finance</b>(opp 21270,第五个 MS 香港岗,R2 9/27,官方原文本科 penultimate 明确可投,与普通 IED 21266 是两份独立申请);<b>BofA 香港 Global Corporate Banking Summer Analyst</b>(14384,9/30,BofA 香港的第四个前台岗);渣打 <b>Coverage Banking</b>(见上)。"},
    {"k":"info","t":"<b>⚠️ 更正一:Barclays 香港的 Electronic Trading Associate 与 Quantitative Analytics Associate 两个岗限 postgraduate</b>——posting 原文的毕业窗口是 2027年12月–2028年6月且明写 postgraduate,<b>2028 届本科 penultimate 不符合资格</b>。本表此前写「这里的 Associate 是项目名称不是层级」是误读,已更正。本科生做量化方向,银行侧应投主 S&amp;T 项目(Sales, Trading and Structuring)。"},
    {"k":"info","t":"<b>⚠️ 更正二:BNP 的「Wealth Management Front Office Track」这个名字 2027 批没有复用</b>,别再等这几个字。对应岗位现在拆成 <b>Investment Advisory</b>(最接近原 front office track)与 Investment Services 两条,GPA <b>3.3/4.0</b> 硬线。而且这是 <b>2027年7月入职的毕业生项目</b>,面向 2027 届;2028 届 penultimate 该投的是上面那个 Wealth Management 六个月 Long Internship。"},
    {"k":"close","t":"<b>⚠️ 更正三:UBS 这条线基本关完了。</b>暑期三岗 8/6 硬截止已过;香港 Global Research off-cycle(jobid 348319)与新加坡 Global Markets off-cycle(348322)实测均返回「posting has expired」;<b>GWM Solutions 香港 off-cycle 在 jobs.ubs.com 官方职位库搜不到</b>,只剩 LinkedIn / ExpatJobBoard 等第三方聚合站还挂着页面——三个 UBS off-cycle 岗全部降为待观察。"},
    {"k":"close","t":"<b>Nomura 香港 International Wealth Management 降为待观察。</b>IB 与 Global Markets 两个香港岗都能在多所大学 career center 的官方转载里找到 2027 版原文(<b>9/30 11:55pm HKT</b>),唯独 IWM 香港只搜得到 2025/2026 版本,没有 2027 版;官方职位板 nomuracampus.tal.net 全站被人机验证拦住,五种 URL 形态都读不到。按本表纪律降级,不等于下线——想投的自己过一次 CAPTCHA 确认。"},
    {"k":"info","t":"<b>Jefferies 香港本周无法复核。</b>LinkedIn 被 robots.txt 禁抓、Jefferies 的 tal.net 板全站 CAPTCHA,两条路都读不到正文。间接信号:tal.net 上 Jefferies 2027 IB SA 的美国岗都已被索引,<b>唯独香港 2027 没有任何 tal.net URL 被索引</b>。状态暂维持已开(上周有实证),但请自己开浏览器确认。"},
    {"k":"info","t":"<b>Rothschild 香港这周不进反退</b>:官方 opportunities 页这次完整渲染出 44 个在挂岗位(不是 JS 挡住),18 个 2027 岗全在欧洲,而且<b>上周还在的 2027 登记页条目现在也不见了</b>。<b>PJT</b> 官方 Students 页明写「9 月开、10 月关」,下周起进入窗口,但已索引的 2027 Summer Analyst 全是美国岗。<b>Blackstone 香港六个月 off-cycle 可能改名叫「Transaction Finance」</b>(第三方聚合站列为在挂,Workday JS 渲染无法证实,不给伪造链接——自己去 Campus Careers 搜「Transaction Finance」)。"},
    {"k":"info","t":"截止日复核全部未变:<b>GS 10/4、MS R2 9/27、JPM 9/30、BofA 9/30、HSBC 10/30、Citi Banking &amp; Markets 10/30、Temasek 9/11</b>。<b>Jane Street 香港 S&amp;T 岗仍开着</b>(Greenhouse 申请表可用,无公示截止,随时会关)。<b>Millennium 香港在挂数由 10 增至 11</b>,无关闭迹象,最多投 2 份。其余未开:<b>Bank of Singapore</b>(官网「Applications are now closed」+ 明示 2026年9月启动 2027 批,全表唯一有官方时点承诺的)、PWMA(官网仍是 2026 届,预计 11 月)、CMBI SIP(时间轴仍停在上一届)、CITIC CLSA、恒生 Summer Seed(页面文案仍是 2025)、FOAHK(Apply Closed)、Schroders(FAQ 口径 9 月)、Eclipse(最新实习仍是 2026 批)、Wells Fargo(旧岗已 404,预计 12 月中)。"},
  ]},
 {"date":"2026-08-17","ver":"v1.6","note":"每周核查:DB 香港 IBD 开闸、Jefferies 香港现身,MS 切入 R2。",
  "items":[
    {"k":"new","t":"<b>Deutsche Bank 香港 IBD 2027 已开</b>——官方原文「Applications close on 30 September 2026, 11.45pm HKT」、滚动审;毕业窗口 2027年12月1日–2028年7月31日,相关全职经验 ≤12 个月,明确接受香港学生签。申请走 db.recsolu 链接(卡片内直达)。同批新加坡已挂 Private Bank、固收等多岗,<b>香港私行岗未见但大概率临近</b>,盯 careers.db.com。"},
    {"k":"new","t":"<b>Jefferies 香港 2027 Investment Banking Summer Analyst 已在官方 LinkedIn 挂出</b>——8/3 查证还查无此岗,本周现身,比历年 6–7 月的节奏晚约一个月。未写截止、GPA 3.4 硬线(全表最高)、仅限 penultimate。官方 tal.net 板索引尚未同步,从 LinkedIn 岗位页或官网 students 页进。"},
    {"k":"ddl","t":"<b>Morgan Stanley R1 8/16 已截止,现在走 R2 9/27(终轮)</b>——官方原文两轮日期核验未变(23:55 HKT),四个口(IBD/IED/FID/GCM)均适用;IBD 卡片倒计时已切到 9/27。官方同时写明滚动审,R2 别掐点交。"},
    {"k":"info","t":"<b>渣打官方口径的「8 月中旬」已到,8/17 实测香港 2027 仍未挂</b>(early careers 页文案未变、职位库无香港条目);<b>BNP 的「8 月开申」同样未兑现</b>,只剩两周窗口——这两家继续每天刷。"},
    {"k":"info","t":"其余按兵不动:Citi Wealth/私行、GS IBD Classic、Rothschild 香港(已开 2027 登记页,可先登记)、PJT(官方 9 月窗口临近)、Blackstone 香港 Business Finance off-cycle、恒生 Summer Seed、Schroders(9月)、Bank of Singapore(9月启动)、PWMA(11月)均未开;Temasek 9/11、Nomura/JPM/BofA/HSBC 截止未变;Lazard 香港板最新仍是 2022 批,无新岗。"},
  ]},
 {"date":"2026-08-10","ver":"v1.5","note":"每周核查:Citi Banking 与 Nomura 开闸,渣打/BNP 官方坐实 8 月,UBS 关窗。",
  "items":[
    {"k":"new","t":"<b>Citi 香港 Banking 2027 已开</b>——Investment Banking、Capital Markets、Corporate Banking 三岗同批挂出,<b>10/30 截止、滚动审</b>。⚠️ 官方口径 APAC 每人最多申 3 个 summer 项目,和 Markets 怎么组合要提前想好。Wealth/私行岗仍未开(历年晚于 Banking)。"},
    {"k":"new","t":"<b>Nomura 香港 2027 三岗已开</b>——Investment Banking、Global Markets、<b>International Wealth Management(私行条线)</b>,均 9/30 截止。公开挂牌的私行暑期岗从 JPM 一家变两家。单岗深链未被索引,从官方职位板进。"},
    {"k":"new","t":"<b>Temasek 2027 暑期批 Investment Group(新加坡)已开</b>,9/11 截止、滚动审——和 GIC 同窗口,接受去 SG 的抓紧。"},
    {"k":"ddl","t":"<b>GS 官方 APAC 项目页确认:2027 暑期批统一 10月4日截止</b>(此前记 until filled)——香港四个在挂岗全部补上硬日期;IBD Classic 仍未挂出。"},
    {"k":"ddl","t":"<b>Jane Street S&amp;T 岗:原记「约 8/15」改为无官方截止</b>——8/10 实测 Greenhouse 申请通道仍开、页面不写日期,链接已换成可直投的 Greenhouse 页。按 QR/QT 说关就关的前科,尽快投。"},
    {"k":"close","t":"<b>UBS 香港三岗(GB/GM/AM)8/6 硬截止已过</b>,未见延期公告,从可投列表下掉。"},
    {"k":"info","t":"<b>渣打官方明示香港「8 月中旬上线」</b>、<b>BNP 官方 FAQ 写明 8 月开申</b>(含六个月 APAC Internship 与 WM Front Office Track)——这两家进入每天刷的窗口。"},
    {"k":"add","t":"新增收录三家:<b>Schonfeld 2027 暑期登记池</b>(含香港,多策略对冲基金,先登记占位);<b>Mizuho 瑞穗</b>(在港有 ECM/债券承销/股票三个前台暑期分岗,2027 批预计年底开);<b>Schroders 施罗德</b>(官方明示 penultimate、9 月开申)。"},
    {"k":"info","t":"其余按兵不动:DB、PJT(9月)、Rothschild(美国已挂、香港未跟)、Jefferies、CITIC CLSA、CMBI SIP、PWMA(11月)、恒生、Bank of Singapore(9月启动)、FOAHK、Wells Fargo(12月)均未开;Millennium 香港 10 岗全部在挂未变;MS R1 8/16 复核未变;Blackstone 香港 Business Finance off-cycle 未挂,但同系列新加坡 2027 off-cycle 已开,临近;Eclipse 挂出 Graduate Trader 2027(全职),intern 批未开。"},
  ]},
 {"date":"2026-08-03","ver":"v1.4","note":"每周核查:Millennium 开闸、UBS 多出一个岗、Jane Street 两岗提前关。",
  "items":[
    {"k":"new","t":"<b>Millennium 2027 批今天(8/3)如期开放</b>,香港一次上线 10 个岗:前台相关有 Quantitative Researcher、Quantitative Developer、Applied AI Engineer、Execution Trading、Sector Specialist、Corporate Access。滚动补位、无硬截止、<b>最多投 2 份</b>——今天就投。"},
    {"k":"new","t":"<b>UBS 香港 2027 Asset Management 暑期岗</b>(jobid 348591)——此前漏收的新发现,约 7 月中旬挂出,与 GB/GM 同批,<b>大概率同为 8/6 硬截止,按 8/6 对待</b>。"},
    {"k":"new","t":"<b>Blackstone 2027 Real Estate Summer Analyst(上海/香港)</b>已挂出——Blackstone 香港 2027 校招板的第一个前台岗;Business Finance 六个月 off-cycle 仍未挂,进入高频观察期。"},
    {"k":"new","t":"<b>GIC 实习(新加坡,12 周)申请通道已开</b>,滚动审、鼓励早投;页面未标批次年份,投前自行确认是 2027 暑期批。"},
    {"k":"close","t":"<b>Jane Street 香港 QR 暑期岗已提前关闭</b>——官网已挂「不再接受申请」,比原记的 8/18 早了两周以上;QT 岗 7/30 关闭亦获官网确认。<b>S&amp;T 岗(约 8/15)是 Jane Street 香港唯一还开的暑期岗,立即投。</b>"},
    {"k":"close","t":"<b>Citadel International Equities Intern (Asia) 疑似已下架</b>——7/25 上线、一周即从站内列表消失,改回待观察;还想投的先亲测原链接。"},
    {"k":"info","t":"<b>Jefferies 香港 2027 查证</b>:全网找不到香港 2027 req(现挂 2027 全在美洲,香港 2026 批已关),此前标「已开放」应属误判,改回待观察。"},
    {"k":"add","t":"新增收录 <b>Wells Fargo APAC Banking / Markets Summer Analyst</b>(香港)——全表开放周期最晚的 BB,上一批 12月中开、1月底关;错过秋季主窗口 12 月还有这一枪。"},
    {"k":"info","t":"其余「即将开放」均未提前开闸,节奏照旧:Citi Banking/Wealth(Markets 已开一个月,Banking 按规律 8–9 月)、DB(官网已切 2027 文案,临近)、Nomura、渣打(预计 9 月)、BNP、PJT、Rothschild(欧美 2027 已挂、香港未跟)、PWMA、CITIC CLSA、CMBI SIP、恒生、FOAHK 均未开;<b>Bank of Singapore 官网坐实 9 月启动 2027 批</b>;MS R1 8/16、UBS 8/6 均核验未变。"},
  ]},
 {"date":"2026-07-30","ver":"v1.3","note":"倒计时改为实时计算。",
  "items":[
    {"k":"info","t":"<b>倒计时现在每天自己变</b>——按你打开页面当天实时算,不再依赖每周重建。截止日一过,该岗位会自动标成「已截止」、沉到列表底部、并从「现在可投」的计数里剔除。"},
    {"k":"info","t":"新增数据新鲜度提示:顶部会显示距上次核查多少天;超过 10 天会自动弹出橙色警告,提醒自动更新可能没跑起来,别把过时数据当最新的用。"},
    {"k":"info","t":"筛选器新增「已截止」一档,想回看已经关掉的岗位可以单独筛。"},
  ]},
 {"date":"2026-07-30","ver":"v1.2","note":"应朋友要求补齐私行条线,并加上这个更新板块。",
  "items":[
    {"k":"add","t":"新增<b>「私行 / 财富管理」</b>条线,收录 24 个岗位,筛选器里可单独筛。"},
    {"k":"new","t":"JPM Private Bank 香港两个 2027 暑期岗确认在挂:<b>Advisor Program</b>(RM 轨)与 <b>Investment Solutions Program</b>(投研轨),均 9/30 截止、HireVue 必做、两份独立申请。"},
    {"k":"info","t":"收录 <b>PWMA 学徒计划</b>——GS、UBS、渣打、中银香港等不公开挂学生岗的机构,这是唯一学生入口。大一到大三任何专业,预计 11 月开放。"},
    {"k":"info","t":"收录 <b>东亚银行「连续两个暑期」</b>格式(PWMA 里仅四家有),对 2028 届等于一次申请锁定两个暑假。"},
    {"k":"info","t":"泼冷水的核查结论:UBS 香港<b>没有</b> GWM 暑期岗(流传的是美国岗且已过期);HSBC Global Private Banking <b>不在</b>其 7/6 放出的香港套装里;Barclays 私行在<b>新加坡</b>不在香港;Pictet 那个 48 个月私人银行家项目<b>不收本科生</b>。"},
  ]},
 {"date":"2026-07-30","ver":"v1.1","note":"补齐前台非 IBD 条线。",
  "items":[
    {"k":"add","t":"补上一批只搜 IBD 会漏掉的前台岗:BofA <b>GCM</b>(14375)、MS <b>GCM</b>(21294)、GS <b>CSG</b>、Barclays <b>Electronic Trading</b> 与 <b>量化 off-cycle</b>、HSBC <b>Infrastructure Finance</b>。"},
    {"k":"add","t":"股票研究条线单列。全港 2027 批只有三个:GS GIR、JPM Markets-Research(挂在 Markets 目录下)、HSBC GIR。"},
    {"k":"info","t":"逐家核对了 12 家大行 posting 原文的 GPA 门槛。写死数字的只有 <b>Jefferies 3.4</b>、<b>BNP 3.3</b>、<b>招银国际 SIP 3.3</b>;Barclays 是「ideally 3.2」的软措辞;其余不写数字也不在申请阶段强制传成绩单。"},
  ]},
 {"date":"2026-07-30","ver":"v1.0","note":"上线。",
  "items":[
    {"k":"add","t":"首版收录香港前台 2027 Summer 与 Off-cycle 岗位,含薪资、时长、语言与签证要求、GPA 门槛原文、网申测评与面试流程、历年开放规律。"},
    {"k":"info","t":"<b>Citi 的规律是 Markets 先开、Banking 晚 1–3 个月</b>——7/10 Markets 已开、IBD 未挂,不要读成错过了。"},
  ]},
]

FUNC_LABEL = {"IBD":"IBD / M&A","ECM":"ECM·DCM·结构融资","S&T":"Sales & Trading","RES":"股票研究",
              "PB":"私行 / 财富管理","BUY":"买方投资(PE/VC/HF/AM)","QUANT":"量化 / Prop"}
CL_LABEL = {"new":("新开放","gr"),"close":("已关闭","gy"),"ddl":("截止变动","rd"),
            "add":("新增收录","ac"),"info":("信息","am")}
ORG_LABEL = {"BB":"外资投行","EB":"精品行 / 独立顾问","CN":"中资在港","BUY":"买方机构","QUANT":"量化 / Prop","VC":"VC / Crypto"}
ST_LABEL  = {"open":"已开放","soon":"即将开放","watch":"待观察","exp":"已截止"}

html = io.StringIO()
html.write("""<!DOCTYPE html>
<html lang="zh-HK"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>HK 前台求职追踪 · 2027 Summer & Off-cycle</title>
<style>
:root{--bg:#0d0f14;--card:#151920;--card2:#1b2029;--bd:#282e3a;--tx:#e9ecf2;--mu:#98a2b3;
--ac:#5b8def;--gr:#3fb27f;--grb:rgba(63,178,127,.13);--am:#e0a83e;--amb:rgba(224,168,62,.13);
--gy:#7d879b;--gyb:rgba(125,135,155,.13);--rd:#e8695f;--rdb:rgba(232,105,95,.13)}
@media(prefers-color-scheme:light){:root{--bg:#f5f6f8;--card:#fff;--card2:#f0f2f5;--bd:#dfe3ea;--tx:#151a22;--mu:#5b6472;
--ac:#2a60cc;--gr:#18845a;--grb:rgba(24,132,90,.1);--am:#a2740f;--amb:rgba(162,116,15,.1);
--gy:#68717f;--gyb:rgba(104,113,127,.1);--rd:#b8443a;--rdb:rgba(184,68,58,.09)}}
*{box-sizing:border-box}
body{margin:0;padding:22px 16px 70px;background:var(--bg);color:var(--tx);
font:14px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif}
.w{max-width:1180px;margin:0 auto}
h1{font-size:23px;margin:0 0 5px;letter-spacing:-.2px}
.sub{color:var(--mu);font-size:13px;margin-bottom:18px}
.kpis{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px}
.kpi{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:11px 16px;flex:1;min-width:132px}
.kpi b{display:block;font-size:23px;line-height:1.15}.kpi span{color:var(--mu);font-size:11.5px}
.kpi.g b{color:var(--gr)}.kpi.a b{color:var(--am)}.kpi.r b{color:var(--rd)}
.alert{background:var(--rdb);border:1px solid var(--rd);border-radius:10px;padding:12px 15px;margin:0 0 12px;font-size:13.2px}
.alert.am{background:var(--amb);border-color:var(--am)}
.alert b{font-weight:700}
.bar{background:var(--card);border:1px solid var(--bd);border-radius:11px;padding:12px 14px;margin-bottom:14px;
position:sticky;top:0;z-index:20;backdrop-filter:blur(8px)}
.bar .row{display:flex;gap:7px;flex-wrap:wrap;align-items:center;margin-bottom:8px}
.bar .row:last-child{margin-bottom:0}
.lbl{color:var(--mu);font-size:11px;font-weight:700;letter-spacing:.4px;min-width:40px}
.f{padding:5px 11px;border-radius:20px;border:1px solid var(--bd);background:transparent;color:var(--mu);
font-size:12.2px;cursor:pointer;font-family:inherit;transition:.12s;white-space:nowrap}
.f:hover{border-color:var(--ac);color:var(--tx)}
.f.on{background:var(--ac);border-color:var(--ac);color:#fff;font-weight:600}
#q{flex:1;min-width:170px;padding:6px 12px;border-radius:8px;border:1px solid var(--bd);
background:var(--bg);color:var(--tx);font-family:inherit;font-size:13px}
#q:focus{outline:none;border-color:var(--ac)}
.cnt{color:var(--mu);font-size:12px;margin:0 0 10px}
.card{background:var(--card);border:1px solid var(--bd);border-radius:11px;margin-bottom:8px;overflow:hidden}
.hd{display:grid;grid-template-columns:190px 1fr 120px 118px 74px;gap:12px;padding:12px 15px;
align-items:center;cursor:pointer;transition:.12s}
.hd:hover{background:var(--card2)}
.fm{font-weight:700;font-size:13.6px}
.fm small{display:block;font-weight:400;color:var(--mu);font-size:11.3px;margin-top:1px}
.rl{font-size:13.2px;line-height:1.45}
.tags{margin-top:4px;display:flex;gap:5px;flex-wrap:wrap}
.t{font-size:10.6px;padding:1.5px 7px;border-radius:4px;background:var(--card2);color:var(--mu);border:1px solid var(--bd)}
.t.fn{color:var(--ac);border-color:var(--ac)}
.t.tp{color:var(--am);border-color:var(--am)}
.ch{display:inline-block;padding:2.5px 9px;border-radius:20px;font-size:11.4px;font-weight:700;white-space:nowrap}
.ch.open{color:var(--gr);background:var(--grb)}.ch.soon{color:var(--am);background:var(--amb)}
.ch.watch{color:var(--gy);background:var(--gyb)}
.ch.exp{color:var(--rd);background:var(--rdb)}
.card:has(.ch.exp){opacity:.62}
.card:has(.ch.exp):hover{opacity:1}
.dl{font-size:12.4px;font-weight:600;white-space:nowrap}
.dl small{display:block;font-weight:400;color:var(--mu);font-size:10.8px}
.dl.hot{color:var(--rd)}.dl.warm{color:var(--am)}
.go{padding:5px 13px;border-radius:7px;background:var(--ac);color:#fff !important;font-size:12px;
font-weight:700;text-decoration:none;text-align:center;white-space:nowrap}
.go:hover{opacity:.87}
.bd{display:none;padding:0 15px 15px;border-top:1px solid var(--bd);background:var(--card2)}
.card.op .bd{display:block}
.card.op .hd{background:var(--card2)}
.dg{display:grid;grid-template-columns:repeat(auto-fit,minmax(228px,1fr));gap:10px;margin-top:13px}
.d{background:var(--card);border:1px solid var(--bd);border-radius:8px;padding:9px 11px}
.d dt{color:var(--mu);font-size:10.5px;font-weight:700;letter-spacing:.4px;margin-bottom:3px}
.d dd{margin:0;font-size:12.5px;line-height:1.5}
.d.wide{grid-column:1/-1}
.nt{margin-top:11px;padding:9px 12px;background:var(--amb);border-left:3px solid var(--am);
border-radius:0 6px 6px 0;font-size:12.5px;line-height:1.55}
.exp{color:var(--mu);font-size:16px;text-align:center;user-select:none}
.card.op .exp{transform:rotate(180deg)}
h2{font-size:15px;margin:26px 0 9px;color:var(--mu);font-weight:700;letter-spacing:.3px}
.ft{margin-top:34px;padding-top:16px;border-top:1px solid var(--bd);color:var(--mu);font-size:11.8px;line-height:1.7}
.ft b{color:var(--tx)}
.appx{background:var(--card);border:1px solid var(--bd);border-radius:11px;padding:14px 17px;margin-top:12px;font-size:12.8px;line-height:1.65}
.appx a{color:var(--ac);text-decoration:none;font-weight:600}.appx a:hover{text-decoration:underline}
.appx h3{font-size:13.5px;margin:0 0 7px}
.ver{display:inline-block;padding:2px 9px;border-radius:20px;font-size:11.5px;font-weight:700;
background:var(--ac);color:#fff;margin-left:7px;vertical-align:middle}
.log{background:var(--card);border:1px solid var(--bd);border-radius:11px;margin-bottom:14px;overflow:hidden}
.logh{display:flex;align-items:center;gap:9px;padding:11px 15px;cursor:pointer;user-select:none}
.logh:hover{background:var(--card2)}
.logh b{font-size:13.5px}
.logh .when{color:var(--mu);font-size:11.8px;margin-left:auto}
.logb{padding:0 15px 13px}
.entry{padding:11px 0;border-top:1px dashed var(--bd)}
.entry:first-child{border-top:none}
.ehd{display:flex;align-items:baseline;gap:8px;margin-bottom:7px;flex-wrap:wrap}
.ehd .d{background:none;border:none;padding:0;color:var(--mu);font-size:11.5px;font-weight:600}
.ehd .v{font-size:11.5px;font-weight:700;color:var(--ac)}
.ehd .n{color:var(--mu);font-size:12px}
.li{display:flex;gap:8px;align-items:baseline;padding:3.5px 0;font-size:12.7px;line-height:1.55}
.kk{flex:none;font-size:10.5px;font-weight:700;padding:1.5px 7px;border-radius:4px;white-space:nowrap;min-width:56px;text-align:center}
.kk.gr{color:var(--gr);background:var(--grb)} .kk.gy{color:var(--gy);background:var(--gyb)}
.kk.rd{color:var(--rd);background:var(--rdb)} .kk.am{color:var(--am);background:var(--amb)}
.kk.ac{color:var(--ac);background:rgba(91,141,239,.13)}
.more{margin-top:9px;font-size:12.2px;color:var(--ac);cursor:pointer;font-weight:600;user-select:none}
.more:hover{text-decoration:underline}
.hid{display:none}
.arw{color:var(--mu);font-size:15px;transition:transform .15s}
.log.op .arw{transform:rotate(180deg)}
.log:not(.op) .logb{display:none}
@media(max-width:900px){
.hd{grid-template-columns:1fr;gap:7px}
.dl,.ch{justify-self:start}
.go{justify-self:start;padding:6px 18px}
.exp{display:none}
.kpi{min-width:calc(50% - 5px)}
.bar{position:static}}
</style></head><body><div class="w">
<h1>HK 前台求职追踪 · 2027 Summer & Off-cycle</h1>
<div class="sub">香港前台条线(IBD / ECM·DCM / S&amp;T / 研究 / 私行 / 买方投资 / 量化)· 全部链接指向官方入口</div>
<div class="sub" id="fresh" style="margin-top:-12px"></div>
<div class="kpis">
<div class="kpi g"><b id="k1">0</b><span>已开放,现在可投</span></div>
<div class="kpi r"><b id="k2">0</b><span>30 天内截止</span></div>
<div class="kpi a"><b id="k3">0</b><span>即将开放,设提醒</span></div>
<div class="kpi"><b id="k4">0</b><span>收录岗位总数</span></div>
</div>
""")

# —— 提醒板块 ——
for n in NOTICES:
    cls = "alert" if n["lv"]=="urgent" else ("alert am" if n["lv"]=="warn" else "alert info")
    icon = "\u23f0 " if n["lv"]=="urgent" else ""
    html.write(f'<div class="{cls}">{icon}<b>{n["title"]}:</b>{n["body"]}</div>\n')

# —— 更新日志 ——
html.write('<div class="log op"><div class="logh" id="logh"><span class="arw">\u2304</span>'
           f'<b>\u66f4\u65b0\u65e5\u5fd7</b><span class="ver">{VERSION}</span>'
           f'<span class="when">\u6700\u540e\u66f4\u65b0 {UPDATED} \u00b7 \u6bcf\u5468\u4e00\u81ea\u52a8\u6838\u67e5</span></div>'
           '<div class="logb">')
for i, e in enumerate(CHANGELOG):
    hid = " hid oldentry" if i > 0 else ""
    html.write(f'<div class="entry{hid}"><div class="ehd"><span class="d">{e["date"]}</span>'
               f'<span class="v">{e["ver"]}</span><span class="n">{e.get("note","")}</span></div>')
    for it in e["items"]:
        lbl, col = CL_LABEL[it["k"]]
        html.write(f'<div class="li"><span class="kk {col}">{lbl}</span><span>{it["t"]}</span></div>')
    html.write('</div>')
if len(CHANGELOG) > 1:
    html.write(f'<div class="more" id="more">\u5c55\u5f00\u5386\u53f2\u8bb0\u5f55\uff08{len(CHANGELOG)-1} \u6761\u66f4\u65e9\u7684\u66f4\u65b0\uff09\u2304</div>')
html.write('</div></div>\n')

html.write('<div class="bar">\n<div class="row"><span class="lbl">条线</span>')
html.write('<button class="f on" data-k="func" data-v="">全部</button>')
for k,v in FUNC_LABEL.items(): html.write(f'<button class="f" data-k="func" data-v="{k}">{v}</button>')
html.write('</div>\n<div class="row"><span class="lbl">机构</span><button class="f on" data-k="org" data-v="">全部</button>')
for k,v in ORG_LABEL.items(): html.write(f'<button class="f" data-k="org" data-v="{k}">{v}</button>')
html.write('</div>\n<div class="row"><span class="lbl">状态</span><button class="f on" data-k="st" data-v="">全部</button>')
for k,v in ST_LABEL.items(): html.write(f'<button class="f" data-k="st" data-v="{k}">{v}</button>')
html.write('<button class="f" data-k="typ" data-v="Offcycle">只看 Off-cycle</button>')
html.write('<input id="q" placeholder="搜公司 / 岗位 / 关键词…"></div>\n</div>\n')
html.write('<div class="cnt" id="cnt"></div><div id="list"></div>\n')

html.write("""
<h2>附:非前台但通向前台的通道</h2>
<div class="appx">
<h3>Big4 交易咨询(全年滚动、无 GPA 线,是最容易拿到的「正规 deal 经历」)</h3>
<b>KPMG Basecamp — Deal Advisory</b>:冬/夏/off-cycle 三轨 + 5–12 个月 placement,全年按项目补挂 · <a href="https://app.mokahr.com/campus-recruitment/kpmg/70399">mokahr 入口</a>。流程为站内 OA → 面试,官方流程无独立视频面环节。<br>
<b>Deloitte Financial Advisory — Project Intern</b>:弹性 off-cycle、可 part-time,官方明写 penultimate 可投 · <a href="https://wecruit.hotjob.cn/SU64365a780dcad43c5ae82bab/pb/interns.html">hotjob 入口</a>。冬批约 10–11 月、夏批约 4–5 月。<br>
<b>EY Strategy and Transactions(EY-Parthenon)</b> · <a href="https://eyhk.hotjob.cn/">eyhk.hotjob.cn</a>,大二至大四均可,官方流程:网申 → OA → AC → offer。<br>
<b>PwC Deals</b> · <a href="https://app.mokahr.com/campus-recruitment/pwc/148260?locale=en-US">mokahr 入口</a>,站内 OA 为 SHL 式认知 + OPQ 性格。<br>
<b>FTI Consulting — Corporate Finance &amp; Restructuring</b>:历年 11 月开 · <a href="https://fticonsult.referrals.selectminds.com/ftistudentcareers">学生入口</a>,要求中英流利,有投行经历者优先,写「excellent academic records」但无 GPA 数字。<br>
<b>BDO 特殊咨询(估值/尽调/重组)</b> · <a href="https://recruitment.bdo.com.hk">recruitment.bdo.com.hk</a>。
</div>
<div class="appx" style="margin-top:10px">
<h3>科创 / 家办生态(窗口固定,现在设提醒即可)</h3>
<b>HKSTP 科学园实习</b>:下一轮约 11 月开(上轮为 2025年11月–2026年2月28日投递,7 月入职)· <a href="https://www.hkstp.org/en/talent/early-career-and-internship/hkstp-internship-programme">入口</a><br>
<b>FOAHK 香港家族办公室协会联合实习</b>:一个入口覆盖 20+ 家办(Raffles FO、Carret Private、VMS 等),Year 2 以上可投,下一轮约 2027 年 3 月 · <a href="https://www.foahk.org/internship">入口</a>——家办赛道最省力的一枪。<br>
<b>Cyberport</b> 数码港学生机会 · <a href="https://www.cyberport.hk/en/entrepreneurship/opportunities_for_students/">入口</a>(投向生态内初创而非投资岗)。
</div>
<div class="appx" style="margin-top:10px">
<h3>查证为「香港无公开前台实习」的机构 —— 不要在这些上面浪费子弹</h3>
<b>精品行:</b>Evercore(实习只在美国/伦敦)、Centerview(无香港办公室)、Lazard(香港已两个 cycle 无 summer 岗)。<br>
<b>研究条线:</b>MS Research、UBS Research(其 APAC 研究 off-cycle 设在新加坡)、Bernstein(只有资深岗)、CLSA Research、Daiwa、Mizuho、Macquarie Research —— 香港 2027 批均无在挂的研究实习。<br>
<b>PE:</b>Carlyle、Apollo、TPG、CVC、EQT/BPEA、General Atlantic、Bain Capital、PAG、高瓴、Warburg、博裕、春华、鼎晖、方源、MBK、L Catterton —— 亚洲均无固定校园项目,靠 ad hoc 与 networking。<br>
<b>量化:</b>Two Sigma(仅纽约)、Optiver(香港只有资深岗,亚太学生批在悉尼/上海且悉尼要澳洲工作许可)、IMC、SIG(同为悉尼)、Squarepoint、G-Research、九坤香港、Graviton。<br>
<b>主权/养老:</b>CPP、OTPP(2025年3月已关香港办公室)、OMERS、中东主权基金 —— 香港均无学生岗。<br>
<b>企业 CVC:</b>腾讯投资、阿里战投、小米 —— 三家在所有香港求职板与招聘站均查无学生 req,不要信二手转述。
</div>
""")

html.write("""
<div class="ft">
<b>怎么用这张表:</b>点任意一行展开,里面有该岗位的薪资、时长、语言与签证要求、GPA 门槛原文、网申测评与面试流程、历年开放规律。顶部筛选器可按条线 / 机构 / 状态叠加过滤,搜索框支持公司名、岗位名与任意关键词。<br><br>
<b>关于 GPA:</b>核对 12 家大行 posting 原文后,真正写死数字的只有 <b>Jefferies(3.4)</b>、<b>BNP Paribas(3.3)</b> 与 <b>招银国际 SIP(3.3)</b>;Barclays 是「ideally 3.2」的软措辞;HSBC 2026 批写 3.2 但 2027 页面未见。GS / MS / JPM / BofA / Citi / UBS / Nomura / 渣打的香港 posting <b>既不写 GPA 数字,也不在申请阶段强制上传成绩单</b>——渣打更是明确不设 GPA、走 strengths-based。但要清醒:不写不等于不看,多数行会在终面或 offer 后的背景核查阶段要成绩单。<br><br>
<b>关于语言:</b>大行的普遍口径是「英文流利」为底线、亚洲语言加分,<b>但 Barclays 香港岗硬性要求中文书写 + 普通话口语,UBS 香港硬性要求掌握普通话等五种亚洲语言之一</b>。中资与本地精品行(招银国际、BDA、Somerley、Asian Capital)普遍硬性要求中英双语。<br><br>
<b>关于签证:</b>大多数 posting 对签证保持沉默,沉默不等于愿意担保。明确表态的三家:<b>HSBC</b> 明示会考虑需要担保的候选人并接受香港学生签、<b>Deutsche Bank</b> 接受香港学生签、<b>鐘港资本</b> 为海外候选人安排 training visa。<b>BDA Partners</b> 是唯一明确排除的:只收香港永久居民、香港高校在读生或 IANG 持有者。Barclays 要求申请时申报担保需求。<br><br>
<b>关于薪资:</b>香港投行几乎不公开实习薪资。表内标注的数字绝大多数来自 Glassdoor 等自报数据,样本小、且会把前台与科技/运营岗混在一起——月薪低于约 HK$2.5 万的数据点基本是非前台污染。可参照的行业口径是:香港 BB 暑期实习薪资通常按一年级 analyst 薪资折算发放。<br><br>
<b>数据说明:</b>所有链接均来自各机构官方 careers 域名,核验于 2026年8月10日。标「预计」的开放时间是按上一 cycle 规律推断,以官网为准。滚动审(rolling)意味着早投晚投不是同一个竞争面。若某行显示的截止日与官网不一致,以官网为准。
</div></div>
""")

html.write("<script>\nconst D=" + json.dumps(DATA, ensure_ascii=False) + ";\n")
html.write(f'const UPDATED_AT="{UPDATED}";\n')
html.write("const FL=" + json.dumps(FUNC_LABEL, ensure_ascii=False) + ",OL=" + json.dumps(ORG_LABEL, ensure_ascii=False) + ",SL=" + json.dumps(ST_LABEL, ensure_ascii=False) + ";\n")
html.write(r"""
const F={func:"",org:"",st:"",typ:""};
/* 实时基准:每次打开页面按访问者当天重新计算,不依赖构建时写死的日期 */
const TODAY=(function(){var d=new Date();d.setHours(0,0,0,0);return d;})();
function days(s){if(!s)return null;const p=s.split("-");const d=new Date(+p[0],+p[1]-1,+p[2]);
return Math.round((d-TODAY)/864e5);}
/* 截止日已过 → 自动判定为已截止,不用等每周重建 */
function isExp(r){const n=days(r.ddl);return n!==null&&n<0;}
function effSt(r){return isExp(r)?"exp":r.st;}
function esc(s){return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
function dcell(r){const n=days(r.ddl);let cls="",sub="";
if(n!==null){
  if(n<0){cls="hot";sub=(-n)+" 天前已截止";}
  else if(n===0){cls="hot";sub="今天最后一天";}
  else if(n===1){cls="hot";sub="只剩明天";}
  else if(n<=10){cls="hot";sub="剩 "+n+" 天";}
  else if(n<=30){cls="warm";sub="剩 "+n+" 天";}
  else{sub="剩 "+n+" 天";}}
return '<div class="dl '+cls+'">'+esc(r.ddl_txt||"—")+(sub?'<small>'+sub+'</small>':'')+'</div>';}
function row(r,i){const d=[["薪资",r.pay],["时长",r.dur],["语言要求",r.lang],["签证 / 工作权利",r.visa],
["GPA 门槛(原文)",r.gpa],["网申测评与面试流程",r.proc],["历年开放规律",r.pat]];
let dd="";d.forEach(function(x,j){if(!x[1])return;
dd+='<div class="d'+(j>=5?' wide':'')+'"><dt>'+x[0]+'</dt><dd>'+esc(x[1])+'</dd></div>';});
return '<div class="card" data-i="'+i+'"><div class="hd">'+
'<div class="fm">'+esc(r.firm)+'<small>'+OL[r.org]+(r.loc?' · '+esc(r.loc):'')+'</small></div>'+
'<div><div class="rl">'+esc(r.role)+'</div><div class="tags"><span class="t fn">'+FL[r.func]+'</span>'+
'<span class="t tp">'+esc(r.typ)+'</span>'+(r.opened?'<span class="t">上线 '+esc(r.opened)+'</span>':'')+'</div></div>'+
'<div><span class="ch '+effSt(r)+'">'+SL[effSt(r)]+'</span></div>'+dcell(r)+
'<a class="go" href="'+r.url+'" target="_blank" rel="noopener">申请 →</a>'+
'</div><div class="bd"><div class="dg">'+dd+'</div>'+
(r.note?'<div class="nt">'+esc(r.note)+'</div>':'')+'</div></div>';}
function render(){const q=(document.getElementById("q").value||"").toLowerCase();
const out=D.map(function(r,i){return [r,i];}).filter(function(p){const r=p[0];
if(F.func&&r.func!==F.func)return false;if(F.org&&r.org!==F.org)return false;
if(F.st&&effSt(r)!==F.st)return false;
if(F.typ&&r.typ.indexOf("Offcycle")<0&&r.typ.indexOf("双轨")<0)return false;
if(q){const blob=(r.firm+r.role+r.note+r.loc+r.pat+r.proc+r.gpa+r.lang).toLowerCase();
if(blob.indexOf(q)<0)return false;}return true;});
out.sort(function(a,b){const x=days(a[0].ddl),y=days(b[0].ddl);
const ra={open:0,soon:1,watch:2,exp:3}[effSt(a[0])],rb={open:0,soon:1,watch:2,exp:3}[effSt(b[0])];
if(ra!==rb)return ra-rb;
if(x===null&&y===null)return 0;if(x===null)return 1;if(y===null)return -1;return x-y;});
document.getElementById("list").innerHTML=out.map(function(p){return row(p[0],p[1]);}).join("")||
'<div class="cnt">没有符合条件的岗位,换个筛选试试。</div>';
document.getElementById("cnt").textContent="显示 "+out.length+" / "+D.length+" 个岗位 · 按状态与截止日排序 · 点行展开细节";}
document.querySelectorAll(".f").forEach(function(b){b.onclick=function(){const k=b.dataset.k,v=b.dataset.v;
if(k==="typ"){F.typ=F.typ?"":"Offcycle";b.classList.toggle("on");render();return;}
F[k]=v;document.querySelectorAll('.f[data-k="'+k+'"]').forEach(function(o){o.classList.remove("on");});
b.classList.add("on");render();};});
document.getElementById("q").oninput=render;
document.getElementById("list").onclick=function(e){if(e.target.closest(".go"))return;
const c=e.target.closest(".card");if(c)c.classList.toggle("op");};
var lh=document.getElementById("logh");
if(lh)lh.onclick=function(){document.querySelector(".log").classList.toggle("op");};
var mb=document.getElementById("more");
if(mb)mb.onclick=function(e){e.stopPropagation();
var hs=document.querySelectorAll(".oldentry"),sh=hs[0]&&hs[0].classList.contains("hid");
hs.forEach(function(x){x.classList.toggle("hid",!sh);});
mb.textContent=sh?"收起历史记录 ⌃":"展开历史记录("+hs.length+" 条更早的更新) ⌄";};
/* KPI 同样实时算:已截止的自动从「现在可投」里剔除 */
document.getElementById("k1").textContent=D.filter(function(r){return effSt(r)==="open";}).length;
document.getElementById("k2").textContent=D.filter(function(r){const n=days(r.ddl);return n!==null&&n>=0&&n<=30;}).length;
document.getElementById("k3").textContent=D.filter(function(r){return effSt(r)==="soon";}).length;
document.getElementById("k4").textContent=D.length;

/* 数据新鲜度:超过 10 天没核查就显式提示,不让人误以为是最新的 */
(function(){
var u=UPDATED_AT.split("-"),ud=new Date(+u[0],+u[1]-1,+u[2]);
var age=Math.round((TODAY-ud)/864e5);
var el=document.getElementById("fresh");
if(!el)return;
var t=TODAY.getFullYear()+" 年 "+(TODAY.getMonth()+1)+" 月 "+TODAY.getDate()+" 日";
el.innerHTML="今天是 "+t+" · 下方倒计时按今天实时计算 · 数据最后核查于 "+UPDATED_AT+
 (age<=0?"(今天)":"("+age+" 天前)");
if(age>10){var w=document.createElement("div");w.className="alert";
w.innerHTML="<b>⚠ 数据可能已过时:</b>距上次核查已 "+age+
" 天,自动更新可能没跑起来(常见原因是 GitHub token 过期)。下方状态与截止日请以各机构官网为准。";
var host=document.querySelector(".kpis");host.parentNode.insertBefore(w,host.nextSibling);}
})();
render();
</script></body></html>""")

open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)),"index.html"),"w",encoding="utf-8").write(html.getvalue())
print("rows:", len(DATA))
print("open:", sum(1 for r in DATA if r["st"]=="open"))
