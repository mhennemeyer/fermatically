# ── Build-Stage ──────────────────────────────────────────────
FROM python:3.12-slim AS build

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdocs build --strict

# ── Runtime-Stage ────────────────────────────────────────────
FROM nginx:alpine

COPY --from=build /app/site /usr/share/nginx/html

EXPOSE 80
