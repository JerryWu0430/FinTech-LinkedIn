import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import io
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.errors import HttpError
## firebase imports
import sys
sys.path.append("Firebase/")
import quotesDatabase 

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive"]


def init():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("contentCreation/quotes/token.json"):
        creds = Credentials.from_authorized_user_file(
            "contentCreation/quotes/token.json", SCOPES
        )
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "contentCreation/quotes/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("contentCreation/quotes/token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def get_file(creds):
    """
        Download the first file in the quotes folder that is not already in the database
        The path is always the same : contentCreation/quotes/quote.jpg
    """
    try:
        service = build("drive", "v3", credentials=creds)

        # Call the Drive v3 API
        ## search for quotes folder
        results = (
            service.files()
            .list(
                q="mimeType='application/vnd.google-apps.folder' and name='entrepreneurial quotes'",
                fields="files(id, name)",
            )
            .execute()
        )
        items = results.get("files", [])

        folder = items[0]
        ## get all files in quotes folder

        results = (
            service.files()
            .list(
                q=f"'{folder['id']}' in parents",
                fields="files(id, name)",
            )
            .execute()
        )
        items = results.get("files", [])
        print("Files:")
        for item in items:
            print(f"{item['name']} ({item['id']})")

        file_id = None
        while file_id == None:
            file_id = items[0]["id"]
            if quotesDatabase.isIn(file_id):
                file_id = None
                items.pop(0)
        
        print(f"File id: {file_id}")

        file = download_file(file_id, creds)
        print(file)
    except HttpError as error:
        print(f"An error occurred: {error}")
    

def download_file(real_file_id, creds, filePath="contentCreation/quotes/quote.jpg"):
    """Downloads a file
    Args:
      real_file_id: ID of the file to download
    Returns : IO object with location.

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
  

    try:
        # create drive api client
        service = build("drive", "v3", credentials=creds)

        file_id = real_file_id

        # pylint: disable=maybe-no-member
        request = service.files().get_media(fileId=file_id)
        with io.FileIO(filePath, mode='wb') as file:
            downloader = MediaIoBaseDownload(file, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(f"Download {int(status.progress() * 100)}%.")

        return True

    except Exception as error:
        print(f"An error occurred: {error}")
        return False




if __name__=="__main__":
   creds = init()
   get_files(creds)

