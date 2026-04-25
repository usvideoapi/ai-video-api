# Restaurant Instagram Case

## Use Case

A local restaurant wants a short 9:16 ad for Instagram Reels or Stories to promote a lunch special.

## Recommended Brief

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

## Example API Request

```bash
curl -X POST "https://usvideoapi.com/v1/videos" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "seedance-1-pro",
    "prompt": "A 9:16 restaurant ad with close-up food shots, lunch combo pricing, fast pacing, and a clear visit-now CTA.",
    "size": "1080p",
    "duration": 5
  }'
```

## Workflow Notes

- keep the first second visually strong
- prioritize food detail and offer clarity
- use a short CTA focused on visit or order behavior
