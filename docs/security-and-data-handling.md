# Security And Data Handling

This page is meant to answer the first practical questions enterprise and agency buyers usually ask on first review.

## Core Security Posture

US Video API uses a standard HTTPS API model with bearer-token authentication.

Recommended customer-side practices:

- keep API keys server-side
- do not expose production keys in client-side JavaScript
- use separate keys for testing and production workflows
- log requests and job IDs in your own system
- rotate keys when team membership or deployment boundaries change

## Data Handling Model

Typical integration data includes:

- prompts
- image URLs for image-to-video workflows
- job IDs
- job status values
- output asset URLs

Recommended customer-side handling:

- store prompts and job records in your own system of record
- treat prompt history as business data
- avoid putting unnecessary secrets into prompts
- keep downstream asset retention aligned with your own policy requirements

## Enterprise Integration Guidance

For enterprise or agency workflows, the standard shape should be:

1. your app calls `POST /v1/videos`
2. your system stores the returned job ID
3. your backend polls `GET /v1/videos/{id}`
4. your app stores final asset URLs and downstream metadata

This gives you clean auditability for:

- who requested generation
- what prompt was used
- which job ID maps to which internal request
- which final asset was delivered downstream

## Access And Operational Discipline

Recommended operating model:

- keep production API calls on the server side
- use environment-based separation between staging and production
- centralize key ownership
- log job creation and result retrieval
- limit internal access to production credentials

## Public Trust Surface

Current public review surface includes:

- website: `https://usvideoapi.com`
- API page: `https://usvideoapi.com/ai-video-api`
- GitHub repo: `https://github.com/usvideoapi/ai-video-api`
- YouTube: `https://www.youtube.com/@USVideoApi`

## Scope Note

This public repository is the developer-facing trust surface, not a full legal or procurement packet. It is meant to show:

- how integration works
- how to structure secure usage
- how to reason about prompt, job, and asset handling
