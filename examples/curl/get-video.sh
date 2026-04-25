#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${USVIDEOAPI_KEY:-}" ]]; then
  echo "Set USVIDEOAPI_KEY first." >&2
  exit 1
fi

if [[ $# -ne 1 ]]; then
  echo "usage: $0 <job_id>" >&2
  exit 1
fi

curl -H "Authorization: Bearer ${USVIDEOAPI_KEY}" \
  "https://usvideoapi.com/v1/videos/$1"
