import feedparser
import requests
from bs4 import BeautifulSoup
import sys
import logging

logging.basicConfig(level=logging.INFO)
sys.path.append("Firebase")
import rssDatabase

sources = [
    {"url": "https://aitechtrend.com/feed/", "name": "AI Tech Trends"},
    {
        "url": "https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml",
        "name": "mit",
    },
    # {"url": "https://techcrunch.com/category/artificial-intelligence/feed/", "name": "techcrunch",}, ## Not wwoking either, no content given, just the beginning of the article
    ##{"url": "https://www.wired.com/feed/tag/ai/latest/rss", "name": "wired"},  # No content given, only link to article
    {"url": "https://www.unite.ai/feed/", "name": "unite.ai"},
    {"url": "https://www.greataiprompts.com/feed/", "name": "Great AI Prompts"},
    {
        "url": "https://aws.amazon.com/blogs/machine-learning/feed/",
        "name": "AWS Machine Learning",
    },
]


def getArticlesFromFeed(source):
    num_entries_to_fetch = 5
    feed = feedparser.parse(source["url"])
    if feed.bozo:
        logging.error("Error with the rss feed")
        return None
    else:
        articles = []
        # print("We have", len(feed.entries), "entries in the feed.")
        logging.info("We have %s entries in the feed.", len(feed.entries))
        for entry in feed.entries[:num_entries_to_fetch]:
            # print(entry.title)
            # print(entry.link)
            try:
                content = entry.content[0].value
            except AttributeError:
                content = entry.description

            soup = BeautifulSoup(content, "html.parser")
            p_tags = soup.find_all("p")
            res = ""
            for p in p_tags:
                # print(p.text)
                res += p.text
            article = {"title": entry.title, "link": entry.link, "content": res}
            ##print(article)
            articles.append(article)
            ##print("------")
        return articles


def printArticles(articles):
    for article in articles:
        print("Title : ", article["title"])
        print("Link : ", article["link"])
        # print(article["content"])
        print("------")


def getNewArticles(source):
    articles = getArticlesFromFeed(source)
    if articles == None:
        return []
    res = []
    for article in articles:
        if rssDatabase.checkIfIn(article["link"], source=source["name"]) == False:
            res.append(article)
    return res


if __name__ == "__main__":
    source = sources[-1]
    logging.info("Getting new articles from %s", source["name"])
    res = getNewArticles(source=source)
    if res == []:
        logging.info("No new articles from %s", source["name"])
    else:
        for article in res:
            print(article)
            logging.info("Adding article to database")
            # rssDatabase.addArticleToFirebase(article["link"], source=source["name"])
