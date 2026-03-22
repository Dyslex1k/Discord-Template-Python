# ── Stage 1: dependency builder ─────────────────────────────────────────────
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build tools only in this stage
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy and install dependencies into a local prefix (no venv needed)
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --prefix=/install --no-cache-dir -r requirements.txt

# Copy source + tests for validation in builder stage
COPY src/ /app/src/
COPY tests/ /app/tests/
WORKDIR /app/src

# Run tests in container build; fail fast if tests fail
RUN pip install pytest && pytest -q /app/tests


# ── Stage 2: final runtime image ─────────────────────────────────────────────
FROM python:3.12-slim AS runtime

# Security: run as non-root
RUN addgroup --system botgroup && adduser --system --ingroup botgroup botuser

WORKDIR /app

# Pull in only the installed packages from the builder
COPY --from=builder /install /usr/local

# Copy application source
COPY --chown=botuser:botgroup src/ .

USER botuser

# Disable .pyc files and enable unbuffered stdout for clean container logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

CMD ["python", "main.py"]
