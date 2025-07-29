# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]

# docker-compose.yml
version: '3.8'
services:
  agent:
    build: .
    environment:
      - API_KEY=${API_KEY}
    volumes:
      - .:/app
    depends_on:
      - redis
  redis:
    image: redis:6-alpine
    ports:
      - "6379:6379"
