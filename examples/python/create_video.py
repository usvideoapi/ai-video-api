import json
import os
import urllib.request


API_KEY = os.environ["USVIDEOAPI_KEY"]
BASE_URL = os.environ.get("USVIDEOAPI_BASE_URL", "https://usvideoapi.com")

payload = {
    "model": "seedance-1-pro",
    "prompt": (
        "A 9:16 local restaurant ad showing a lunch combo, close-up food shots, "
        "quick pacing, and a final offer CTA."
    ),
    "size": "1080p",
    "duration": 5,
}

req = urllib.request.Request(
    f"{BASE_URL}/v1/videos",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    },
    method="POST",
)

with urllib.request.urlopen(req) as resp:
    print(resp.read().decode("utf-8"))
