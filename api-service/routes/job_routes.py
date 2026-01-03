from fastapi import APIRouter, HTTPException
from jobs import jobs

router = APIRouter()

@router.get("/{job_id}")
def get_job_status(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    return {
        "job_id": job_id,
        "status": jobs[job_id]["status"],
        "message": jobs[job_id]["message"]
    }
