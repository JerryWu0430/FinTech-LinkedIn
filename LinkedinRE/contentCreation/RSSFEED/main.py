from rssFeed import getNewArticles, sources
import rssDatabase
import sys
import logging
import random



import convertArticleToPost
import time

sys.path.append("reverseEngineering/post")
import postFunction

sys.path.append("slack/")
import slackBot


def main():
    for source in sources:
        logging.info("Getting new articles from : " + str(source["name"]))
        res = getNewArticles(source=source)
        if res == []:
            logging.info("No new articles")
        else:
            for article in res:
                ## We do what we need to do with the article (post, etc, etc)
                print(article["title"])
                post = convertArticleToPost.getPost(article["content"])
                ##os.system("clear")
                if "Doug" not in post:
                    print("Doug not in post")
                    ## we retry once
                    post = convertArticleToPost.getPost(article["content"])
                print("Here is the post : --------------------------------------------")
                print(post)
                res = postFunction.post(post, pageId="100470244")
                rssDatabase.addArticleToFirebase(
                    article["link"], source=source["name"]
                )
                ## sleep for x minutes x between 20 and 40 random
                time.sleep(60*(20+random.randint(0,20)))


if __name__ == "__main__":
    try:
        while True:
            main()
            logging.info("Sleeping for 2 hours")
            time.sleep(60*60*2)
    except Exception as e:
        logging.error(e)
        errorMessage = "RSSFEED has crashed." + str(e)
        slackBot.sendMessage(errorMessage)

