# Claude Code Example

Use this prompt in Claude Code when you want the agent to integrate US Video API into an app:

```text
Integrate US Video API into this codebase.

Requirements:
- Read the API key from USVIDEOAPI_KEY.
- Create a helper that sends POST /v1/videos to https://usvideoapi.com.
- Add one example flow for a 9:16 ad-generation job.
- Handle polling GET /v1/videos/{id} until the job is complete.
- Keep the implementation production-friendly and easy to extend.
```

Recommended environment variable:

```text
USVIDEOAPI_KEY=...
```
