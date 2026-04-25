# JavaScript SDK

Minimal JavaScript client for US Video API.

## Example

```javascript
import { USVideoAPI } from "./index.mjs";

const client = new USVideoAPI({ apiKey: process.env.USVIDEOAPI_KEY });

const job = await client.createVideo({
  prompt: "A 9:16 restaurant ad with fast pacing and a lunch offer CTA."
});

const result = await client.waitForVideo(job.id);
console.log(result);
```
