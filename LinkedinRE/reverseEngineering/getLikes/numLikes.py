import requests
import json
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=os.path.join("reverseEngineering", ".env"))

# File paths
COOKIES_FILE = os.getenv("COOKIES_FILE", "reverseEngineering/LinkdIncookiesMain.json")
HEADERS_FILE = os.getenv("HEADERS_FILE", "reverseEngineering/headers.json")


# Load cookies from a file
def load_cookies(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Load headers dynamically
def load_headers(file_path, cookies):
    with open(file_path, "r") as file:
        headers = json.load(file)
        headers["csrf-token"] = cookies["JSESSIONID"]
        return headers

def getLikes(postId, cookies, headers):
    print("Post id : ",postId)
    url = (
        "https://www.linkedin.com/voyager/api/graphql?variables=(count:5,start:0,threadUrn:urn%3Ali%3AugcPost%3A{postId})&queryId=voyagerSocialDashReactions.56bde53f0c6873eb4870f5a25da96573"
    )
    
    response = requests.get(url, cookies=cookies, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code != 200:
        print(f"Failed to fetch likes: {response.text}")
        return 0
    # print(response.text)

    res = json.loads(response.text)
    if res is None:
        print("Likes is None")
        return 0
    #print(response.text)
    likes = res["data"]["data"]["socialDashReactionsByReactionType"]["paging"]['total']
    time.sleep(5)
    print("Likes : ", likes)
    return int(likes)

if __name__=="__main__":
    cookies = load_cookies(COOKIES_FILE)
    headers = load_headers(HEADERS_FILE, cookies)
    post_id = os.getenv("POST_ID", "7149393591805648897")
    getLikes(post_id, cookies, headers)