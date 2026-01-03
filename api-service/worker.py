import time
from jobs import jobs

def process_import_job(job_id: str):
    # Step 1: processing
    jobs[job_id]["status"] = "processing"
    jobs[job_id]["message"] = "Import in progress"

    time.sleep(5)  # simulate heavy work (download + upload)

    # Step 2: completed
    jobs[job_id]["status"] = "completed"
    jobs[job_id]["message"] = "Import completed successfully"
