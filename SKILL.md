---
name: wujinwu-resume-ai-skill
description: >-
  提供吴金武的结构化履历事实（售前 / 招投标 / 信息化统筹 / 咨询驻场），供通用 AI Agent 写简历、求职信提纲与面试 STAR；禁止编造 facts 中不存在的信息。
  触发词：简历、CV、求职、投递、JD、自我介绍、STAR、售前、招投标、立项、解决方案、信息化、咨询、调研、投标。
---

# 吴金武 · 通用 AI 履历 Skill

先把履历拆成 **明确的规则 (`SKILL.md`) + 可查的数据 (`facts.*`)**，再给各类 Agent 读写：动笔前必须从 facts 取数；对外材料里没有的东西不要补。

## 读什么

1. `facts.json`：结构化字段，优先考虑。
2. `facts.md`：给人类快速浏览的长文本版（应保持与 JSON 对齐）。
3. 需要话术时再看 `voice.md`、`examples.md`、`reference.md`。

## 硬规矩

- 公司名 / 头衔 / 起止时间与 bullet，只能出自 facts；没有的字段发问，别猜。
- `not_claimable_without_confirmation` 中的条目在用户补充前视为不存在。
- 联系方式遵从 `facts.json.contact.sharing_policy`。

## MCP

可选：通过 `mcp/server.py` 在本机启用 **stdio MCP**，把结构化履历拆成小工具便于宿主调用。若要在公网上以 HTTP/S 提供服务，自建域名与 TLS，并做好鉴权；本仓库不内置任何公网地址。