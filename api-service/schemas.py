from pydantic import BaseModel
from typing import List
from typing import Optional

# ===== REQUEST =====
class GoogleDriveImportRequest(BaseModel):
    folder_url: str

# ===== RESPONSE =====
class ImageMeta(BaseModel):
    name: str
    google_drive_id: str
    size: int
    mime_type: str
    storage_path: str


class GoogleDriveImportResponse(BaseModel):
    imported_images: int
    images: List[ImageMeta]
