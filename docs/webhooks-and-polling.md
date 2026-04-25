# Polling And Webhook Strategy

US Video API currently exposes an async job pattern that is easy to integrate with polling.

## Polling

Recommended loop:

1. `POST /v1/videos`
2. capture the returned job ID
3. poll `GET /v1/videos/{id}`
4. stop when the status becomes terminal

Terminal states should be treated as:

- `completed` or `succeeded`
- `failed` or `error`

See:

- [Python polling example](../examples/python/poll_video.py)
- [JavaScript polling example](../examples/javascript/poll-video.mjs)

## Webhook-Ready Design

Even if your first integration uses polling, keep your internal architecture webhook-ready:

- persist `job_id`
- persist your own `external_ref`
- separate job creation from job completion handling
- make downstream processing idempotent

This makes it easy to adopt a future webhook event surface later without refactoring your whole system.
