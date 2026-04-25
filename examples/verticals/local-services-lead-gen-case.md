# Local Services Lead Gen Case

## Use Case

A local service business wants a short ad to drive calls, quote requests, or form fills.

## Recommended Brief

```json
{
  "industry": "local_services",
  "channel": "instagram",
  "goal": "drive quote requests",
  "audience": "homeowners in the service area",
  "brand_tone": "reliable, direct, local",
  "format": "video",
  "aspect_ratio": "9:16",
  "prompt": "Create a local services ad with trust, speed, and a clear quote CTA"
}
```

## Example API Request

```bash
curl -X POST "https://usvideoapi.com/v1/videos" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "seedance-1-pro",
    "prompt": "A 9:16 local services ad with before-and-after service visuals, reliability messaging, local trust cues, and a get-a-quote CTA.",
    "size": "1080p",
    "duration": 5
  }'
```

## Workflow Notes

- trust and locality matter more than brand flair
- show the service outcome clearly
- make the CTA immediate and action-oriented
