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
- YouTube: [youtube.com/@USVideoApi](https://www.youtube.com/@USVideoApi)

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
