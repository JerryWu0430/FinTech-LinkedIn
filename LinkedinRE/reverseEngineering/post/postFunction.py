import requests
import json

with open("reverseEngineering/LinkdIncookiesMain.json", "r") as file:
    cookies = json.loads(file.read())

headers = {
    "authority": "www.linkedin.com",
    "accept": "application/vnd.linkedin.normalized+json+2.1",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json; charset=UTF-8",
    "csrf-token": "ajax:1514152367892086323",
    "dnt": "1",
    "origin": "https://www.linkedin.com",
    "referer": "https://www.linkedin.com/feed/",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "x-li-lang": "fr_FR",
    "x-li-page-instance": "urn:li:page:d_flagship3_feed;jjJqhGFKR7+73Tu9PX/c1Q==",
    "x-li-pem-metadata": "Voyager - Feed - Posts=create-normshare",
    "x-li-track": '{"clientVersion":"1.13.8499","mpVersion":"1.13.8499","osName":"web","timezoneOffset":1,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    "x-restli-protocol-version": "2.0.0",
}


def post(text, fileTag=None, fileType=None, pageId=None):
    """
    FileType: 'IMAGE',
    fileTag : 'urn:li:digitalmediaAsset:D4E22AQEBNsL-q-MGxA'
    """

    json_data = {
        "visibleToConnectionsOnly": False,
        "externalAudienceProviders": [],
        "commentaryV2": {
            "text": text,
            "attributes": [],
        },
        "origin": "FEED",
        "allowedCommentersScope": "ALL",
        "postState": "PUBLISHED",
        "media": [],
    }
    if pageId != None:
        json_data["origin"] = "ORGANIZATION"
        json_data["dashNonMemberActor"] = "urn:li:fsd_company:" + str(pageId)
    if fileTag != None:
        print("We add the fileTag")
        json_data["media"].append(
            {
                "category": fileType,
                "mediaUrn": fileTag,
                "tapTargets": [],
                "altText": "",
            }
        )
    ##print(json_data)
    response = requests.post(
        "https://www.linkedin.com/voyager/api/contentcreation/normShares",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    if response.status_code==201:
        print("Post published")
    else:
        print("Post not published : ", response.status_code)
        print(response.text)


if __name__ == "__main__":
    post("Ceci est publié automatiquement", pageId="100470244")
