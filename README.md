# wujinwu-resume-profile

我把个人简历整理成可被对话式 Agent 读取的协作入口：根目录 **`SKILL.md`** 约定回答规则与文风，**`facts.md`** 或 **`facts.json`** 是事实底稿。公开库里只保留 **`facts.example.md` / `facts.example.json`** 作模板；真实履历放在本地填空，且不提交远程，以免隐私进 Git。

它不绑定某一种 IDE。常见用法有三种，按你手头工具选其一即可：**把仓库交给 Agent 当技能目录读**（若你的产品支持）；**挂载本仓库自带的 MCP**（需要客户端支持 MCP）；或 **直接在对话里贴路径 / 指明先读哪些文件**。下面分节写明。

可选 **Cursor**：若你使用该编辑器，可把本目录拷进 `.cursor/skills/`，等价于多了一份「可被 @ 的技能说明」——仅为其中一种挂载方式示例。

---

## 怎么使用这份skill

将整个仓库克隆或解压到本机任选路径；顶层文件夹的名字可以自定。

### 任意 Agent / 会话助手

在对话里说清：**先读取本仓库根目录下的 `SKILL.md`，再按需读取与你维护者一致的 `facts.md` 或 **`facts.example.*`（公开仓库仅能看示例模板）**。需要写法参考时可读 `reference.md`、`examples.md`，语气可查 `voice.md`。

只要客户端能对文件做读取或把整个目录并进上下文即可，不一定要装某个插件。

### 支持「技能目录」的客户端（含 Cursor）

若文档写明了技能要放在固定目录：**把整个仓库文件夹放进那家产品规定的位置**。以 Cursor 为例，常见路径任选其一：

- **全局**：`%USERPROFILE%\.cursor\skills\wujinwu-resume-profile\`
- **单项目**：`你的项目根\.cursor\skills\自选技能名\`

挂载后若不生效，试一下该编辑器里的 **Reload Window**，或在对话里 **`@SKILL.md`**／说明「按本仓库履历 skill」即可。

我只改本地的 `facts.md` / `facts.json`；Word 排完版再导出 PDF，别几处各改各的。

### 装好以后可以问哪些问题

前提是：**Agent 已能访问这份仓库（或你已把技能说明与 facts 并入上下文）**，并且你已 **填好自己的 `facts.md`** 或结构化 **`facts.json`**。若仅用公开仓库，则只能就着示例模板核对约定，拿不到维护者私密履历全文。

下表举例里的「第一段经历」「上一份内部 IT」「驻场咨询段」等表述，都应换成 **`facts.md`（或 JSON）里你自己写的小标题 / 条目顺序**，不要凭空猜公司名字。

| 你可以这样问 | 一般会怎么答 |
| --- | --- |
| 根据 facts 写两分钟自我介绍，侧重售前一条路讲清楚 | 主线跟 facts 时间线对齐，动词具体；平常不把电话邮箱贴出来，除非你说了要导出简历 |
| 整段 JD 贴下面，从历史经历里挑出贴得上的，改成 bullet | 只写 facts 里有的；每项后简短对上 JD；对不上的不写、不圆谎 |
| 按 STAR 帮我准备追问：临时改需求 / 选型扯皮一类 | S-T-A-R 各一两句；客户名称模糊处理；facts 没有的数字不出现 |
| 把 facts 里偏内部 IT／信息化统筹的那一段压成三句，投递用 | 仍围绕选型、交付、文档、培训、日常运维；不新造项目名或指标 |
| 把 facts 里偏咨询与投标的那段压成一条，简历用，八十字内 | 访谈、报告、标书、述标等词与 facts 一致；控制字数 |
| 要投英文岗，给一段概括职业路径的 Rough line | 职位类型与公司经历与 facts 一致；学校公司没有官方英文名时等你确认再写备注 |

`facts` 仍是空壳或仅占位示例时，Agent 应先让你补全事实再写，不要凭空编经历。

### MCP（可选）

本仓库 **`mcp/`** 内提供基于 **FastMCP** 的 **stdio MCP** 服务（工具名形如 `resume_meta`、`resume_experience` 等）。使用前在本机准备好 **`facts.json`**：复制 **`facts.example.json`** 改名为 `facts.json` 并按字段填空。随后在支持 MCP 的客户端里，把服务器入口指向该项目说明里的启动命令即可；具体接线以你那款客户端的设置为准。

`facts.json` 与 `facts.md` 是否要同步维护由你自己约定；公开仓库请勿提交包含隐私的 **`facts.json`**。

---

## 文件一览

| 文件 | 说明 |
| --- | --- |
| SKILL.md | Agent 正文 |
| facts.md | 本人真实履历，仅存本地 |
| facts.example.md / .json | 对外模板 |
| mcp/ | 可选：stdio MCP，从 `facts.json` 暴露字段 |
| reference.md | STAR、自检 |
| examples.md | 句子风格示例 |
| voice.md | 语气：少套话 |
| CHANGELOG-PERSONAL.md | 自己改履历时的备忘 |
| LICENSE | MIT |

Fork 后可改掉 SKILL 里姓名和 YAML 里的 `name:`。公开仓库别把 `facts.md` 或含隐私的 `facts.json` push 上去。

## 离线包说明

若在含中文路径的磁盘上解压出现乱码，可把 zip 解压到英文路径后再整体拷回原目录。
