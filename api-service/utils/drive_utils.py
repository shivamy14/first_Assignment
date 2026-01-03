import re

def extract_folder_id(folder_url: str) -> str:
    """
    Safely extract Google Drive folder ID from a folder URL
    """
    pattern = r"folders/([a-zA-Z0-9_-]+)"
    match = re.search(pattern, folder_url)

    if not match:
        raise ValueError("Invalid Google Drive folder URL")

    return match.group(1)
