# Medspa Offer Case

## Use Case

A medspa wants a short performance ad for a treatment offer or consultation funnel.

## Recommended Brief

```json
{
  "industry": "medspa",
  "channel": "instagram",
  "goal": "promote a limited-time treatment offer",
  "audience": "local beauty and wellness buyers",
  "brand_tone": "premium, clean, aspirational",
  "format": "video",
  "aspect_ratio": "9:16",
  "prompt": "Create a medspa offer ad with polished visuals and a clear consultation CTA"
}
```

## Example API Request

```bash
curl -X POST "https://usvideoapi.com/v1/videos" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "seedance-1-pro",
    "prompt": "A 9:16 medspa ad with polished clinic visuals, treatment atmosphere, benefit callouts, and a limited-time consultation CTA.",
    "size": "1080p",
    "duration": 5
  }'
```

## Workflow Notes

- keep the look premium and clean
- focus on confidence and outcome language
- end with a direct consultation CTA
