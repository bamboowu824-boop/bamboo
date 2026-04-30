---
name: wujinwu-resume-ai-skill
description: >-
  提供吴金武的结构化履历事实（售前 / 招投标 / 信息化统筹 / 咨询驻场），供通用 AI Agent 写简历、求职信提纲与面试 STAR；禁止编造 facts 中不存在的信息。
  触发词：简历、CV、求职、投递、JD、自我介绍、STAR、售前、招投标、立项、解决方案、信息化、咨询、调研、投标。
---

# 吴金武 · 通用 AI 履历 Skill

思路对齐那篇「饺子馆把店面信息开源成 Skill」：**不是给顾客用的 App**，而是给各类助手一份可核验的个人事实接口。原文讨论餐厅与 MCP；我这里换成简历数据层。[微信文章](https://mp.weixin.qq.com/s/lv69EEsxA_gUBLgucgyrKw)

## 读什么

1. `facts.json`：结构化字段，优先考虑。
2. `facts.md`：给人类快速浏览的长文本版（应保持与 JSON 对齐）。
3. 需要话术时再看 `voice.md`、`examples.md`、`reference.md`。

## 硬规矩

- 公司名 / 头衔 / 起止时间与 bullet，只能出自 facts；没有的字段发问，别猜。
- `not_claimable_without_confirmation` 中的条目在用户补充前视为不存在。
- 联系方式遵从 `facts.json.contact.sharing_policy`。

## MCP

本仓库在 `mcp/server.py` 提供 **stdio MCP**（本地进程）。要像文章那样挂 **streamable-http** 远端端点：需要自备域名/TLS/鉴权，可自行把 `FastMCP.run(transport=...)` 接到网关；本仓库不内置公网 URL。\n