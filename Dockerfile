# Production Claw Worker for forge-code-refactor
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run test verification during build
RUN pytest tests/ -v

ENTRYPOINT ["python", "main.py", "--demo"]
