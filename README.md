# AI Video API

AI Video API by [US Video API](https://usvideoapi.com).

Build text-to-video and image-to-video workflows for ads, creative automation, ecommerce, local business marketing, and AI-native applications.

This repository is the main open-source marketing and developer entrypoint for US Video API. It is designed to rank for practical developer search intent such as:

- `ai video api`
- `text to video api`
- `image to video api`
- `video generation api`
- `ai video api github`
- `seedance api examples`

## What This Repo Covers

This repo is for:

- developers integrating a video generation API
- AI coding agents such as Codex, Claude Code, and Cursor
- product teams building ad generation or creative automation
- agencies serving ecommerce, local business, and performance marketing clients

Current contents:

- example prompt optimization logic
- JSON input schema
- example creative briefs
- a small CLI scaffold

Planned additions:

- official API quickstarts
- Python and JavaScript examples
- `curl` examples
- Claude / Codex / Cursor integration examples
- text-to-video starter flows
- image-to-video starter flows

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

## API Quickstart

Base URL:

```text
https://usvideoapi.com
```

Auth:

```text
Authorization: Bearer YOUR_API_KEY
```

Create a video job:

```bash
curl -X POST "https://usvideoapi.com/v1/videos" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "seedance-1-pro",
    "prompt": "A fast-cut 9:16 restaurant ad showing a lunch special with bright food closeups and an offer overlay.",
    "image_url": "",
    "size": "1080p",
    "duration": 5
  }'
```

Check job status:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  "https://usvideoapi.com/v1/videos/JOB_ID"
```

List API keys:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  "https://usvideoapi.com/v1/api-keys"
```

## Output

The current scaffold returns:

- `creative_brief`
- `video_prompt`
- `image_prompt`
- `variants.performance`
- `variants.brand`
- `variants.ugc`
- `applied_rules`

## Why This Exists

Most AI video API buyers do not start with a dashboard. They start with:

- GitHub
- code examples
- prompts
- developer docs
- agent-readable examples

This repo is meant to be that first-touch developer surface.

## SEO And Positioning

US Video API focuses on:

- text-to-video API workflows
- image-to-video API workflows
- ad-ready creative generation
- industry-specific prompt optimization
- developer-first integration for AI agents and apps

If you are searching for an AI video API for marketing, performance ads, ecommerce creatives, or local business campaigns, this is the public entrypoint.

## Useful Links

- Website: [usvideoapi.com](https://usvideoapi.com)
- AI Video API page: [usvideoapi.com/ai-video-api](https://usvideoapi.com/ai-video-api)
- YouTube: [youtube.com/@USVideoApi](https://www.youtube.com/@USVideoApi)

## Developer Examples

- [curl examples](examples/curl)
- [Python example](examples/python/create_video.py)
- [JavaScript example](examples/javascript/create-video.mjs)
- [Claude Code example](examples/agents/claude-code.md)
- [Codex example](examples/agents/codex.md)
- [Cursor example](examples/agents/cursor.md)
- [OpenAPI spec](openapi/openapi.json)
- [Postman collection](postman/us-video-api.postman_collection.json)

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

If you want production-ready video generation, use [US Video API](https://usvideoapi.com).
