import { USVideoAPI } from "../../sdk/javascript/index.mjs";

const client = new USVideoAPI({ apiKey: process.env.USVIDEOAPI_KEY });

const job = await client.createVideo({
  prompt:
    "A 9:16 salon ad with polished service shots, quick transformations, and a booking CTA.",
});

console.log("created", job);

const result = await client.waitForVideo(job.id, {
  pollIntervalMs: 5000,
  timeoutMs: 300000,
});

console.log("result", result);
