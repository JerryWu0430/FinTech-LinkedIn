import requests
import json
import logging

logging.basicConfig(level=logging.INFO)

with open("reverseEngineering/LinkdIncookiesMain.json", "r") as file:
    cookies = json.loads(file.read())

headers = {
    "authority": "www.linkedin.com",
    "accept": "application/vnd.linkedin.normalized+json+2.1",
    "accept-language": "en-US,en;q=0.9",
    "csrf-token": "ajax:1514152367892086323",
    "dnt": "1",
    "referer": "https://www.linkedin.com/in/mstrukov/",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "x-li-lang": "fr_FR",
    "x-li-page-instance": "urn:li:page:d_flagship3_detail_base;PoEh+D7VSNS1/J9SfTvaJw==",
    "x-li-track": '{"clientVersion":"1.13.8499","mpVersion":"1.13.8499","osName":"web","timezoneOffset":1,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    "x-restli-protocol-version": "2.0.0",
}


def getPostInfos(postId, cookies=cookies, headers=headers):
    response = requests.get(
        "https://www.linkedin.com/voyager/api/graphql?variables=(commentsCount:0,likesCount:0,includeCommentsFirstReply:false,moduleKey:feed-item%3Adesktop,urnOrNss:urn%3Ali%3AugcPost%3A"
        + postId
        + ")&queryId=voyagerFeedDashUpdates.4dcfe64a6cb017481619f23a8c8986ed",
        cookies=cookies,
        headers=headers,
    )
    if response.status_code != 200:
        logging.warning("Request getPostInfos failed")
        return False
    data = response.text

    # print(response.text)
    json_data = json.loads(data)
    """with open("reverseEngineering/getPostContent/response.txt", "w") as file:
        json.dump(json_data, file)"""
    ## Get the text of the post
    json_data = json_data["included"]

    ## Get the user :
    profileId = None
    author = None
    postText = None
    nbAuthor = 0
    for i in range(len(json_data)):
        try:
            author = json_data[i]["actor"]["name"]["text"]
            ##print("Author : ", author)
            nbAuthor += 1
        except:
            pass

    for i in range(len(json_data)):
        try:
            postText = json_data[i]["commentary"]["text"]["text"]
            
        except:
            pass
    for i in range(len(json_data)):
        try:
            for j in range(len(json_data[i]['actions'])):
                if json_data[i]["actions"][j]["authorProfileId"] != None:
                    profileId = json_data[i]["actions"][j]["authorProfileId"]
        except:
            pass
    if nbAuthor > 1:
        logging.warning("More than one author")
        return False
    if postText == None:
        logging.warning("No post text")
        return False
    postText = postText.replace("#", "")
    #print("Post text : ", postText)
    return (author, postText, profileId)


if __name__ == "__main__":
    postUrl = ""
    postId = "7149373344860045312"
    getPostInfos(postId)


"""
Thomas post id : 7143878799514914816
Thomas account tag : ACoAADjxHUcBECLpJTiQt-X8ge4cuU_YAKhEY7I
"""
