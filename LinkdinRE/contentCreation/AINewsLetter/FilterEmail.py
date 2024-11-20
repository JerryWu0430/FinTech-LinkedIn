from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import tiktoken
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')


preprompt = """

    You are a sophisticated filter algorithm. Your primary task is to thoroughly analyze any piece of text I provide, focusing on the content and the topics approached. After your analysis, you will respond to this question ONLY saying 'YES' or 'NO', here is the question: 
    Is this mail give AI related news? You are my assistant. I will give you an email I received and I want you to answer this question : 
    Is this mail giving a brand new AI news ? What I mean by that is : is there enouh information about AI news in this mail ?
    YES or NO ?

"""

template = (
    preprompt
    + """
Here is the content: {content}
LinkdIn assistant :"""
)

prompt = PromptTemplate(input_variables=["content"], template=template)

llm = OpenAI(openai_api_key=openai_api_key)

llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
)


def getNbTokens(content):
    enc = tiktoken.get_encoding("cl100k_base")
    assert enc.decode(enc.encode("hello world")) == "hello world"

    # To get the tokeniser corresponding to a specific model in the OpenAI API:
    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
    res = enc.encode(content)
    print(len(res))
    return len(res)


def filterEmail(content):
    while getNbTokens(content) > 3500:
        content = content[50:-50]
    res = llm_chain.predict(content=content).strip()
    if res[0] == '"':
        print("Removing the first and last char")
        res = res[1:-1]
    print(res)
    if "YES" in res:
        return True
    else:
        return False


if __name__ == "__main__":
    email = """	


Thank you for subscribing to our Monday morning newsletter!

Be sure to add this to your Primary Inbox to ensure delivery


We also offer a paid tier for business professionals
AI Breakfast Business Premium, a comprehensive analysis of the latest AI news and developments for business leaders and investors.

3x the information, for less than $2/week
Monday: All subscribersWednesday: Business PremiumFriday: Business Premium

Business Premium members also receive:

-Discounts on industry conferences like Ai4-Discounts on AI tools for business (Like Jasper)-Free digital download of our upcoming book Decoding AI: A Non-technical Explanation of Artificial Intelligence available April 18th

Use code "BUSINESS" to save 30% on your annual subscription when you enroll today

↓

Get Premium

tw	
 
Update your email preferences or unsubscribe here

© 2024 AI Breakfast

228 Park Ave S, #29976, New York, New York 10003, United States

beehiiv logoPowered by beehiiv

"""
    filterEmail(email)
