<h1 align="center">⚔️ 多Agent协作 · Edict</h1>

<p align="center">
  <strong>我用 1300 年前的帝国制度，重新设计了 AI 多 Agent 协作架构。<br>结果发现，古人比现代 AI 框架更懂分权制衡。</strong>
</p>

<p align="center">
  <sub>12 个 AI Agent（11 个业务角色 + 1 个兼容角色）组成多Agent协作：前台分拣、产品经理规划、质量审核审核驳回、项目经理派发、六部+人力资源并行执行。<br>比 CrewAI 多一层<b>制度性审核</b>，比 AutoGen 多一个<b>实时看板</b>。</sub>
</p>

<p align="center">
  <a href="#-demo">🎬 看 Demo</a> ·
  <a href="#-30-秒快速体验">🚀 30 秒体验</a> ·
  <a href="#-架构">🏛️ 架构</a> ·
  <a href="#-功能全景">📋 看板功能</a> ·
  <a href="docs/task-dispatch-architecture.md">📚 架构文档</a> ·
  <a href="README_EN.md">English</a> ·
  <a href="CONTRIBUTING.md">参与贡献</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/OpenClaw-Required-blue?style=flat-square" alt="OpenClaw">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Agents-12_Specialized-8B5CF6?style=flat-square" alt="Agents">
  <img src="https://img.shields.io/badge/Dashboard-Real--time-F59E0B?style=flat-square" alt="Dashboard">
  <img src="https://img.shields.io/badge/License-MIT-22C55E?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Frontend-React_18-61DAFB?style=flat-square&logo=react&logoColor=white" alt="React">
  <img src="https://img.shields.io/badge/Backend-stdlib_only-EC4899?style=flat-square" alt="Zero Backend Dependencies">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/公众号-cft0808-07C160?style=for-the-badge&logo=wechat&logoColor=white" alt="WeChat">
</p>

---

## 🎬 Demo

<p align="center">
  <video src="docs/Agent_video_Pippit_20260225121727.mp4" width="100%" autoplay muted loop playsinline controls>
    您的浏览器不支持视频播放，请查看下方 GIF 或 <a href="docs/Agent_video_Pippit_20260225121727.mp4">下载视频</a>。
  </video>
  <br>
  <sub>🎥 多Agent协作 AI 多 Agent 协作全流程演示</sub>
</p>

<details>
<summary>📸 GIF 预览（加载更快）</summary>
<p align="center">
  <img src="docs/demo.gif" alt="多Agent协作 Demo" width="100%">
  <br>
  <sub>飞书下发 → 前台分拣 → 产品经理规划 → 质量审核审议 → 六部并行执行 → 报告回报（30 秒）</sub>
</p>
</details>

> 🐳 **没有 OpenClaw？** 跑一行 `docker run -p 7891:7891 cft0808/edict` 即可体验完整看板 Demo（预置模拟数据）。

---

## 🤔 为什么是多Agent协作？

大多数 Multi-Agent 框架的套路是：

> *"来，你们几个 AI 自己聊，聊完把结果给我。"*

然后你拿到一坨不知道经过了什么处理的结果，无法复现，无法审计，无法干预。

**多Agent协作的思路完全不同** —— 我们用了一个在中国存在 1400 年的制度架构：

```
你 (用户) → 前台 (分拣) → 产品经理 (规划) → 质量审核 (审议) → 项目经理 (派发) → 六部 (执行) → 汇报
```

这不是花哨的 metaphor，这是**真正的分权制衡**：

| | CrewAI | MetaGPT | AutoGen | **多Agent协作** |
|---|:---:|:---:|:---:|:---:|
| **审核机制** | ❌ 无 | ⚠️ 可选 | ⚠️ Human-in-loop | **✅ 质量审核专职审核 · 可驳回** |
| **实时看板** | ❌ | ❌ | ❌ | **✅ 运营中心 Kanban + 时间线** |
| **任务干预** | ❌ | ❌ | ❌ | **✅ 叫停 / 取消 / 恢复** |
| **流转审计** | ⚠️ | ⚠️ | ❌ | **✅ 完整报告存档** |
| **Agent 健康监控** | ❌ | ❌ | ❌ | **✅ 心跳 + 活跃度检测** |
| **热切换模型** | ❌ | ❌ | ❌ | **✅ 看板内一键切换 LLM** |
| **技能管理** | ❌ | ❌ | ❌ | **✅ 查看 / 添加 Skills** |
| **新闻聚合推送** | ❌ | ❌ | ❌ | **✅ 天下要闻 + 飞书推送** |
| **部署难度** | 中 | 高 | 中 | **低 · 一键安装 / Docker** |

> **核心差异：制度性审核 + 完全可观测 + 实时可干预**

<details>
<summary><b>🔍 为什么「质量审核审核」是杀手锏？（点击展开）</b></summary>

<br>

CrewAI 和 AutoGen 的 Agent 协作模式是 **"做完就交"**——没有人检查产出质量。就像一个公司没有 QA 部门，工程师写完代码直接上线。

多Agent协作的 **质量审核** 专门干这件事：

- 📋 **审查方案质量** —— 产品经理的规划是否完备？子任务拆解是否合理？
- 🚫 **驳回不合格的产出** —— 不是 warning，是直接打回重做
- 🔄 **强制返工循环** —— 直到方案达标才放行

这不是可选的插件——**它是架构的一部分**。每一个任务都必须经过质量审核，没有例外。

这就是为什么多Agent协作能处理复杂任务而结果可靠：因为在送到执行层之前，有一个强制的质量关卡。1300 年前唐太宗就想明白了——**不受制约的权力必然会出错**。

</details>

---

## ✨ 功能全景

### 🏛️ 十二部制 Agent 架构
- **前台** 消息分拣 —— 闲聊自动回复，任务才建任务
- **三省**（中书·门下·尚书）负责规划、审议、派发
- **七部**（户·礼·兵·刑·工·吏 + 晨会官）负责专项执行
- 严格的权限矩阵 —— 谁能给谁发消息，白纸黑字
- 每个 Agent 独立 Workspace · 独立 Skills · 独立模型
- **任务数据清洗** —— 标题/备注自动剥离文件路径、元数据、无效前缀

### 📋 运营中心看板（10 个功能面板）

<table>
<tr><td width="50%">

**📋 任务看板 · Kanban**
- 按状态列展示全部任务
- 省部过滤 + 全文搜索
- 心跳徽章（🟢活跃 🟡停滞 🔴告警）
- 任务详情 + 完整流转链
- 叫停 / 取消 / 恢复操作

</td><td width="50%">

**🔭 省部调度 · Monitor**
- 可视化各状态任务数量
- 部门分布横向条形图
- Agent 健康状态实时卡片

</td></tr>
<tr><td>

**📜 报告阁 · Memorials**
- 已完成任务自动归档为报告
- 五阶段时间线：任务单→中书→门下→六部→汇报
- 一键复制为 Markdown
- 按状态筛选

</td><td>

**📜 旨库 · Template Library**
- 9 个预设任务单模板
- 分类筛选 · 参数表单 · 预估时间和费用
- 预览任务 → 一键下发

</td></tr>
<tr><td>

**👥 官员总览 · Officials**
- Token 消耗排行榜
- 活跃度 · 完成数 · 会话统计

</td><td>

**📰 天下要闻 · News**
- 每日自动采集科技/财经资讯
- 分类订阅管理 + 飞书推送

</td></tr>
<tr><td>

**⚙️ 模型配置 · Models**
- 每个 Agent 独立切换 LLM
- 应用后自动重启 Gateway（~5秒生效）

</td><td>

**🛠️ 技能配置 · Skills**
- 各省部已安装 Skills 一览
- 查看详情 + 添加新技能

</td></tr>
<tr><td>

**💬 小任务 · Sessions**
- OC-* 会话实时监控
- 来源渠道 · 心跳 · 消息预览

</td><td>

**🎬 上朝仪式 · Ceremony**
- 每日首次打开播放开场动画
- 今日统计 · 3.5秒自动消失

</td></tr>
</table>

---

## 🖼️ 截图

### 任务看板
![任务看板](docs/screenshots/01-kanban-main.png)

<details>
<summary>📸 展开查看更多截图</summary>

### 省部调度
![省部调度](docs/screenshots/02-monitor.png)

### 任务流转详情
![任务流转详情](docs/screenshots/03-task-detail.png)

### 模型配置
![模型配置](docs/screenshots/04-model-config.png)

### 技能配置
![技能配置](docs/screenshots/05-skills-config.png)

### 官员总览
![官员总览](docs/screenshots/06-official-overview.png)

### 会话记录
![会话记录](docs/screenshots/07-sessions.png)

### 报告归档
![报告归档](docs/screenshots/08-memorials.png)

### 任务单模板
![任务单模板](docs/screenshots/09-templates.png)

### 天下要闻
![天下要闻](docs/screenshots/10-morning-briefing.png)

### 上朝仪式
![上朝仪式](docs/screenshots/11-ceremony.png)

</details>

---

## 🚀 30 秒快速体验

### Docker 一键启动

```bash
docker run -p 7891:7891 cft0808/sansheng-demo
```
打开 http://localhost:7891 即可体验运营中心看板。

<details>
<summary><b>⚠️ 遇到 <code>exec format error</code>？（点击展开）</b></summary>

如果你在 **x86/amd64** 机器（如 Ubuntu、WSL2）上看到：
```
exec /usr/local/bin/python3: exec format error
```

这是因为镜像架构不匹配。请使用 `--platform` 参数：
```bash
docker run --platform linux/amd64 -p 7891:7891 cft0808/sansheng-demo
```

或使用 docker-compose（已内置 `platform: linux/amd64`）：
```bash
docker compose up
```

</details>

### 完整安装

#### 前置条件
- [OpenClaw](https://openclaw.ai) 已安装
- Python 3.9+
- macOS / Linux

#### 安装

```bash
git clone https://github.com/cft0808/edict.git
cd edict
chmod +x install.sh && ./install.sh
```

安装脚本自动完成：
- ✅ 创建全量 Agent Workspace（含前台/人力资源/晨会，兼容历史 main）
- ✅ 写入各省部 SOUL.md（角色人格 + 工作流规则 + 数据清洗规范）
- ✅ 注册 Agent 及权限矩阵到 `openclaw.json`
- ✅ 构建 React 前端（需 Node.js 18+，如未安装则跳过）
- ✅ 初始化数据目录 + 首次数据同步
- ✅ 重启 Gateway 使配置生效

#### 启动

```bash
# 终端 1：数据刷新循环
bash scripts/run_loop.sh

# 终端 2：看板服务器
python3 dashboard/server.py

# 打开浏览器
open http://127.0.0.1:7891
```

> 💡 **看板即开即用**：`server.py` 内嵌 `dashboard/dashboard.html`，Docker 镜像包含预构建的 React 前端

> 💡 详细教程请看 [Getting Started 指南](docs/getting-started.md)

---

## 🏛️ 架构

```
                           ┌───────────────────────────────────┐
                           │          👑 用户（你）              │
                           │     Feishu · Telegram · Signal     │
                           └─────────────────┬─────────────────┘
                                             │ 下发
                           ┌─────────────────▼─────────────────┐
                           │          � 前台 (taizi)            │
                           │    分拣：闲聊直接回 / 任务建任务      │
                           └─────────────────┬─────────────────┘
                                             │ 传达
                           ┌─────────────────▼─────────────────┐
                           │          📜 产品经理 (zhongshu)       │
                           │       接单 → 规划 → 拆解子任务       │
                           └─────────────────┬─────────────────┘
                                             │ 提交审核
                           ┌─────────────────▼─────────────────┐
                           │          🔍 质量审核 (menxia)         │
                           │       审议方案 → 通过 / 驳回 🚫      │
                           └─────────────────┬─────────────────┘
                                             │ 通过 ✅
                           ┌─────────────────▼─────────────────┐
                           │          📮 项目经理 (shangshu)       │
                           │     派发任务 → 协调六部 → 汇总汇报    │
                           └───┬──────┬──────┬──────┬──────┬───┘
                               │      │      │      │      │
                         ┌─────▼┐ ┌───▼───┐ ┌▼─────┐ ┌───▼─┐ ┌▼─────┐
                         │💰 财务│ │📝 文档部│ │⚔️ 研发部│ │⚖️ 合规部│ │🔧 运维部│
                         │ 数据  │ │ 文档  │ │ 工程  │ │ 合规  │ │ 基建  │
                         └──────┘ └──────┘ └──────┘ └─────┘ └──────┘
                                                               ┌──────┐
                                                               │📋 人力资源│
                                                               │ 人事  │
                                                               └──────┘
```

### 各省部职责

| 部门 | Agent ID | 职责 | 擅长领域 |
|------|----------|------|---------|
| � **前台** | `taizi` | 消息分拣、需求整理 | 闲聊识别、任务提炼、标题概括 |
| 📜 **产品经理** | `zhongshu` | 接单、规划、拆解 | 需求理解、任务分解、方案设计 |
| 🔍 **质量审核** | `menxia` | 审议、把关、驳回 | 质量评审、风险识别、标准把控 |
| 📮 **项目经理** | `shangshu` | 派发、协调、汇总 | 任务调度、进度跟踪、结果整合 |
| 💰 **财务** | `hubu` | 数据、资源、核算 | 数据处理、报表生成、成本分析 |
| 📝 **文档部** | `libu` | 文档、规范、报告 | 技术文档、API 文档、规范制定 |
| ⚔️ **研发部** | `bingbu` | 代码、算法、巡检 | 功能开发、Bug 修复、代码审查 |
| ⚖️ **合规部** | `xingbu` | 安全、合规、审计 | 安全扫描、合规检查、红线管控 |
| 🔧 **运维部** | `gongbu` | CI/CD、部署、工具 | Docker 配置、流水线、自动化 |
| 📋 **人力资源** | `libu_hr` | 人事、Agent 管理 | Agent 注册、权限维护、培训 |
| 🌅 **晨会官** | `zaochao` | 每日晨会、新闻聚合 | 定时播报、数据汇总 |

### 权限矩阵

> 不是想发就能发 —— 真正的分权制衡

| From ↓ \ To → | 前台 | 中书 | 门下 | 尚书 | 户 | 礼 | 兵 | 刑 | 工 | 吏 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **前台** | — | ✅ | | | | | | | | |
| **产品经理** | ✅ | — | ✅ | ✅ | | | | | | |
| **质量审核** | | ✅ | — | ✅ | | | | | | |
| **项目经理** | | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **六部+人力资源** | | | | ✅ | | | | | | |

### 任务状态流转

```
用户 → 前台分拣 → 中书规划 → 门下审议 → 已派发 → 执行中 → 待审查 → ✅ 已完成
                      ↑          │                              │
                      └──── 驳回 ─┘                    阻塞 Blocked
```

---

## 📁 项目结构

```
edict/
├── agents/                     # 12 个 Agent 的人格模板
│   ├── taizi/SOUL.md           # 前台 · 消息分拣（含任务标题规范）
│   ├── zhongshu/SOUL.md        # 产品经理 · 规划中枢
│   ├── menxia/SOUL.md          # 质量审核 · 审议把关
│   ├── shangshu/SOUL.md        # 项目经理 · 调度大脑
│   ├── hubu/SOUL.md            # 财务 · 数据资源
│   ├── libu/SOUL.md            # 文档部 · 文档规范
│   ├── bingbu/SOUL.md          # 研发部 · 工程实现
│   ├── xingbu/SOUL.md          # 合规部 · 合规审计
│   ├── gongbu/SOUL.md          # 运维部 · 基础设施
│   ├── libu_hr/                # 人力资源 · 人事管理
│   └── zaochao/SOUL.md         # 晨会官 · 情报枢纽
├── dashboard/
│   ├── dashboard.html          # 运营中心看板（单文件 · 零依赖 · ~2500 行）
│   ├── dist/                   # React 前端构建产物（Docker 镜像内包含，本地可选）
│   └── server.py               # API 服务器（Python 标准库 · 零依赖 · ~1200 行）
├── scripts/
│   ├── run_loop.sh             # 数据刷新循环（每 15 秒）
│   ├── kanban_update.py        # 看板 CLI（含任务数据清洗 + 标题校验）
│   ├── skill_manager.py        # Skill 管理工具（远程/本地 Skills 添加、更新、移除）
│   ├── sync_from_openclaw_runtime.py
│   ├── sync_agent_config.py
│   ├── sync_officials_stats.py
│   ├── fetch_morning_news.py
│   ├── refresh_live_data.py
│   ├── apply_model_changes.py
│   └── file_lock.py            # 文件锁（防多 Agent 并发写入）
├── tests/
│   └── test_e2e_kanban.py      # 端到端测试（17 个断言）
├── data/                       # 运行时数据（gitignored）
├── docs/
│   ├── task-dispatch-architecture.md  # 📚 详细架构文档：任务分发、流转、调度的完整设计（业务+技术）
│   ├── getting-started.md             # 快速上手指南
│   ├── wechat-article.md              # 微信文章
│   └── screenshots/                   # 功能截图（11 张）
├── install.sh                  # 一键安装脚本
├── CONTRIBUTING.md             # 贡献指南
└── LICENSE                     # MIT License
```

---

## 🎯 使用方法

### 向 AI 下发

通过 Feishu / Telegram / Signal 给产品经理发消息：

```
给我设计一个用户注册系统，要求：
1. RESTful API（FastAPI）
2. PostgreSQL 数据库
3. JWT 鉴权
4. 完整测试用例
5. 部署文档
```

**然后坐好，看戏：**

1. 📜 产品经理接单，规划子任务分配方案
2. 🔍 质量审核审议，通过 / 驳回打回重规划
3. 📮 项目经理通过，派发给研发部 + 运维部 + 文档部
4. ⚔️ 各部并行执行，进度实时可见
5. 📮 项目经理汇总结果，汇报给你

全程可在**运营中心看板**实时监控，随时可以**叫停、取消、恢复**。

### 使用任务单模板

> 看板 → 📜 旨库 → 选模板 → 填参数 → 下发

9 个预设模板：周报生成 · 代码审查 · API 设计 · 竞品分析 · 数据报告 · 博客文章 · 部署方案 · 邮件文案 · 站会摘要

### 自定义 Agent

编辑 `agents/<id>/SOUL.md` 即可修改 Agent 的人格、职责和输出规范。

### 增补 Skills（从网上连接）

**三种方式添加 Skills：**

#### 1️⃣ 看板 UI（最简单）

```
看板 → 🔧 技能配置 → ➕ 添加远程 Skill
→ 输入 Agent + Skill 名称 + GitHub URL
→ 确认 → ✅ 完成
```

#### 2️⃣ CLI 命令（最灵活）

```bash
# 从 GitHub 添加 code_review skill 到产品经理
python3 scripts/skill_manager.py add-remote \
  --agent zhongshu \
  --name code_review \
  --source https://raw.githubusercontent.com/openclaw-ai/skills-hub/main/code_review/SKILL.md \
  --description "代码审查技能"

# 一键导入官方 skills 库到指定 agents
python3 scripts/skill_manager.py import-official-hub \
  --agents zhongshu,menxia,shangshu,bingbu,xingbu

# 列出所有已添加的远程 skills
python3 scripts/skill_manager.py list-remote

# 更新某个 skill 到最新版本
python3 scripts/skill_manager.py update-remote \
  --agent zhongshu \
  --name code_review
```

#### 3️⃣ API 请求（自动化集成）

```bash
# 添加远程 skill
curl -X POST http://localhost:7891/api/add-remote-skill \
  -H "Content-Type: application/json" \
  -d '{
    "agentId": "zhongshu",
    "skillName": "code_review",
    "sourceUrl": "https://raw.githubusercontent.com/...",
    "description": "代码审查"
  }'

# 查看所有远程 skills
curl http://localhost:7891/api/remote-skills-list
```

**官方 Skills Hub：** https://github.com/openclaw-ai/skills-hub

支持的 Skills：
- `code_review` — 代码审查（Python/JS/Go）
- `api_design` — API 设计审查
- `security_audit` — 安全审计
- `data_analysis` — 数据分析
- `doc_generation` — 文档生成
- `test_framework` — 测试框架设计

详见 [🎓 远程 Skills 资源管理指南](docs/remote-skills-guide.md)

---

## 🔧 技术亮点

| 特点 | 说明 |
|------|------|
| **React 18 前端** | TypeScript + Vite + Zustand 状态管理，13 个功能组件 |
| **纯 stdlib 后端** | `server.py` 基于 `http.server`，零依赖，同时提供 API + 静态文件服务 |
| **Agent 思考可视** | 实时展示 Agent 的 thinking 过程、工具调用、返回结果 |
| **一键安装** | `install.sh` 自动完成全部配置 |
| **15 秒同步** | 数据自动刷新，看板倒计时显示 |
| **每日仪式** | 首次打开播放上朝开场动画 |
| **远程 Skills 生态** | 从 GitHub/URL 一键导入能力，支持版本管理 + CLI + API + UI |

---

## � 深入了解

### 核心文档

- **[📖 任务分发流转完整架构](docs/task-dispatch-architecture.md)** — **必读文档**
  - 详细讲解多Agent协作如何处理复杂任务的业务设计和技术实现
  - 涵盖：9大任务状态机 / 权限矩阵 / 4阶段调度（重试→升级→回滚）/ Session JSONL数据融合
  - 包含完整的使用案例、API端点说明、CLI工具文档
  - 对标 CrewAI/AutoGen：为什么制度化>自由协作
  - 故障场景与恢复机制
  - **读这个文档会理解为什么多Agent协作这么强大**（9500+ 字，30 分钟完整理解）

- **[🎓 远程 Skills 资源管理指南](docs/remote-skills-guide.md)** — Skills 生态
  - 从网上连接和增补 skills，支持 GitHub/Gitee/任意 HTTPS URL
  - 官方 Skills Hub 预设能力库
  - CLI 工具 + 看板 UI + Restful API
  - Skills 文件规范与安全防护
  - 支持版本管理和一键更新

- **[⚡ Remote Skills 快速入门](docs/remote-skills-quickstart.md)** — 5 分钟上手
  - 快速体验、CLI 命令、看板操作示例
  - 创建自己的 Skills 库
  - API 完整参考 + 常见问题

- **[🚀 快速上手指南](docs/getting-started.md)** — 新手入门
- **[🤝 贡献指南](CONTRIBUTING.md)** — 想参与贡献？从这里开始

---
## 🔧 常见问题排查

<details>
<summary><b>❌ 任务总超时 / 下属完成了但无法传回前台</b></summary>

**症状**：六部或项目经理已完成任务，但前台收不到回报，最终超时。

**排查步骤**：

1. **检查 Agent 注册状态**：
```bash
curl -s http://127.0.0.1:7891/api/agents-status | python3 -m json.tool
```
确认 `taizi` agent 的 `statusLabel` 是 `alive`。

2. **检查 Gateway 日志**：
```bash
ls /tmp/openclaw/ | tail -5          # 找到最新日志
grep -i "error\|fail\|unknown" /tmp/openclaw/openclaw-*.log | tail -20
```

3. **常见原因**：
   - Agent ID 不匹配（已在 v1.2 修复：`main` → `taizi`）
   - LLM provider 超时（增加了自动重试）
   - 僵尸 Agent 进程（运行 `ps aux | grep openclaw` 检查）

4. **强制重试**：
```bash
# 手动触发巡检扫描（自动重试卡住的任务）
curl -X POST http://127.0.0.1:7891/api/scheduler-scan \
  -H 'Content-Type: application/json' -d '{"thresholdSec":60}'
```

</details>

<details>
<summary><b>❌ Docker: exec format error</b></summary>

**症状**：`exec /usr/local/bin/python3: exec format error`

**原因**：镜像架构（arm64）与主机架构（amd64）不匹配。

**解决**：
```bash
# 方法 1：指定平台
docker run --platform linux/amd64 -p 7891:7891 cft0808/sansheng-demo

# 方法 2：使用 docker-compose（已内置 platform）
docker compose up
```

</details>

<details>
<summary><b>❌ Skill 下载失败</b></summary>

**症状**：`python3 scripts/skill_manager.py import-official-hub` 报错。

**排查**：
```bash
# 测试网络连通性
curl -I https://raw.githubusercontent.com/openclaw-ai/skills-hub/main/code_review/SKILL.md

# 如果超时，使用代理
export https_proxy=http://your-proxy:port
python3 scripts/skill_manager.py import-official-hub --agents zhongshu
```

**常见原因**：
- 中国大陆访问 GitHub raw 资源需要代理
- 网络超时（已增加到 30 秒 + 自动重试 3 次）
- 官方 Skills Hub 仓库维护中

</details>

---
## �🗺️ Roadmap

> 完整路线图及参与方式：[ROADMAP.md](ROADMAP.md)

### Phase 1 — 核心架构 ✅
- [x] 十二部制 Agent 架构（前台 + 三省 + 七部 + 晨会官）+ 权限矩阵
- [x] 运营中心实时看板（10 个功能面板 + 实时活动面板）
- [x] 任务叫停 / 取消 / 恢复
- [x] 报告系统（自动归档 + 五阶段时间线）
- [x] 任务单模板库（9 个预设 + 参数表单）
- [x] 上朝仪式感动画
- [x] 天下要闻 + 飞书推送 + 订阅管理
- [x] 模型热切换 + 技能管理 + 技能添加
- [x] 官员总览 + Token 消耗统计
- [x] 小任务 / 会话监控
- [x] 前台消息分拣（闲聊自动回复 / 任务建任务）
- [x] 任务数据清洗（路径/元数据/前缀自动剥离）
- [x] 重复任务防护 + 已完成任务保护
- [x] 端到端测试覆盖（17 个断言）
- [x] React 18 前端重构（TypeScript + Vite + Zustand · 13 组件）
- [x] Agent 思考过程可视化（实时 thinking / 工具调用 / 返回结果）
- [x] 前后端一体化部署（server.py 同时提供 API + 静态文件服务）

### Phase 2 — 制度深化 🚧
- [ ] 御批模式（人工审批 + 一键通过/驳回）
- [ ] 功过簿（Agent 绩效评分体系）
- [ ] 急递铺（Agent 间实时消息流可视化）
- [ ] 国史馆（知识库检索 + 引用溯源）

### Phase 3 — 生态扩展
- [ ] Docker Compose + Demo 镜像
- [ ] Notion / Linear 适配器
- [ ] 年度大考（Agent 年度绩效报告）
- [ ] 移动端适配 + PWA
- [ ] ClawHub 上架

---

## 🤝 参与贡献

欢迎任何形式的贡献！详见 [CONTRIBUTING.md](CONTRIBUTING.md)

特别欢迎的方向：
- 🎨 **UI 增强**：深色/浅色主题、响应式、动画优化
- 🤖 **新 Agent**：适合特定场景的专职 Agent 角色
- 📦 **Skills 生态**：各部门专用技能包
- 🔗 **集成扩展**：Notion · Jira · Linear · GitHub Issues
- 🌐 **国际化**：日文 · 韩文 · 西班牙文
- 📱 **移动端**：响应式适配、PWA

---

## 📂 案例

`examples/` 目录收录了真实的端到端使用案例：

| 案例 | 任务 | 涉及部门 |
|------|------|----------|
| [竞品分析](examples/competitive-analysis.md) | "分析 CrewAI vs AutoGen vs LangGraph" | 中书→门下→财务+研发部+文档部 |
| [代码审查](examples/code-review.md) | "审查这段 FastAPI 代码的安全性" | 中书→门下→研发部+合规部 |
| [周报生成](examples/weekly-report.md) | "生成本周工程团队周报" | 中书→门下→财务+文档部 |

每个案例包含：完整任务 → 产品经理规划 → 质量审核审核意见 → 各部执行结果 → 最终报告。

---

## ⭐ Star History

如果这个项目让你会心一笑，请给个 Star ⚔️

[![Star History Chart](https://api.star-history.com/svg?repos=cft0808/edict&type=Date)](https://star-history.com/#cft0808/edict&Date)

---

## 📮 朕的邸报——公众号

> 古有邸报传天下政令，今有公众号聊 AI 架构。

<p align="center">
  <img src="docs/assets/wechat-qrcode.jpg" width="220" alt="公众号二维码 · cft0808">
  <br><br>
  <b>👆 扫码关注「cft0808」—— 朕的技术邸报</b>
</p>

你会看到：

- 🏛️ **架构拆解** —— 多Agent协作到底怎么分权制衡的？12 个 Agent 各司何职？
- 🔥 **踩坑复盘** —— Agent 吵架了怎么办？Token 烧光了怎么省？质量审核为什么总驳回？
- 🛠️ **Issue 修复实录** —— 每个 bug 都是一道报告，看朕如何批红
- 💡 **Token 省钱术** —— 用 1/10 的 token 跑出质量审核审核效果的秘密
- 🎭 **Agent 人设彩蛋** —— 六部的 SOUL.md 是怎么写出来的？

> *"朕让 AI 上朝，结果 AI 比朕还卷。"* —— 关注后你会懂的。

---

## 📄 License

[MIT](LICENSE) · 由 [OpenClaw](https://openclaw.ai) 社区构建

---

<p align="center">
  <strong>⚔️ 以古制御新技，以智慧驾驭 AI</strong><br>
  <sub>Governing AI with the wisdom of ancient empires</sub><br><br>
  <a href="#-朕的邸报公众号"><img src="https://img.shields.io/badge/公众号_cft0808-关注获取更新-07C160?style=for-the-badge&logo=wechat&logoColor=white" alt="WeChat"></a>
</p>
