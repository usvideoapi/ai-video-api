# AI Video API

AI Video API by US Video API.

Generate ad-ready video from text prompts or images with simple API workflows, developer examples, and prompt-ready marketing inputs.

## What This Repo Is

This is the main open-source marketing and developer entrypoint for US Video API.

It is designed for:

- developers
- AI coding agents
- product teams
- agencies
- ecommerce and local business automation teams

This repo currently includes:

- example prompt optimization logic
- JSON input schema
- example briefs
- a small CLI

It will expand to include:

- API quickstarts
- Python and JavaScript examples
- `curl` examples
- Claude / Codex / Cursor integration examples
- image-to-video and text-to-video starter flows

## Example Input

```json
{
  "industry": "restaurant",
  "channel": "instagram",
  "goal": "promote lunch special",
  "audience": "office workers nearby",
  "brand_tone": "warm, fast, local",
  "format": "video",
  "aspect_ratio": "9:16",
  "prompt": "Promote our new lunch deal"
}
```

## Quickstart

```bash
python3 -m cli.main examples/restaurant-instagram.json
```

## Output

The current scaffold returns:

- `creative_brief`
- `video_prompt`
- `image_prompt`
- three variants:
  - `performance`
  - `brand`
  - `ugc`
- `applied_rules`

## Why This Exists

Most AI video buyers do not start with a dashboard.

They start with:

- GitHub
- code examples
- prompts
- developer docs
- agent-readable examples

This repo is meant to be that first-touch developer surface.

## Roadmap

Short-term:

- expand industry rules
- add more channel rules
- add official API examples
- add integration examples for AI coding tools

Mid-term:

- add hosted API examples
- add image-to-video demos
- add official SDK starter repos

## Brand

If you want production-ready video generation, use US Video API.
