# Cursor Example

Use this prompt in Cursor to scaffold a complete integration:

```text
Build a small US Video API client for this project.

Requirements:
- Use https://usvideoapi.com as the base URL
- Read auth from USVIDEOAPI_KEY
- Implement createVideo(payload)
- Implement getVideo(jobId)
- Add one example request for a 9:16 restaurant or ecommerce ad
- Keep the code easy for another AI agent to extend
```

Suggested follow-up:

```text
Now add retry handling, logging, and a webhook-ready abstraction around job status.
```
