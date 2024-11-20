from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import datetime
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    import language
else:
    import reactions.comments.language as language

import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env"))


def getLLMChain(filePath=None):
    if filePath != None:
        with open(filePath, "r") as file:
            preprompt = file.read()
    else:
        with open(
            "reverseEngineering/reactions/comments/prepromptComment.txt", "r"
        ) as file:
            preprompt = file.read()
    template = preprompt

    prompt = PromptTemplate(input_variables=["post"], template=template)

    llm = OpenAI(openai_api_key=os.getenv("OPEN_AI_KEY"))

    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
    )
    return llm_chain


def cleanRes(content):
    while content[0] == "\n":
        print("Removing the backslash n")
        content = content[1:]
    print("Content : ", content)
    if content[0] == '"' or content[0] == "«":
        print("Removing the first and last char quote")
        content = content[1:-1]
    # tant que premier char is not a letter or a number
    while (
        content[0]
        not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    ):
        print("Removing the first char")
        content = content[1:]
    while '"' in content:
        logging.info("Removing the quotes")
        content = content.replace('"', "")
    return content


def removingHashtags(content):
    ## remove all words after a hashtags in the content
    res = ""
    for word in content.split(" "):
        if "#" not in word:
            res += word + " "
    ##print("content without hashtags : ", res)
    return res


def removingDashEnd(content):
    ## remove all words after a hashtags in the content
    res = content.split(" -")
    return res[0]


def getComment(prompt, promptFile=None):
    print(prompt)
    llm_chain = getLLMChain(promptFile)
    res = llm_chain.predict(post=prompt).strip()
    res = cleanRes(res)
    ## Translation if needed
    if len(prompt) > 100:
        prompt = prompt[:100]
    languagePrompt = language.getLanguage(prompt)
    if languagePrompt != language.getLanguage(res):
        res = language.translate(res, languagePrompt)
    res = removingHashtags(res)
    res = removingDashEnd(res)
    print(res)
    return res


if __name__ == "__main__":
    prompt = "Author : Camis Dubu, Post : Salut! IA va changer le monde!"
    getComment(
        prompt=prompt, promptFile="reverseEngineering/reactions/comments/promptLMM.txt"
    )
