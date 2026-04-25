# Dental Lead Gen Case

## Use Case

A dental clinic wants a vertical ad to drive consultation or whitening bookings.

## Recommended Brief

```json
{
  "industry": "dental",
  "channel": "instagram",
  "goal": "drive consultation bookings",
  "audience": "local adults seeking cosmetic or family dental care",
  "brand_tone": "clean, trustworthy, modern",
  "format": "video",
  "aspect_ratio": "9:16",
  "prompt": "Create a dental clinic ad focused on trust, clean visuals, and a booking CTA"
}
```

## Example API Request

```bash
curl -X POST "https://usvideoapi.com/v1/videos" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "seedance-1-pro",
    "prompt": "A 9:16 dental clinic ad with clean office visuals, smiling patient moments, clear treatment credibility, and a book-now CTA.",
    "size": "1080p",
    "duration": 5
  }'
```

## Workflow Notes

- lead with trust before offer
- keep visuals bright and professional
- use CTA language tied to consults or appointment booking
