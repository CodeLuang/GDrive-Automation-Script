from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
from pathlib import Path
import logging
import glob

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def start():
    """
    Upload file-file sesuai pola ke Google Drive menggunakan service account.
    """
    
    SCOPES = ['https://www.googleapis.com/auth/drive.file'] 
    SERVICE_ACCOUNT_FILE = 'path/to/your-service-account-key.json'
    FOLDER_ID = 'your-google-drive-folder-id'

    paths = [
        "D:/backup/*.zip",
        "D:/backup/*.tar.gz",
    ]

    if not paths:
        logger.warning("Tidak ada pola file yang ditentukan. Backup dibatalkan.")
        return

    try:
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=SCOPES
        )
        service = build("drive", "v3", credentials=creds, cache_discovery=False)

        for pattern in paths:
            matched_files = glob.glob(pattern)
            if not matched_files:
                logger.info(f"Tidak ada file yang cocok dengan pola: {pattern}")
                continue

            for file_path in matched_files:
                fullpath = Path(file_path)
                if not fullpath.is_file():
                    logger.warning(f"Bukan file valid: {fullpath}")
                    continue

                file_metadata = {
                    'name': fullpath.name,
                    'parents': [FOLDER_ID]
                }
                media = MediaFileUpload(str(fullpath), resumable=True)

                request = service.files().create(
                    body=file_metadata,
                    media_body=media,
                    fields='id'
                )
                response = request.execute()

                if response and 'id' in response:
                    logger.info(f"Berhasil upload: {fullpath.name} (ID: {response['id']})")
                else:
                    logger.error(f"Gagal upload: {fullpath.name}")

    except Exception as e:
        logger.error(f"Error saat upload: {e}")
        raise
