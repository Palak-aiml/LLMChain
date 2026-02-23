# LLMChain Cloud Deployment Guide

## Docker
- Build: `docker build -t llmchain .`
- Run: `docker run -p 8000:8000 --env-file .env llmchain`

## Scaling
- Use Docker Compose, Kubernetes, or cloud services for scaling.

## Security
- Store secrets in environment variables or secret managers.
- Use HTTPS and authentication for production endpoints.

## Example Docker Compose
```yaml
version: '3'
services:
  llmchain:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
```
