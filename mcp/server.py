# -*- coding: utf-8 -*-
from __future__ import annotations

import json
from pathlib import Path

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "facts.json"
app = FastMCP("wujinwu-resume")


def _load() -> dict:
    if not DATA.exists():
        raise FileNotFoundError("缺少 facts.json：复制 facts.example.json 后填写。")
    return json.loads(DATA.read_text(encoding="utf-8"))


@app.tool()
def resume_meta() -> str:
    return json.dumps(_load().get("meta", {}), ensure_ascii=False, indent=2)


@app.tool()
def resume_capabilities() -> str:
    return json.dumps(_load().get("capabilities_for_clients", []), ensure_ascii=False, indent=2)


@app.tool()
def resume_experience() -> str:
    return json.dumps(_load().get("experience", []), ensure_ascii=False, indent=2)


@app.tool()
def resume_education() -> str:
    return json.dumps(_load().get("education", []), ensure_ascii=False, indent=2)


@app.tool()
def resume_constraints() -> str:
    loaded = _load()
    payload = {
        "not_claimable": loaded.get("not_claimable_without_confirmation", []),
        "sharing_policy": loaded.get("contact", {}).get("sharing_policy", ""),
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


@app.tool()
def resume_contact(include_phone_email: bool = False) -> str:
    contact = dict(_load().get("contact", {}))
    policy = contact.pop("sharing_policy", None)
    if not include_phone_email:
        minimal = {
            "address": contact.get("address", ""),
            "sharing_policy": policy,
            "_note": "手机号/邮箱默认隐藏；生成简历前请用户同意并传 include_phone_email=true",
        }
        return json.dumps(minimal, ensure_ascii=False, indent=2)
    if policy:
        contact["sharing_policy"] = policy
    return json.dumps(contact, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    app.run(transport="stdio")
