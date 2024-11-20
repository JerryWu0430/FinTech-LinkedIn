import requests
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os                                                                                                                                                                                                          
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(".env"))


private_key = "f6a15958-af40-ed10-981f-742a0c3f0667:fx"

headers = {
    "Authorization": "DeepL-Auth-Key " + private_key,
    "Content-Type": "application/x-www-form-urlencoded",
}

preprompt = "Is this text in english or in french ? Only answer with the name of the language. like [English] or [French]"

template = (
    preprompt
    + """\n Here is text : {post}
Answer :  """
)

prompt = PromptTemplate(input_variables=["post"], template=template)

llm = OpenAI(openai_api_key=os.getenv("OPEN_AI_KEY"))

llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
)


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
    return content


def getLanguage(text):
    print(text)
    res = llm_chain.predict(post=text).strip()
    if "French" in res:
        return "FR"
    else:
        return "EN"


def translate(text, target_lang):
    data = {
        "text": text,
        "target_lang": target_lang,
    }
    response = requests.post(
        "https://api-free.deepl.com/v2/translate", headers=headers, data=data
    )
    json_response = response.json()
    return json_response["translations"][0]["text"]


def getAvailableLanguages():
    response = requests.get("https://api-free.deepl.com/v2/languages")
    print(response.text)


if __name__ == "__main__":
    translated_text = translate(text="Bonjour comment ça va ?", target_lang="EN")
    print(translated_text)