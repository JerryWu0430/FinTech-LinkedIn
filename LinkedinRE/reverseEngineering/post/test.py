
import requests
import base64
import uploadImageToDrive 



def postMake(imageId):
    url = "https://hook.eu2.make.com/vqugj2drxo34ee813217t6jdbbcm5vsr"


# JSON payload including the base64-encoded image
    payload = {
        'ImageID': imageId,
        'Content': 'Salut'
    }

    # Send the payload via POST request to the webhook endpoint
    response = requests.post(url, data=payload)

    # Check the response status
    if response.status_code == 200:
        print('Image sent successfully via webhook')
    else:
        print('Failed to send image via webhook:', response.status_code)

if __name__ == "__main__":
    imageId = uploadImageToDrive.upload_image('reverseEngineering/post/black.jpeg')
    postMake(imageId)
