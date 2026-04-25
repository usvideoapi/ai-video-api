import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _load_rule(folder: str, key: str) -> dict:
    path = ROOT / "templates" / folder / f"{key}.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def optimize_brief(payload: dict) -> dict:
    industry = (payload.get("industry") or "").strip().lower()
    channel = (payload.get("channel") or "").strip().lower()
    goal = (payload.get("goal") or "").strip()
    audience = (payload.get("audience") or "").strip()
    brand_tone = (payload.get("brand_tone") or "").strip()
    fmt = (payload.get("format") or "video").strip().lower()
    aspect_ratio = (payload.get("aspect_ratio") or "").strip()
    prompt = (payload.get("prompt") or "").strip()

    industry_rule = _load_rule("industries", industry)
    channel_rule = _load_rule("channels", channel)

    applied_rules = []
    if industry_rule.get("tag"):
        applied_rules.append(industry_rule["tag"])
    if channel_rule.get("tag"):
        applied_rules.append(channel_rule["tag"])
    if fmt:
        applied_rules.append(f"format:{fmt}")
    if aspect_ratio:
        applied_rules.append(f"aspect:{aspect_ratio}")

    brief_parts = []
    if industry_rule.get("brief_rule"):
        brief_parts.append(industry_rule["brief_rule"])
    if channel_rule.get("brief_rule"):
        brief_parts.append(channel_rule["brief_rule"])
    if goal:
        brief_parts.append(f"Goal: {goal}.")
    if audience:
        brief_parts.append(f"Audience: {audience}.")
    if brand_tone:
        brief_parts.append(f"Brand tone: {brand_tone}.")

    creative_brief = " ".join(brief_parts).strip()

    video_parts = [prompt]
    if industry_rule.get("video_rule"):
        video_parts.append(industry_rule["video_rule"])
    if channel_rule.get("video_rule"):
        video_parts.append(channel_rule["video_rule"])
    if goal:
        video_parts.append(f"Keep the message focused on {goal}.")

    image_parts = [prompt]
    if industry_rule.get("image_rule"):
        image_parts.append(industry_rule["image_rule"])
    if channel_rule.get("image_rule"):
        image_parts.append(channel_rule["image_rule"])
    if goal:
        image_parts.append(f"Single-frame concept should clearly support {goal}.")

    video_prompt = " ".join(part for part in video_parts if part).strip()
    image_prompt = " ".join(part for part in image_parts if part).strip()

    return {
        "creative_brief": creative_brief,
        "video_prompt": video_prompt,
        "image_prompt": image_prompt,
        "variants": {
            "performance": f"{video_prompt} Optimize for direct response and conversion clarity.",
            "brand": f"{video_prompt} Keep the result premium, polished, and brand-led.",
            "ugc": f"{video_prompt} Keep the result more natural, native, and creator-style."
        },
        "applied_rules": applied_rules
    }
