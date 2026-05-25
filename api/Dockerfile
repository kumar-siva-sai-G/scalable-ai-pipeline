# Stage 1: Build dependencies
FROM python:3.10-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Minimal runtime footprint
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY api/main.py .

ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000
# FIXED: Changed main.py:app to main:app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]