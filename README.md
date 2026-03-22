# Discord Bot — Python

A Discord bot built with **discord.py**, containerised with an optimised multi-stage Docker image.

## Stack

| Tool | Version |
|------|---------|
| Python | 3.12-slim |
| discord.py | 2.3.2 |
| Docker | multi-stage build |

## Project Structure

```
discord-bot-python/
├── bot.py               # Bot entry point
├── requirements.txt     # Python dependencies
├── Dockerfile           # Multi-stage optimised image
├── docker-compose.yml   # Compose config
├── .dockerignore
└── .env.example
```

## Getting Started

1. **Copy the env file and fill in your token:**
   ```bash
   cp .env.example .env
   ```

2. **Build and run with Docker Compose:**
   ```bash
   docker compose up -d --build
   ```

3. **View logs:**
   ```bash
   docker compose logs -f
   ```

4. **Stop the bot:**
   ```bash
   docker compose down
   ```

## Local Development (without Docker)

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # fill in your token
python bot.py
```

## Available Commands

| Command | Description |
|---------|-------------|
| `!ping` or `/ping` | Check bot latency |
| `!hello` or `/hello` | Greet the bot |

## Docker Optimisations

- **Multi-stage build** — build tools (gcc) are excluded from the final image
- **`python:3.12-slim`** base — minimal footprint
- **Non-root user** — runs as `botuser` for security
- **`PYTHONDONTWRITEBYTECODE=1`** — no `.pyc` clutter
- **`PYTHONUNBUFFERED=1`** — logs stream immediately
- **`.dockerignore`** — keeps build context lean
