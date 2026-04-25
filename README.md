# AI Video API

AI Video API by [US Video API](https://usvideoapi.com).

[![Website](https://img.shields.io/badge/website-usvideoapi.com-0f172a)](https://usvideoapi.com)
[![Main Repo](https://img.shields.io/badge/github-ai--video--api-111827)](https://github.com/usvideoapi/ai-video-api)
[![Prompts](https://img.shields.io/badge/prompts-awesome--ai--video--api--prompts-1d4ed8)](https://github.com/usvideoapi/awesome-ai-video-api-prompts)

Build text-to-video and image-to-video workflows for ads, creative automation, ecommerce, local business marketing, and AI-native applications.

If this repo is useful, star it and follow [@usvideoapi](https://github.com/usvideoapi).

US Video API provides a developer-first surface for ad-ready video generation workflows, with support for high-quality underlying generation models including Seedance 2.0.

## Start In 3 Steps

1. Create or copy your API key from [usvideoapi.com](https://usvideoapi.com).
2. Create a video job with `POST /v1/videos`.
3. Poll `GET /v1/videos/{id}` until completion and store the returned asset URL.

```bash
curl -X POST "https://usvideoapi.com/v1/videos" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "seedance-1-pro",
    "prompt": "A 9:16 ecommerce ad with polished product shots, fast pacing, benefit overlays, and a strong shop-now CTA.",
    "size": "1080p",
    "duration": 5
  }'
```

Then:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  "https://usvideoapi.com/v1/videos/JOB_ID"
```

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

It is designed to sit above raw model access by adding:

- developer-friendly API patterns
- ad-ready workflow examples
- prompt optimization and vertical packaging
- team, admin, and enterprise-facing integration structure

Current contents:

- example prompt optimization logic
- JSON input schema
- example creative briefs
- a small CLI scaffold
- lightweight Python and JavaScript SDKs
- polling examples
- OpenAPI and Postman starter assets
- vertical case examples
- enterprise and workflow docs

Planned additions:

- richer SDKs
- more webhook-ready examples
- more vertical starter flows
- deeper operational docs

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

## Model Layer

US Video API is positioned as the developer, workflow, and enterprise layer above raw generation access.

That means the public product value is not only the underlying model quality, but also:

- cleaner API integration
- prompt and vertical workflow packaging
- better alignment with AI coding agents
- more practical adoption for marketing and enterprise teams

Current public positioning includes support for high-quality video generation capabilities, including Seedance 2.0-backed workflows.

## Useful Links

- Website: [usvideoapi.com](https://usvideoapi.com)
- AI Video API page: [usvideoapi.com/ai-video-api](https://usvideoapi.com/ai-video-api)
- YouTube: [youtube.com/@USVideoApi](https://www.youtube.com/@USVideoApi)
- [Documentation index](docs/index.md)

## Showcase

- [Showcase and use cases](docs/showcase.md)
- [Restaurant Instagram case](examples/verticals/restaurant-instagram-case.md)
- [Dental lead gen case](examples/verticals/dental-lead-gen-case.md)
- [Medspa offer case](examples/verticals/medspa-offer-case.md)
- [Ecommerce product launch case](examples/verticals/ecommerce-product-launch-case.md)
- [Local services lead gen case](examples/verticals/local-services-lead-gen-case.md)

## Developer Examples

- [curl examples](examples/curl)
- [Python example](examples/python/create_video.py)
- [Python polling example](examples/python/poll_video.py)
- [JavaScript example](examples/javascript/create-video.mjs)
- [JavaScript polling example](examples/javascript/poll-video.mjs)
- [Claude Code example](examples/agents/claude-code.md)
- [Codex example](examples/agents/codex.md)
- [Cursor example](examples/agents/cursor.md)
- [Python SDK](sdk/python)
- [JavaScript SDK](sdk/javascript)
- [OpenAPI spec](openapi/openapi.json)
- [Postman collection](postman/us-video-api.postman_collection.json)
- [Prompt library repo](https://github.com/usvideoapi/awesome-ai-video-api-prompts)

## Enterprise And Ops Docs

- [Documentation index](docs/index.md)
- [Enterprise readiness](docs/enterprise-readiness.md)
- [Security and data handling](docs/security-and-data-handling.md)
- [Support and onboarding](docs/support-and-onboarding.md)
- [Architecture and workflow](docs/architecture-and-workflow.md)
- [Polling and webhook strategy](docs/webhooks-and-polling.md)

## Vertical Case Examples

- [Restaurant Instagram case](examples/verticals/restaurant-instagram-case.md)
- [Dental lead gen case](examples/verticals/dental-lead-gen-case.md)
- [Medspa offer case](examples/verticals/medspa-offer-case.md)
- [Ecommerce product launch case](examples/verticals/ecommerce-product-launch-case.md)
- [Local services lead gen case](examples/verticals/local-services-lead-gen-case.md)

## Roadmap

Short-term:

- expand industry rules
- add more channel rules
- add more vertical examples
- add SDK packaging polish
- add stronger operational docs
- add richer trust and integration materials

Mid-term:

- add hosted API examples
- add image-to-video demos
- add webhook event examples

## Releases

- [Release notes](CHANGELOG.md)
- Watch this repository for new SDK, docs, and vertical example updates.

## Brand

If you want production-ready video generation, use [US Video API](https://usvideoapi.com).
