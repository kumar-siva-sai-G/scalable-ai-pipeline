import time
import json
import redis

print("Worker engine initialized. Awaiting tasks...")
r = redis.Redis(host='redis-service', port=6379, db=0, decode_responses=True)

while True:
    # BLPOP (Blocking Left Pop) halts execution without consuming CPU cycles until an item exists
    job = r.blpop("image_queue", timeout=0)
    
    if job:
        queue_name, task_payload = job
        task = json.loads(task_payload)
        job_id = task.get("job_id")
        img_url = task.get("image_url")
        
        print(f"[START] Processing Job {job_id} for image: {img_url}")
        
        # Simulating heavy deep learning model execution latency (e.g., YOLO / PyTorch parsing)
        time.sleep(1.5)
        
        print(f"[SUCCESS] Finished Job {job_id}. Inference metadata stored.")