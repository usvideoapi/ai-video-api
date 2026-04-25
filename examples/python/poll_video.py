import os

from sdk.python.usvideoapi import USVideoAPI


client = USVideoAPI(api_key=os.environ["USVIDEOAPI_KEY"])

job = client.create_video(
    prompt="A 9:16 medspa ad with before/after framing, benefit callouts, and a consultation CTA."
)
print("created", job)

result = client.wait_for_video(job["id"], poll_interval=5, timeout=300)
print("result", result)
