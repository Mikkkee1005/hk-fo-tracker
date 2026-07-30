# 维护说明(给每次执行更新的会话看)

## 架构

- `build.py` —— **唯一的数据源**。所有岗位是脚本顶部一连串 `add(...)` 调用。
- `index.html` —— **构建产物,永远不要手工编辑**。跑 `python3 build.py` 由 build.py 生成。
- 站点地址:https://mikkkee1005.github.io/hk-fo-tracker/ (GitHub Pages,main 分支 / root)

## 更新流程

```bash
git clone https://github.com/Mikkkee1005/hk-fo-tracker.git && cd hk-fo-tracker
# 1. 读 build.py,看现有 104 条记录的字段结构
# 2. 核查:先查 st="open" 且有 ddl 的岗位是否还开着;再查 st="soon" 的是否已开放
# 3. 改 build.py 里对应的 add(...) 参数
# 4. 重新生成并验证
python3 build.py           # 会打印 rows / open 数量
# 5. 提交推送(见下方 git 注意事项)
```

改完务必跑一次 `python3 build.py` 确认无报错,再用无头浏览器验证 JS 无错、卡片数量正确:

```bash
npm i playwright --silent
node -e "const{chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox']});const p=await b.newPage();const e=[];p.on('pageerror',x=>e.push(''+x));await p.goto('file://'+process.cwd()+'/index.html');await p.waitForTimeout(800);console.log('errors:',e.length?e:'none','cards:',await p.locator('.card').count());await b.close()})()"
```

## 每次更新必做的三件事(顺序不能省)

1. **改 `VERSION` 和 `UPDATED`** —— `UPDATED` 写今天,`VERSION` 小版本号 +1(v1.2 → v1.3)。
2. **在 `CHANGELOG` 列表**最前面插入一条新条目。这是使用者最先看的东西,写清楚这周变了什么:

```python
{"date":"2026-08-03","ver":"v1.3","note":"一句话说明这次更新的性质,没什么可说就留空字符串",
 "items":[
   {"k":"new",  "t":"<b>Citi 香港 IBD</b> 2027 暑期岗已挂出,截止 X 月 X 日。"},
   {"k":"ddl",  "t":"<b>Morgan Stanley</b> 第一轮 8/16 已过,现在走第二轮 9/27。"},
   {"k":"close","t":"<b>UBS</b> 香港两个暑期岗 8/6 已截止,已从可投列表下掉。"},
 ]}
```
`k` 取值:`new` 新开放 / `close` 已关闭 / `ddl` 截止变动 / `add` 新增收录 / `info` 信息。
`t` 里可以用 `<b></b>`,会原样渲染。**这周没变化就写一条 `info` 说明「本周无变化」,不要跳过条目。**

3. **更新 `NOTICES`** —— 顶部那几个提醒框。把已经过期的时点删掉,换成当下最紧的。`lv` 取 `urgent`(红)/ `warn`(黄)/ `info`(蓝),最多留三条,别堆。

## 字段说明

| 字段 | 取值 |
|---|---|
| `func` | `IBD` / `ECM` / `S&T` / `RES` / `PB` / `BUY` / `QUANT` |
| `org` | `BB` 外资投行 / `EB` 精品行 / `CN` 中资在港 / `BUY` 买方 / `QUANT` 量化Prop / `VC` VC·Crypto |
| `st` | `open` 已开放 / `soon` 即将开放 / `watch` 待观察 |
| `typ` | `Summer` / `Offcycle` / `双轨` |
| `ddl` | ISO 日期 `YYYY-MM-DD`,用于倒计时;不确定就留空 |
| `ddl_txt` | 展示用文案,如 `9/30(滚动审)` |

## 倒计时是自动的,不要手工维护

页面里的「剩 N 天」按**访问者打开页面的当天**实时计算(`const TODAY=new Date()`),不依赖构建时间。
由此自动发生、**不需要你做任何事**的行为:

- 截止日一过,该岗位状态自动变成「已截止」、透明度降低、排序沉到列表底部;
- 「已开放,现在可投」和「30 天内截止」两个计数自动把过期项剔除;
- 顶部显示「数据最后核查于 X(N 天前)」,N 由 `UPDATED` 与当天相减得出;
- **N > 10 时页面自动弹出橙色警告**,提示自动更新可能没跑起来。

也就是说:即使某周自动更新失败,页面也不会假装数据是新的。但这只解决「时间流逝」,
**不解决「岗位状态变了」**——机构提前关闭、临时加开、截止日改动,仍然只有靠每周核查发现。
所以 `st` 和 `ddl` 该改还是要改。

## git 推送注意

这个云环境的 `/root/.gitconfig` 有一条 URL 重写,会把 `https://github.com/` 改写到本地 git 代理并用它自己的凭证,导致用户 token 失效、报 403。推送时必须屏蔽掉:

```bash
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null GIT_CONFIG_COUNT=0
unset GITHUB_TOKEN GIT_ASKPASS
git -c user.email=noreply@anthropic.com -c user.name=Claude -c commit.gpgsign=false \
    -c credential.interactive=false \
    push "https://x-access-token:${TOKEN}@github.com/Mikkkee1005/hk-fo-tracker.git" HEAD:main
```

注意:GitHub REST API(api.github.com)在这个环境被网关拦截,**只有 git 协议可用**。
另外 `mikkkee1005.github.io` 在沙箱内不可达,验证站点是否生效要用浏览器工具,不能用 curl。

## 口径

只收**前台**:IBD / ECM·DCM / Sales & Trading / 股票研究 / 私行财富管理 / 买方投资岗 / 量化。
中后台(风控、产品控制、COO、运营、科技)不进主表。Big4 交易咨询、HKSTP、FOAHK 等放页尾附录。

不要编造链接。查不到就把状态标 `watch` 并在 `note` 里写明查证结论。
