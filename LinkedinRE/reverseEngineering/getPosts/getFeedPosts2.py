import requests
import logging
import re
import json

with open("reverseEngineering/LinkdIncookiesMain.json", "r") as f:
    cookies = json.load(f)

headers = {
    'accept': 'application/vnd.linkedin.normalized+json+2.1',
    'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7',
    'content-type': 'application/json; charset=UTF-8',
    # 'cookie': 'bcookie="v=2&7c2b59b6-f361-4371-851b-19a77d664e7f"; bscookie="v=1&2024052810215410a69698-ab4c-4c4b-841e-29655cc89207AQHNddsvXJg4yavZGorLWHqziNbafbfZ"; li_gc=MTswOzE3MTY4OTE3MTQ7MjswMjHWvMjcoJZXKAbA+vnM9U/WMgdOcdhD3+/u9gqijFuh7Q==; li_alerts=e30=; liap=true; JSESSIONID="ajax:8605260549462175672"; timezone=Europe/Paris; li_theme=light; li_theme_set=app; dfpfpt=cca0d274cb7a43b4867f281b6211a6c7; li_sugr=fe6626e7-d0f0-488b-b42c-6e16a0baf37c; __ssid=a5e44fb7-4873-4e56-b5c0-6d617117724e; liveagent_oref=https://www.linkedin.com/campaignmanager/accounts; liveagent_vc=1; li_at=AQEDATnsHuUCMLYWAAABj8U0MMIAAAGQefxTaU4A0iL94OrGarwlw01rVYc-bDq_AkdLn9MU8HJBUvsagPvVdqQ850Ag3wjdiIY_EHT43w1-KisjCwHjLzW_EFHYgtOXE5vf6DTcLeLpWIxNWBsGXycU; li_mc=MTsyMTsxNzIwMDEwMTI4OzI7MDIxNBjMaCluo90zDJWxsPcq3jzaASJMq+z2eDwO3Rs0vXE=; lidc="b=TB17:s=T:r=T:a=T:p=T:g=16432:u=180:x=1:i=1720010128:t=1720079609:v=2:sig=AQFmYHMd-FYI_Oaw1-TONZ9A96F9rZ6V"; lang=v=2&lang=fr-fr; UserMatchHistory=AQJzPe44Z7HbPAAAAZB4l_l6jNI9Ad-MveaGPlskvmL71YR9UUqG_uSiP9evVo4TU-pqCdHC0Katq2Rzn5VtbxhSpGyKyp0khh2HR4w69WuXrKMPWWdtwOEzptqpbo5uxDuB1uRHzw5xbuKugHjyk5KWIdosH4Mh0mQLjVK5wKMm2RNIcO9rB1uI2Z4jHhvVs-QI4xtaLDFEKSGcY-hywVfE9FX6uYNyoOsEsFtKuJPXsBS_PuplqRWrQTlut2GPyZmKDyNBB_mVrQszVIGiPRZbhaD71i2es9u2B1fOfjMrMFBpXZiR3E2DQcrtCtiAhTyrE2i2AXAE8bdzfus8181mbvsP9LvHapu4AX7O8yg_dMvYEw; fptctx2=taBcrIH61PuCVH7eNCyH0Iitb%252bEMfwlgK%252fM8w%252f28EbdFmrion%252b7g%252blQK4HVUXVzxx07fqyKR7mPLLcNwptIetaV3wk%252bLTvy2nryCRreevOoaRZQjZ%252bniRgc152L2xl61RMT2E1hFMpXLTN%252fxjEdPH421i%252fToYZZFVj6%252fpauNz5p5gzshqDqf6YX7qkGzbsecYBAzN4rFPG54JyX3Eg%252fcJSqVLa13zOjsdnCDHWt07Djl3d8gDokBFZVRwkH0mUm1tPCbB329XP2jkTABnWQFXOs%252bSzO2G2dH2IPvdB2iNSseutR%252b5jYsi1ZjLCVsPUkcxgLtedlNkVXKcWukpGPxJ5kzNI1u3TrF4dUIEspvhTs%253d',
    'csrf-token': 'ajax:1514152367892086323',
    'dnt': '1',
    'origin': 'https://www.linkedin.com',
    'priority': 'u=1, i',
    'referer': 'https://www.linkedin.com/feed/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
    'x-li-lang': 'fr_FR',
    'x-li-page-instance': 'urn:li:page:d_flagship3_feed;fl8soo6wQTeFh/spdHfGJA==',
    'x-li-track': '{"clientVersion":"1.13.19196","mpVersion":"1.13.19196","osName":"web","timezoneOffset":2,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    'x-restli-protocol-version': '2.0.0',
}



def getPosts(count, cookies=cookies, headersToHappen=None):
    if headersToHappen:
        for key, value in headersToHappen.items():
            headers[key] = value
    print(headers["csrf-token"])
    params = {
        "commentsCount": "0",
        "count": count,
        "likesCount": "0",
        "moduleKey": "home-feed:desktop",
        "q": "feed",
    }
    logging.info("Getting the feed posts")
    response = requests.get(
        "https://www.linkedin.com/voyager/api/feed/updatesV2",
        params=params,
        cookies=cookies,
        headers=headers
    )

    if response.status_code != 200:
        logging.error("Error while getting the feed posts", response.text)
        return False
    ##print(response.text)
    logging.info("Feed posts retrieved")
    ugc_post_ids = set(re.findall(r"ugcPost:(\d+)", str(response.text)))
    print(ugc_post_ids)
    return ugc_post_ids


if __name__ == "__main__":
    print(getPosts(100))
