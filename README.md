# wujinwu-resume-ai-skill

把个人简历做成可被通用 Agent / MCP 客户端读取的「结构化接口」，思路和「金谷园饺子馆开源 Skill」一致（见 [此文](https://mp.weixin.qq.com/s/lv69EEsxA_gUBLgucgyrKw)）。

## 01 · 有什么用

挂载到任意支持 Skills 目录或 MCP 的宿主（示例：OpenClaw、Codex CLI、国产 Agent IDE —— 以对应用具文档为准）后，你可以在对话里让模型撰写：

- JD 对齐的 bullet；
- 两分钟内口述稿；
- STAR 小故事；
并让模型读取 `facts.json` 避免胡编。

## 02 · 为什么做

等平台帮你总结前先占住一份 **AI 可读的官方履历**。换模型也只是换外壳，数据源不变。

## 03 · 安装

### A. Skill 本体

将整个目录放到对应产品的 **skills/** 根目录（不同客户端路径不同）；聊天时显式附上 `SKILL.md` 或要求模型读取 `facts.json`。

### B. MCP（stdio）

1. `pip install -r mcp/requirements.txt`
2. 在客户端 `mcpServers` 填入（改成你的磁盘路径）：

```json
{
  "mcpServers": {
    "wujinwu-resume": {
      "command": "python",
      "args": [
        "d:/海晟融创/参考/last/wujinwu-resume-profile/mcp/server.py"
      ]
    }
  }
}
```

3. 重启宿主。

### C. Streamable HTTP

与文中饺子馆范例一样可把 MCP 暴露在 HTTP——需自行运维和鉴权，本仓库不托管在线 URL。

## 隐私

远端 Git 请勿提交真实的 `facts.md` / `facts.json`（`.gitignore` 默认忽略）；公开仓库附带 `facts.example.*`。\n