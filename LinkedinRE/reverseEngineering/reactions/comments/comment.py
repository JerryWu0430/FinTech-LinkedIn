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
    "x-li-deco-include-micro-schema": "true",
    "x-li-lang": "fr_FR",
    "x-li-page-instance": "urn:li:page:d_flagship3_detail_base;cEKGcYMARtOhmmYq58045Q==",
    "x-li-pem-metadata": "Voyager - Feed - Comments=create-a-comment",
    "x-li-track": '{"clientVersion":"1.13.8499","mpVersion":"1.13.8499","osName":"web","timezoneOffset":1,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    "x-restli-protocol-version": "2.0.0",
}


def comment(text, postId, company=None, cookies=cookiesMain, headersToAdd=None):
    if headersToAdd != None:
        for key in headersToAdd:
            headersMain[key] = headersToAdd[key]
    params = {
        "decorationId": "com.linkedin.voyager.dash.deco.social.NormComment-41",
    }
    json_data = {
        "commentary": {
            "text": text,
            "attributesV2": [],
            "$type": "com.linkedin.voyager.dash.common.text.TextViewModel",
        },
        "threadUrn": "urn:li:ugcPost:" + postId,
    }
    if company != None:
        print("We comment from :", str(company))
        json_data["nonMemberActorUrn"] = "urn:li:fsd_company:" + str(company)
    
    response = requests.post(
        "https://www.linkedin.com/voyager/api/voyagerSocialDashNormComments",
        params=params,
        cookies=cookies,
        headers=headersMain,
        json=json_data,
    )

    if response.status_code == 201:
        print("Comment successful")
    else:
        print("Something happened for the comment")
        print(response.text)


if __name__ == "__main__":
    with open("reverseEngineering/LinkdIncookiesMaxab.json", "r") as f:
        MaxabCookies = json.load(f)
    headersToAdd = dict()
    headersToAdd["csrf-token"] = MaxabCookies["csrf-token"]
    ## remove the csrf-token from the cookies
    del MaxabCookies["csrf-token"]
    print("MaxabCookies : ", MaxabCookies)
    print("headersToAdd : ", headersToAdd)
    comment(
        "Bravo, j'espère que vous allez trouver!!",
        "7184544205220831235",
        company=101299089,
        cookies=MaxabCookies,
        headersToAdd=headersToAdd,
    )
