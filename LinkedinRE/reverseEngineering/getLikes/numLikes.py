import requests
import json
import time




with open("reverseEngineering/LinkdIncookiesMain.json", "r") as file:
    cookies = json.loads(file.read())


headers = {
    "authority": "www.linkedin.com",
    "accept": "application/vnd.linkedin.normalized+json+2.1",
    "accept-language": "en-US,en;q=0.9",
    "csrf-token": "ajax:1514152367892086323",
    "dnt": "1",
    "referer": "https://www.linkedin.com/feed/update/urn:li:activity:7148976776256311296/",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "x-li-lang": "fr_FR",
    "x-li-page-instance": "urn:li:page:d_flagship3_detail_base;HHfz9jNhSWeQcj0FtK1cfQ==",
    "x-li-track": '{"clientVersion":"1.13.8817","mpVersion":"1.13.8817","osName":"web","timezoneOffset":1,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    "x-restli-protocol-version": "2.0.0",
}

def getLikes(postId, cookies=cookies, headers=headers):
    print("Post id : ",postId)
    response = requests.get(
        "https://www.linkedin.com/voyager/api/graphql?variables=(count:5,start:0,threadUrn:urn%3Ali%3AugcPost%3A"+str(postId)+")&queryId=voyagerSocialDashReactions.56bde53f0c6873eb4870f5a25da96573",
        cookies=cookies,                                                                                                                                           #56bde53f0c6873eb4870f5a25da96573
        headers=headers,
    )

    print("Get likes :",response.status_code)
    # print(response.text)

    res = json.loads(response.text)
    if res is None:
        print("Likes in None")
        return 0
    #print(response.text)
    likes = res["data"]["data"]["socialDashReactionsByReactionType"]["paging"]['total']
    time.sleep(5)
    print("Likes : ", likes)
    return int(likes)

if __name__=="__main__":
    with open("reverseEngineering/LinkdIncookiesMaxab.json", "r") as file:
        cookies = json.loads(file.read())
    headersNew = headers
    headersNew["csrf-token"] = cookies["csrf-token"]
    ## remove the csrf-token from the cookies
    del cookies["csrf-token"]
    getLikes("7149393591805648897", cookies=cookies, headers=headersNew)