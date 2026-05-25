# Stage 1: Build dependencies (Corrected to uppercase AS)
FROM python:3.10-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Minimal runtime footprint
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY worker/worker.py .

ENV PATH=/root/.local/bin:$PATH
CMD ["python", "worker.py"]