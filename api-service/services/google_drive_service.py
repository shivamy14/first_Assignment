from io import BytesIO
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
from googleapiclient.discovery import build
import re
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "service_account.json")

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


def extract_folder_id(folder_url_or_id: str) -> str:
    # If already a folder ID
    if re.fullmatch(r"[a-zA-Z0-9_-]{10,}", folder_url_or_id):
        return folder_url_or_id

    match = re.search(r"/folders/([a-zA-Z0-9_-]+)", folder_url_or_id)
    if not match:
        raise ValueError("Invalid Google Drive folder URL")

    return match.group(1)


def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH,
        scopes=SCOPES,
    )
    return build("drive", "v3", credentials=creds)


def list_images(folder_input: str):
    folder_id = extract_folder_id(folder_input)
    service = get_drive_service()

    files = []
    page_token = None

    while True:
        response = service.files().list(
            q=f"'{folder_id}' in parents and mimeType contains 'image/'",
            fields="nextPageToken, files(id, name, mimeType, size)",
            pageToken=page_token,
            pageSize=100
        ).execute()

        files.extend(response.get("files", []))
        page_token = response.get("nextPageToken")

        if not page_token:
            break

    return files


def download_image(file_id: str) -> bytes:
    service = get_drive_service()
    request = service.files().get_media(fileId=file_id)

    fh = BytesIO()
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        _, done = downloader.next_chunk()

    fh.seek(0)
    return fh.read()
