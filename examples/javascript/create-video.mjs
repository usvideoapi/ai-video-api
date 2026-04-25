const apiKey = process.env.USVIDEOAPI_KEY;
const baseUrl = process.env.USVIDEOAPI_BASE_URL || "https://usvideoapi.com";

if (!apiKey) {
  throw new Error("Set USVIDEOAPI_KEY first.");
}

const payload = {
  model: "seedance-1-pro",
  prompt:
    "A 9:16 ad for a dental clinic with clean office visuals, smiling patient moments, trust-building text overlays, and a booking CTA.",
  size: "1080p",
  duration: 5,
};

const response = await fetch(`${baseUrl}/v1/videos`, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify(payload),
});

console.log(await response.text());
