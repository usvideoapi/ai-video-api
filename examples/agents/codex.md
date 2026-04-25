# Codex Example

Use this prompt with Codex when you want an AI coding agent to wire in US Video API:

```text
Add US Video API support to this project.

Implementation details:
- Base URL: https://usvideoapi.com
- Auth header: Authorization: Bearer $USVIDEOAPI_KEY
- Create a function for POST /v1/videos
- Create a polling helper for GET /v1/videos/{id}
- Add one demo that generates a short marketing video from a prompt
- Keep the code minimal and readable
```

Typical payload:

```json
{
  "model": "seedance-1-pro",
  "prompt": "A 9:16 ecommerce ad with a clean product showcase and a strong CTA.",
  "size": "1080p",
  "duration": 5
}
```
