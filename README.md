# Docker Python API

A small FastAPI service with validated endpoints and Docker configuration for containerized deployment.

**Problem → Solution → Result:** Lightweight calculation services still need validation, documentation, tests, and repeatable deployment. This API provides all four in a compact project that can be handed over and run consistently.

## Problem

Teams may need a simple HTTP service for health checks and reusable calculations, but an undocumented script is difficult to integrate and deploy reliably.

## Solution

The service exposes validated JSON endpoints, interactive OpenAPI documentation, automated tests, and a Docker Compose workflow.

## Features

- `GET /health` for service monitoring
- `GET /calculate?a=10&b=20` for addition
- `POST /statistics` for count, mean, minimum, and maximum
- Pydantic validation with standard FastAPI error responses
- Interactive documentation at `/docs`
- Tested local execution plus Docker and Compose configuration

## Tech Stack

Python 3.11+, FastAPI, Pydantic, Uvicorn, pytest, Docker

## Project Structure

```text
docker-python-api/
├── app/main.py
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Quick Start

Local development:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

Docker:

```bash
docker compose up --build
```

The application and endpoints have been tested locally. The Docker configuration has been statically reviewed but was not built on the validation machine because Docker was unavailable.

Open `http://localhost:8000/docs`. Run tests with `python -m pytest`.

## Example

```http
POST /statistics
Content-Type: application/json

{"values": [1, 2, 3, 4, 5]}
```

```json
{"count": 5, "mean": 3.0, "min": 1.0, "max": 5.0}
```

## Use Cases

- Containerized Python API delivery
- Health-check integration
- Small calculation or transformation services
- A starting point for internal business APIs

## Possible Extensions

- Authentication and request logging
- Additional domain-specific calculations
- CI checks and container publishing
