from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import datetime

from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

preprompt = "Return True is this post is about AI, Business or technologies, False otherwise. only answer [True] or [False] inside brackets"
# print(preprompt)

template = preprompt + """\nHere is the post : {post}"""

prompt = PromptTemplate(input_variables=["post"], template=template)

llm = OpenAI(openai_api_key=openai_api_key)

llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
)

def cleanPost(content):
    while content[0] == "\n":
        print("Removing the backslash n")
        content = content[1:]
    if content[0] == '"':
        print("Removing the first and last char quote")
        content = content[1:-1]
    return content


aiWords = ["ai ", "artificial intelligence", "machine learning", "deep learning", "neural network", "data science", "big data", "business", "technology", "chatgpt", "gpt-3", "gpt3", "gpt 3", "gpt-2", "gpt2", "gpt 2", "openai","google","bard","gemini", "gpt4"]

def talksAboutAI(postContent: str):
    print("Talks about AI : ",end="")
    for word in aiWords:
        if word.upper() in postContent.upper():
            print("True. The word is : \"", word, "\"")
            return True
    print("False")
    return False


if __name__ == "__main__":
    post = """('Author : ', 'Marina Panova', '\nPost : ', 'ChatGPT is a creative powerhouse.\n\nEspecially for Content Creators.\n\nHave a look at what me and Jérémy prepared for you.\n\n#contentcreator #chatgpt #socialmedia #ai ')"""
    print(talksAboutAI(post))
