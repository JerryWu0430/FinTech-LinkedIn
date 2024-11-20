from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import tiktoken
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

preprompt = """You are my AI assistant. I will give you an email I received and I want you to :
    Extract the main news from this email. ONLY ONE SUJBECT. Ignore the others. Answer with the sujbect, for ex : chatGPT new features.
"""

template = (
    preprompt
    + """
Voici le contenu du mail: {content}
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


def extractSubject(content):
    while getNbTokens(content) > 3500:
        content = content[50:-50]
    res = llm_chain.predict(content=content).strip()
    if res[0] == '"':
        print("Removing the first and last char")
        res = res[1:-1]
    print(res)
    return res


if __name__ == "__main__":
    email = """January 07, 2024   |   Read Online



Dear industry leader, here's your 3-minute recap (without the fluff):

Jeff Bezos' investment in Perplexity to dethrone Google

Visa deploys AI to monitor a staggering 76,000 transactions per second across 200+ countries

Siri gets a $1 billion upgrade at WWDC 2024

New tools, funding updates & job postings

Decode & Deliver: Crafting a Stellar Q&A System with Huggingface AI

Master Q&A with Hugging Face AI! Join Mina Ghashami, a seasoned FAANG engineer, on Jan 10th, 6:30 PM PST.

Unleash the power of AI to build interactive chatbots, answer complex questions, and revolutionize your text analysis.

Hands-on coding, best practices, and future trends - all packed into one session. Don't miss out! ✨

Register now
Sponsor Us

🛠️ Tools
Hopy copy - Writes better email campaigns and uses AI to generate powerful content for hundreds of different email marketing campaigns. (link)

Flick - All-in-one platform to grow and manage your socials. Get help with copywriting, scheduling, hashtags, analytics and more. (link)

Scale Donovan - An AI-powered decision-making platform that can help operators and analysts understand, plan, and act in minutes. (link)

Apollo AI - Helps you close your ideal buyers with over 265M contacts and streamlined engagement workflows powered by AI. (link)

📚 Resources
US Chief Justice: AI is here to stay, but so are judges (link)

Business Leadership in the AI Era – IBM's AI Academy (link)

What is generative AI and how does it impact businesses? (link)

A responsible approach to scaling and accelerating the impact of AI (link)

The uneven impact of generative AI on entrepreneurial performance (link)

P.S. You can still get The Ultimate ChatGPT Toolkit (no email opt-in).

Free access here →
🗞️ News
Better than Google?
Jeff Bezos has invested in Perplexity through his investment firm Bezos Expeditions. Perplexity is building an "answer engine" that responds directly to questions in text form rather than providing links, using AI technology from OpenAI.

It aims to challenge the dominance of Google in search by directly answering questions rather than just returning links. Perplexity has raised $74 million in funding at a valuation of $520 million.

→ More details about Bezos' investment & answer engine

AI preventing hackers
Visa is using AI to monitor 76,000 transactions per second across more than 200 countries. This helps Visa detect and prevent fraudulent transactions in real time.

The AI helps protect credit card users from hackers and fraudsters trying to steal money.

→ More details about Visa's AI

Apple's $1 billion investment
The new version of Siri will be unveiled at WWDC 2024. It will be powered by advanced AI and is expected to incorporate generative AI technology. With a $1 billion investment, Siri will seamlessly adapt to user's preferences and engage in natural, flowing conversations.

→ More details about the new Siri

✅ Daily AI Challenge
A business struggling with high employee turnover decides to implement AI-powered employee engagement tools. Which potential benefit is most likely to contribute to reducing turnover?
Automating performance reviews and feedback processes

Personalizing career development recommendations based on skills and interests

Monitoring employee activity and productivity levels

Replacing human managers with AI-powered leadership roles

💰 Funding
Nabla raises $24M in series B to fuel expansion of its ambient AI assistant to transform care delivery (link)

Hatz AI raises $2.5M to enable MSPs to deliver AI-as-a-Service (link)

💼 Job Board
Director of Sales Engineering at OctoML (Remote)

Senior Sales Engineer at OctoML (Remote)

🤖 Prompt Tutorial
From Blank Page to Blueprint
Prepare a content outline for [page description] and optimize for SEO.

Page description = [Insert here]




 
 	
Access our Prompts Hub (updated daily) by referring 1 friend using your custom link: https://www.neatprompts.com/subscribe?ref=ScbZKSw5pP

 
 

That's all.

If you have a second, I'd appreciate it if you could rate this email from 1-5. Just reply and let me know!

Stay curious, leaders!

- Mr. Prompts

PS. If you missed yesterday's issue, you can find it here.

*Our emails may contain sponsored content that helps support the team

PS. This newsletter is free (for early subscribers). Enjoy!

Forwarded by a friend? Sign up here.

Want to advertise with us? Learn more here.

Want the latest Startup News in your inbox? Sign up with one click.

Get your updates on Whatsapp or Telegram. Join us!"""
    extractSubject(email)
