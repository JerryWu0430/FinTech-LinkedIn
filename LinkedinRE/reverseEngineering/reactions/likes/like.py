import requests
import json

with open("reverseEngineering/LinkdIncookiesMain.json", "r") as file:
    cookiesMain = json.loads(file.read())

headersMain = {
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
    "x-li-page-instance": "urn:li:page:d_flagship3_detail_base;9dT6fOvVRkS7BKXCvwmXWg==",
    "x-li-track": '{"clientVersion":"1.13.8499","mpVersion":"1.13.8499","osName":"web","timezoneOffset":1,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    "x-restli-protocol-version": "2.0.0",
}


def like(postId, company=None, cookies=cookiesMain, headers=headersMain):
    params = {
        "threadUrn": "urn:li:ugcPost:" + postId,
    }

    json_data = {
        "reactionType": "LIKE",
        #'actorUrn': 'urn:li:fsd_company:100470244',
    }
    if company != None:
        print("We like as :", str(company))
        json_data["actorUrn"] = "urn:li:fsd_company:" + str(company)

    response = requests.post(
        "https://www.linkedin.com/voyager/api/voyagerSocialDashReactions",
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    if response.status_code == 201:
        print("Like successful")
    else:
        print("Something happened for the like")
        print(response.text)


if __name__ == "__main__":
    like("7257824006148440064")
