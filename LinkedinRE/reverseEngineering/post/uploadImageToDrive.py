from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests
import os
import pickle

# Set up the OAuth 2.0 scope.
SCOPES = ['https://www.googleapis.com/auth/photoslibrary.appendonly']

def create_service():
    creds = None
    if os.path.exists('token_photoslibrary_v1.pickle'):
        with open('token_photoslibrary_v1.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'reverseEngineering/post/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token_photoslibrary_v1.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def upload_image(filepath):
    creds = create_service()
    headers = {
        'Authorization': 'Bearer ' + creds.token,
        'Content-type': 'application/octet-stream',
        'X-Goog-Upload-File-Name': os.path.basename(filepath),
        'X-Goog-Upload-Protocol': 'raw',
    }

    img_bytes = open(filepath, 'rb').read()
    upload_response = requests.post('https://photoslibrary.googleapis.com/v1/uploads', headers=headers, data=img_bytes)
    upload_token = upload_response.content.decode('utf-8')

    create_body = {
        'newMediaItems': [{'simpleMediaItem': {'uploadToken': upload_token}}]
    }
    create_response = requests.post('https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate', headers={'Content-type': 'application/json', 'Authorization': 'Bearer ' + creds.token}, json=create_body)
    if create_response.status_code != 200:
        print('Error creating media item: ' + create_response.content)
        return
    mediaItemId = create_response.json()['newMediaItemResults'][0]['mediaItem']['id']
    return mediaItemId

# Example usage
upload_image('reverseEngineering/post/black.jpeg')


def postImageToLinkdin():
    webhookUrl = 'https://api.linkedin.com/v2/ugcPosts'