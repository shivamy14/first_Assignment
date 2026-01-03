from fastapi import APIRouter
from database import SessionLocal
from models.image import Image   # ✅ REQUIRED IMPORT

router = APIRouter()

@router.get("/")
def get_images():
    db = SessionLocal()
    try:
        images = db.query(Image).all()
        return images
    finally:
        db.close()
