export class USVideoAPI {
  constructor({ apiKey, baseUrl = "https://usvideoapi.com" }) {
    this.apiKey = apiKey;
    this.baseUrl = baseUrl.replace(/\/$/, "");
  }

  async request(path, { method = "GET", body } = {}) {
    const response = await fetch(`${this.baseUrl}${path}`, {
      method,
      headers: {
        Authorization: `Bearer ${this.apiKey}`,
        ...(body ? { "Content-Type": "application/json" } : {}),
      },
      ...(body ? { body: JSON.stringify(body) } : {}),
    });
    return response.json();
  }

  async createVideo({
    prompt,
    model = "seedance-1-pro",
    image_url,
    size = "1080p",
    duration = 5,
  }) {
    const payload = { prompt, model, size, duration };
    if (image_url) {
      payload.image_url = image_url;
    }
    return this.request("/v1/videos", { method: "POST", body: payload });
  }

  async getVideo(jobId) {
    return this.request(`/v1/videos/${jobId}`);
  }

  async listApiKeys() {
    return this.request("/v1/api-keys");
  }

  async waitForVideo(jobId, { pollIntervalMs = 5000, timeoutMs = 300000 } = {}) {
    const deadline = Date.now() + timeoutMs;
    while (Date.now() < deadline) {
      const job = await this.getVideo(jobId);
      const status = (job.status || "").toLowerCase();
      if (["completed", "succeeded", "failed", "error"].includes(status)) {
        return job;
      }
      await new Promise((resolve) => setTimeout(resolve, pollIntervalMs));
    }
    throw new Error(`Timed out waiting for video job ${jobId}`);
  }
}
