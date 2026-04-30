# wujinwu-resume-ai-skill

将个人简历整理为结构化事实（`facts.json` / `facts.md`），配合支持 Agent Skills 或 MCP 的客户端：按岗位 JD 调整表述、撰写自述与 STAR，并尽量只引用 facts 中已有内容。

## 仓库内容

| 文件/目录 | 说明 |
| --- | --- |
| `SKILL.md` | 给模型的行为约束与流程 |
| `facts.json` | 结构化履历字段（公开仓库请使用 `facts.example.json`） |
| `facts.md` | 人读版履历，应与 JSON 同步维护 |
| `voice.md`、`reference.md`、`examples.md` | 语气、自检与句式示例 |
| `mcp/` | 可选本机 MCP（stdio），按需安装依赖 |

## 能力范围

- 按 JD 改写中文履历 bullet（不捏造 facts 中不存在的 KPI、证书、项目名称）
- 口述稿或求职材料提纲
- STAR 小故事拆解
- 与 facts 对照的自检

## 使用方法

### 作为 Skill 目录

将整个文件夹放进宿主文档指定的 skills 目录，在对话开始时让模型读取 `facts.json` 与 `SKILL.md`。

### 本地 MCP（stdio）

```bash
pip install -r mcp/requirements.txt
```

在宿主 MCP 配置中加入（将 `args` 改为本机的绝对路径）：

```json
{
  "mcpServers": {
    "wujinwu-resume": {
      "command": "python",
      "args": ["D:/你的路径/wujinwu-resume-profile/mcp/server.py"]
    }
  }
}
```

保存配置后重启宿主。

### 公网 MCP（HTTP）

若要对公网提供服务，请自行搭建域名、HTTPS、鉴权及流量治理；本仓库不提供托管 endpoint。

## 隐私与分发

- 不要将真实的 `facts.md`、`facts.json` 提交到公开仓库。
- `.gitignore` 默认忽略上述私密文件；每次 push 前用 `git status` 自检。

## 路径提示

在含中文路径的环境中若个别工具出现异常，可将目录临时移动到纯英文路径再操作。
