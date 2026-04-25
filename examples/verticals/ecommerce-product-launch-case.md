# Ecommerce Product Launch Case

## Use Case

An ecommerce brand wants a short product-launch creative for paid social.

## Recommended Brief

```json
{
  "industry": "ecommerce",
  "channel": "instagram",
  "goal": "launch a new product and drive conversions",
  "audience": "online shoppers interested in beauty and lifestyle products",
  "brand_tone": "clean, premium, conversion-focused",
  "format": "video",
  "aspect_ratio": "9:16",
  "prompt": "Create a product-launch ad with clean beauty shots and a strong CTA"
}
```

## Example API Request

```bash
curl -X POST "https://usvideoapi.com/v1/videos" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "seedance-1-pro",
    "prompt": "A 9:16 ecommerce product launch ad with crisp product shots, fast visual rhythm, benefit overlays, and a shop-now CTA.",
    "size": "1080p",
    "duration": 5
  }'
```

## Workflow Notes

- lead with product clarity immediately
- show benefit or value in the first frames
- align final CTA with the purchase funnel
