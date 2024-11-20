import requests
import json

with open("reverseEngineering/linkedinCookiesMain.json", "r") as f:
    cookies = json.load(f)

headers = {
    "accept": "application/vnd.linkedin.normalized+json+2.1",
    "accept-language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
    "csrf-token": "ajax:5870874727930491173",
    "dnt": "1",
    "priority": "u=1, i",
    "referer": "https://www.linkedin.com/in/c-samuel-mosher-52a2a1a/",
    "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
    "x-li-lang": "fr_FR",
    "x-li-page-instance": "urn:li:page:d_flagship3_profile_view_base_contact_details;aK/OIo1xT/+EQESvvONZYw==",
    "x-li-track": '{"clientVersion":"1.13.15893","mpVersion":"1.13.15893","osName":"web","timezoneOffset":-5,"timezone":"America/Bogota","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    "x-restli-protocol-version": "2.0.0",
}

response = requests.get(
    "https://www.linkedin.com/voyager/api/graphql?includeWebMetadata=true&variables=(memberIdentity:c-samuel-mosher-52a2a1a)&queryId=voyagerIdentityDashProfiles.5a6722404e6afd08958f5105e51cad51",
    cookies=cookies,
    headers=headers,
)

print(response.status_code)
print(json.dumps(response.json(), indent=4))
