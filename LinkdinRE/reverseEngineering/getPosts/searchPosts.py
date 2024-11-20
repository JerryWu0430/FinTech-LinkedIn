import requests
import json
import re
import time
import json

with open("reverseEngineering/LinkdIncookiesMain.json", "r") as file:
    cookies = json.loads(file.read())

headers = {
    "authority": "www.linkedin.com",
    "accept": "application/vnd.linkedin.normalized+json+2.1",
    "accept-language": "en-US,en;q=0.9",
     "csrf-token": "ajax:1514152367892086323",
    "dnt": "1",
    "referer": "https://www.linkedin.com/search/results/all/?keywords=ai&origin=GLOBAL_SEARCH_HEADER&sid=iq)",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "x-li-lang": "fr_FR",
    "x-li-page-instance": "urn:li:page:d_flagship3_search_srp_content;RpMPgDFlTzuSa+62W16AZQ==",
    "x-li-track": '{"clientVersion":"1.13.8499","mpVersion":"1.13.8499","osName":"web","timezoneOffset":1,"timezone":"Europe/Paris","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1,"displayWidth":1920,"displayHeight":1080}',
    "x-restli-protocol-version": "2.0.0",
}


def searchPost(prompt, count=4):
    res = []
    for i in range(0,count*10,10):
        response = requests.get(
            "https://www.linkedin.com/voyager/api/graphql?variables=(start:"+str(i)+",origin:OTHER,query:(keywords:"
            + prompt
            + ",flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:datePosted,value:List(past-week)),(key:resultType,value:List(CONTENT)))))&queryId=voyagerSearchDashClusters.0d1dfeebfce461654ef1279a11e52846",
            # queryParameters:List((key:resultType,value:List(CONTENT))))&queryId=voyagerSearchDashFilterClusters.a316af94acc09f9e8762cfb5021dc130
            cookies=cookies,
            headers=headers,
        )
        print(response.status_code)
        #print(response.text)
        # print(response.text)
        with open("reverseEngineering/getPosts/searchPostResponse.json", "w") as file:
            file.write(response.text)
        data = response.text

        """with open("reverseEngineering/searchPostResponse.txt", "r") as file:
            data = file.read()"""

        print("Number of posts :", str(len(data)))
        json_data = json.loads(data)
        ugc_post_ids = re.findall(r"ugcPost:(\d+)", str(data))
        print("Posts: ", ugc_post_ids)
        res += ugc_post_ids
        time.sleep(5)
    return res



if __name__ == "__main__":
    searchPost("ai")
