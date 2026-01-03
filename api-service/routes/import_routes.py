import traceback
from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models.image import Image
from services.google_drive_service import list_images, download_image
from storage import upload
from schemas import GoogleDriveImportRequest

router = APIRouter()

@router.post("/google-drive")
def import_google_drive_images(request: GoogleDriveImportRequest):
    print("🔥 IMPORT API HIT 🔥", flush=True)
    db = SessionLocal()

    try:
        folder_url = request.folder_url

        files = list_images(folder_url)
        if not files:
            return {"message": "No images found in folder"}

        response = []

        for file in files:
            image_bytes = download_image(file["id"])

            minio_url = upload(
                filename=file["name"],
                data=image_bytes,
                content_type=file["mimeType"]
            )

            image = Image(
                name=file["name"],
                google_drive_id=file["id"],
                size=int(file.get("size", 0)),
                mime_type=file["mimeType"],
                storage_path=minio_url
            )

            db.add(image)

            response.append({
                "name": image.name,
                "size": image.size,
                "mime_type": image.mime_type,
                "storage_path": image.storage_path
            })

        db.commit()
        return response

    except Exception as e:
        db.rollback()
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()
