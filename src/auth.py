from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account
from pathlib import Path
import logging
import glob


def start():
    # logging
    logging.basicConfig(level=logging.INFO)

    SCOPES = ['']
    SERVICE_ACCOUNT_FILE = ''
    FOLDER_ID = ''

    
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )
    
    service = build("drive", "v3", credentials=creds, cache_discovery=False)

    # full paths
    paths = [
        ""
    ]
    if paths:
        for uploading in range(len(paths)):
            path = glob.glob(paths[uploading])

            for i in path:
                fullpath = Path(i)

                file_metadata = {
                    'name': fullpath.name,
                    'parents': [FOLDER_ID]
                }
                file = MediaFileUpload(fullpath, resumable=True)

                res = service.files().create(
                    body=file_metadata,
                    media_body=file,
                    fields='id'
                ).execute()

                if res:
                    logging.info(f"{fullpath.name}")
                    print("file uploaded")
                else:
                    print("file failed to upload")

                print(file)
