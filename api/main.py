import uuid
import json
from fastapi import FastAPI, HTTPException
import redis

app = FastAPI(title="High-Throughput Ingestion API")

# 'redis-service' is the DNS name resolved inside Docker/Kubernetes networks
try:
    r = redis.Redis(host='redis-service', port=6379, db=0, decode_responses=True)
except Exception as e:
    print(f"Redis Connection Failed: {e}")

@app.post("/predict")
async def ingest_image(payload: dict):
    if not payload:
        raise HTTPException(status_code=400, detail="Invalid payload")
        
    job_id = str(uuid.uuid4())
    task_data = {
        "job_id": job_id,
        "image_url": payload.get("image_url", "default_mock_path.jpg"),
        "timestamp": payload.get("timestamp", "now")
    }
    
    # Push job to the tail of the Redis list (FIFO Queue)
    r.rpush("image_queue", json.dumps(task_data))
    
    return {
        "job_id": job_id,
        "status": "Accepted",
        "queue_depth": r.llen("image_queue")
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}