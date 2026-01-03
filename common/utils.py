import re
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

# Absolute path inside Docker container
SERVICE_ACCOUNT_FILE = "/worker/service_account.json"

def get_drive_service():
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        raise FileNotFoundError(
            f"Service account file not found at {SERVICE_ACCOUNT_FILE}"
        )

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )

    return build("drive", "v3", credentials=creds)


def extract_folder_id(folder_url: str) -> str:
    match = re.search(r"/folders/([a-zA-Z0-9_-]+)", folder_url)
    if not match:
        raise ValueError("Invalid Google Drive folder URL")
    return match.group(1)
