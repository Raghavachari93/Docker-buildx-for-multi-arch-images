This repo demonstrates how to build and publish **multi-architecture Docker images**
(using `linux/amd64` and `linux/arm64`) with **GitHub Actions** and **Docker buildx**.

## Image

Images are pushed to **GitHub Container Registry (GHCR)**:

- `ghcr.io/<OWNER>/docker-buildx-for-multi-arch-images:latest`

For your repo, that will be:

- `ghcr.io/Raghavachari93/docker-buildx-for-multi-arch-images:latest`

## Local build (optional)

```bash
docker build -t local-multi-arch-test .
docker run --rm -p 8000:8000 local-multi-arch-test
