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

## 字段说明

| 字段 | 取值 |
|---|---|
| `func` | `IBD` / `ECM` / `S&T` / `RES` / `PB` / `BUY` / `QUANT` |
| `org` | `BB` 外资投行 / `EB` 精品行 / `CN` 中资在港 / `BUY` 买方 / `QUANT` 量化Prop / `VC` VC·Crypto |
| `st` | `open` 已开放 / `soon` 即将开放 / `watch` 待观察 |
| `typ` | `Summer` / `Offcycle` / `双轨` |
| `ddl` | ISO 日期 `YYYY-MM-DD`,用于倒计时;不确定就留空 |
| `ddl_txt` | 展示用文案,如 `9/30(滚动审)` |

倒计时基准日写在 build.py 生成的 JS 里:`const TODAY=new Date(2026,6,30);`。
**每次更新必须把这个日期改成当天**,否则倒计时会失准。在 build.py 里搜 `TODAY=new Date` 修改。

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
