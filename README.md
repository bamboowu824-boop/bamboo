# wujinwu-resume-profile

自用 Cursor 履历 skill，顺带开源当模板：**远程仓库不传真实 `facts.md`**，只留下 `facts.example.md`；别人拷贝改名就能装。

---

## 别人怎么装进 Cursor

把整个文件夹放进下面任一目录；顶层文件夹的名字可以自定。

- **全局**：`%USERPROFILE%\.cursor\skills\wujinwu-resume-profile\`
- **单个项目**：`你的仓库根目录\.cursor\skills\自选技能名\`

放进去了还不顺手就试一下 Cursor 「Reload Window」。聊天里 `@SKILL.md` 或者说一声「按我简历 skill」写都行。

我只改 `facts.md` 作主源；Word 排版完再导出 PDF，别几处各改各的。

### 装好以后可以问哪些问题

前提是目录已经放进 `.cursor/skills/` 里，并且 **填好自己的 `facts.md`**。聊天时 `@SKILL.md` 或说一句「按简历 skill」即可。

表里「雨果网」「卓斯瑞」等是举例；你只要把段落名换成自己在 `facts.md` 里的小标题即可。

| 你可以这样问 | 一般会怎么答 |
| --- | --- |
| 根据 facts 写两分钟自我介绍，侧重售前一条路讲清楚 | 主线跟 facts 时间线对齐，动词具体；平常不把电话邮箱贴出来，除非你说了要导出简历 |
| 整段 JD 贴下面，从历史经历里挑出贴得上的，改成 bullet | 只写 facts 里有的；每项后简短对上 JD；对不上的不写、不圆谎 |
| 按 STAR 帮我准备追问：临时改需求 / 选型扯皮一类 | S-T-A-R 各一两句；客户名称模糊处理；facts 没有的数字不出现 |
| 雨果网那段压成投递用的三句，语气偏信息化统筹 | 仍围绕选型、交付、文档、培训、日常运维；不新造项目名或指标 |
| 卓斯瑞咨询经历压成一条，简历用，八十字内 | 访谈、报告、标书、述标等词与 facts 一致；控制字数 |
| 要投英文岗，给一段概括职业路径的 Rough line | 职位类型与公司经历与 facts 一致；学校公司没有官方英文名时等你确认再写备注 |

`facts` 还是空壳或示例时，Agent 应先让你补全再写，不要凭空编经历。

---

## 小白：从零把仓库挂到 GitHub

下面这些在 Windows 里能照着敲。先试终端 `git --version`，有输出再往下。

### 1. GitHub 账号

浏览器打开 github.com 注册邮箱。

### 2. 本机准备副本

把整个 skill 文件夹复制到一个专门给 Git 用的目录。

关键点：**真实履历写在 `facts.md`**；项目根的 `.gitignore` 默认忽略 `facts.md`，所以 **`git add .` 不会把它提交**。若 `git status` 里出现 `facts.md`，先检查 `.gitignore`，别 push 隐私。

换电脑别把 `facts.md` 指望在 GitHub 上找回；用隐私渠道拷走。

### 3. 第一次初始化

文件夹里 Shift + 右键打开 PowerShell：

```powershell
git init
git branch -M main
git add .
git status
```

确认待提交里没有 `facts.md`，再：

```powershell
git commit -m "chore: initial cursor resume skill template"
```

### 4. 网页上建仓

GitHub → New repository → 仓库名自定，例如 `resume-cursor-skill`。**不要勾选**「用模板生成 README」；本机若已有完整文件，网页上不必再生成一份。

建好记下 HTTPS，形如 `https://github.com/<你的用户名>/resume-cursor-skill.git`。

### 5. 推送

仍在本地仓库目录：

```powershell
git remote add origin https://github.com/<你的用户名>/resume-cursor-skill.git
git push -u origin main
```

第一次 `git push` 多半要用 **Personal Access Token**；GitHub 已不能用账号登录密码代替。路径：Settings → Developer settings → Personal access tokens → 新建后复制粘贴。

以后小改：

```powershell
git add .
git commit -m "docs: 更新 README"
git push
```

### 6. 别人怎么取用

克隆：`git clone https://github.com/<你的用户名>/resume-cursor-skill.git`

或直接 Download ZIP。

到手后：**复制 `facts.example.md` 改名为 `facts.md` 填空**，将整个目录搬进 `.cursor/skills/`。

---

## 文件一览

| 文件 | 说明 |
| --- | --- |
| SKILL.md | Agent 正文 |
| facts.md | 本人真实履历，仅存本地 |
| facts.example.md | 对外模板 |
| reference.md | STAR、自检 |
| examples.md | 句子风格示例 |
| voice.md | 语气：少套话 |
| CHANGELOG-PERSONAL.md | 自己改履历时的备忘 |
| PUBLISH.txt | 发朋友圈/ Release 可复制文案 |
| LICENSE | MIT |

Fork 后可改掉 SKILL 里姓名和 YAML 里的 `name:`。公开仓库别把 `facts.md` push 上去。

## 离线包说明

若在含中文路径的磁盘上解压出现乱码，可把 zip 解压到英文路径后再整体拷回原目录。

