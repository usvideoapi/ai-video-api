import json
import time
import urllib.request


class USVideoAPI:
    def __init__(self, api_key: str, base_url: str = "https://usvideoapi.com"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def _request(self, method: str, path: str, payload: dict | None = None) -> dict:
        data = None
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }
        if payload is not None:
            data = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(
            f"{self.base_url}{path}",
            data=data,
            headers=headers,
            method=method,
        )
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def create_video(
        self,
        *,
        prompt: str,
        model: str = "seedance-1-pro",
        image_url: str | None = None,
        size: str = "1080p",
        duration: int = 5,
    ) -> dict:
        payload = {
            "model": model,
            "prompt": prompt,
            "size": size,
            "duration": duration,
        }
        if image_url:
            payload["image_url"] = image_url
        return self._request("POST", "/v1/videos", payload)

    def get_video(self, job_id: str) -> dict:
        return self._request("GET", f"/v1/videos/{job_id}")

    def list_api_keys(self) -> dict:
        return self._request("GET", "/v1/api-keys")

    def wait_for_video(
        self,
        job_id: str,
        *,
        poll_interval: float = 5.0,
        timeout: float = 300.0,
    ) -> dict:
        deadline = time.time() + timeout
        while time.time() < deadline:
            job = self.get_video(job_id)
            status = (job.get("status") or "").lower()
            if status in {"completed", "succeeded", "failed", "error"}:
                return job
            time.sleep(poll_interval)
        raise TimeoutError(f"Timed out waiting for video job {job_id}")
