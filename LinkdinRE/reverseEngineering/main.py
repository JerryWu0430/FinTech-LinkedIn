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
sys.path.append("slack/")
import slackBot

sys.path.append("Firebase/")
import commentsDatabase

logging.basicConfig(level=logging.INFO)


pagesId = {
    "AINewsRoom": "100470244",
    "Marketing Masterclass": "100470244"
}




def LikeAndCommentPost(companyName=None):
    postCount = 50
    commented = False
    while commented == False:
        logging.info("Getting posts ids")
        # posts = searchPost(prompt="ai", count=1)
        posts = getFeedPosts2.getPosts(postCount)
        if posts == False:
            logging.error("Error while getting posts")
            return False 
        #print("posts : ", posts)
        for postId in posts:
            logging.info("Post id : " + postId)
            if commentsDatabase.isIn(postId, companyName):
                logging.info("Already done")
            elif getLikes(postId) < 30:
                logging.info("Likes < 30")
            else:
                time.sleep(random.randint(4, 8) + random.random())
                res = getPostInfos(postId)
                if res == False:
                    continue
                elif talksAboutAI.talksAboutAI(res[1]) == False :
                    logging.info("Not AI post")
                elif language.getLanguage(res[1]) != "EN":
                    logging.info("Not english post")
                else:
                    logging.info("Valid post to comment")

                    (author, text, profileId) = res
                    #print("Profile id : ", profileId)
                    time.sleep(random.randint(4, 8) + random.random())
                    prompt = "Author : ", author, "\nPost : ", text
                    commentText = getComment(prompt)
                    comment(commentText, postId=postId, company=pagesId[companyName])
                    like(postId=postId, company=pagesId[companyName])
                    like(postId=postId)
                    message = "We commented the post from "+str(author)+" with the text : \""+str(commentText)+"\"."
                    print(message)
                    slackBot.sendMessage(message)
                    commentsDatabase.addCommentToDatabase(postId, companyName)
                    commented = True
                    return True
        


def commentLoop(nbOfComments, companyName=None):
    for i in range(nbOfComments):
        LikeAndCommentPost(companyName=companyName)
        time.sleep(random.randint(50, 100) + random.random())


def main():
    while True:
        try:
            commentLoop(10, companyName="AINewsRoom")
            while True:
                ## tourne que si time > 6h and time < 20h
                hour = time.localtime().tm_hour
                print("Hour : ", hour)
                postingHours = [6,8,14,18]
                if hour in postingHours:
                    logging.info("Commenting")
                    commentLoop(random.randint(10,15))
                    time.sleep(60 * 60)
                else:
                    logging.info("Sleeping")
                time.sleep(60 * 45)
        except Exception as e:
            print("Error : ", e)
            slackBot.sendMessage("Error : The comment bot has failed. \""+str(e)+"\"", channel="#bot")
            slackBot.sendMessage("Pausing for 20 min before restarting...", channel="#bot")
            time.sleep(60*20)
            slackBot.sendMessage("Restarting now...", channel="#bot")
        
if __name__ == "__main__":
    main()
    