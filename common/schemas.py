from pydantic import BaseModel
from typing import List

class GoogleDriveImportRequest(BaseModel):
    folder_url: str

class ImageResponse(BaseModel):
    name: str
    google_drive_id: str
    size: int
    mime_type: str
    storage_path: str
