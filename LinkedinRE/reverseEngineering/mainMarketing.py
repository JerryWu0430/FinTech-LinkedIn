import time
import random
from reactions.likes.like import like
from getPostContent.getPostInfos import getPostInfos
from reactions.comments.comment import comment
from reactions.comments.getComment import getComment
from getPosts.searchPosts import searchPost
from getLikes.numLikes import getLikes
import sys
import getPosts.getFeedPosts2 as getFeedPosts2
import reactions.talksAboutAI as talksAboutAI
import reactions.comments.language as language
import logging
import json

sys.path.append("slack/")
import slackBot

sys.path.append("Firebase/")
import commentsDatabase

logging.basicConfig(level=logging.INFO)

headers = {
    "authority": "www.linkedin.com",
    "accept": "application/vnd.linkedin.normalized+json+2.1",
    "accept-language": "en-US,en;q=0.9",
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

pagesId = {
    "AINewsRoom": "100470244",
    "Marketing Masterclass": "101299089",
}


def LikeAndCommentPost(companyName=None):
    postCount = 50
    commented = False
    while commented == False:
        logging.info("Getting posts ids")
        # posts = searchPost(prompt="ai", count=1)
        with open("reverseEngineering/MarketingCookies.json", "r") as f:
            getFeedCookies = json.load(f)
        headersNew = headers
        headersNew["csrf-token"] = getFeedCookies["csrf-token"]
        ## remove the csrf-token from the cookies
        del getFeedCookies["csrf-token"]
        
        
        posts = getFeedPosts2.getPosts(postCount, cookies=getFeedCookies, headersToHappen=headersNew)
        if posts == False:
            logging.error("Error while getting posts")
            return False
        # print("posts : ", posts)
        print("We have the posts!")
        with open("reverseEngineering/LinkdIncookiesMaxab.json", "r") as f:
            MaxabCookies = json.load(f)
            ##print("MaxabCookies : ", MaxabCookies)
        headersMaxab = headers
        headersMaxab["csrf-token"] = MaxabCookies["csrf-token"]
        ## remove the csrf-token from the cookies
        del MaxabCookies["csrf-token"]
        print("Beginning loop")
        for postId in posts:
            logging.info("Post id : " + postId)
            if commentsDatabase.isIn(postId, companyName):
                logging.info("Already done")
            elif getLikes(postId, cookies=MaxabCookies, headers=headersMaxab) < 30:
                logging.info("Likes < 30")
            else:
                time.sleep(random.randint(4, 8) + random.random())
                res = getPostInfos(postId, cookies=MaxabCookies, headers=headersMaxab)
                if res == False:
                    continue
                else:
                    logging.info("Valid post to comment")
                    (author, text, profileId) = res
                    # print("Profile id : ", profileId)
                    time.sleep(random.randint(4, 8) + random.random())
                    prompt = "Author : ", author, "\nPost : ", text
                    commentText = getComment(prompt, promptFile="reverseEngineering/reactions/comments/promptLMM.txt")
                    comment(commentText, postId=postId, company=pagesId[companyName], cookies=MaxabCookies, headersToAdd=headersMaxab)
                    like(postId=postId, company=pagesId[companyName], cookies=MaxabCookies, headers=headersMaxab)
                    message = (
                        companyName
                        + " : We commented the post from "
                        + str(author)
                        + ' with the text : "'
                        + str(commentText)
                        + '".'
                    )
                    print(message)
                    slackBot.sendMessage(message, channel="#bot-comment-marketing")
                    commentsDatabase.addCommentToDatabase(postId, companyName)

                    commented = True
                    return True


def commentLoop(nbOfComments):
    for i in range(nbOfComments):
        LikeAndCommentPost(companyName="Marketing Masterclass")
        logging.info("Sleeping...")
        time.sleep(random.randint(50, 100) + random.random())


def main():
    while True:
        try:
            commentLoop(10)
        except Exception as e:
            print("Error : ", e)
            slackBot.sendMessage('Error : The comment bot has failed. "' + str(e) + '"', channel="#bot-comment-marketing")
            slackBot.sendMessage("Pausing for 20 min before restarting...", channel="#bot-comment-marketing")
            time.sleep(60*20)
            slackBot.sendMessage("Restarting now...", channel="#bot-comment-marketing")

if __name__ == "__main__":
    main()
