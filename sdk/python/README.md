# Python SDK

Minimal Python client for US Video API.

## Example

```python
from usvideoapi import USVideoAPI

client = USVideoAPI(api_key="YOUR_API_KEY")

job = client.create_video(
    prompt="A 9:16 ecommerce ad with strong product focus and a clear CTA."
)

result = client.wait_for_video(job["id"])
print(result)
```
