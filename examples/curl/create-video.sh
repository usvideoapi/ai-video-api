#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${USVIDEOAPI_KEY:-}" ]]; then
  echo "Set USVIDEOAPI_KEY first." >&2
  exit 1
fi

curl -X POST "https://usvideoapi.com/v1/videos" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${USVIDEOAPI_KEY}" \
  -d '{
    "model": "seedance-1-pro",
    "prompt": "A polished 9:16 ecommerce ad for a skincare product with clean product beauty shots, quick benefit callouts, and a clear offer CTA.",
    "size": "1080p",
    "duration": 5
  }'
