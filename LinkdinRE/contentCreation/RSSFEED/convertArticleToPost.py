from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import logging
import tiktoken

## Import API key from .env
import os                                                                                                                                                                                                          
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(".env"))


logging.basicConfig(level=logging.INFO)

with open("contentCreation/prepromptPost.txt", "r") as file:
    preprompt = file.read()
# print(preprompt)

template = (
    preprompt
    + """
    {content}
    assistant :"""
)

prompt = PromptTemplate(input_variables=["content"], template=template)

llm = OpenAI(openai_api_key=os.getenv("OPEN_AI_KEY"))

llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
)


def getNbTokens(content):
    enc = tiktoken.get_encoding("cl100k_base")
    # To get the tokeniser corresponding to a specific model in the OpenAI API:
    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
    res = enc.encode(content)
    logging.info(f"Number of tokens from prompt: {len(res)}")
    return len(res)


def cleanPost(content):
    while content[0] == "\n":
        logging.info("Removing the backslash n")
        content = content[1:]
    while content[0] == '"':
        logging.info("Removing the first char")
        content = content[1:]
    while content[-1] == '"':
        logging.info("Removing the last char because it is a quote")
        content = content[:-1]
    while '"' in content:
        logging.info("Removing the quotes")
        content = content.replace('"', "")
    return content



def getPost(content):
    while getNbTokens(content+preprompt) > 3000:
        content = content[50:-50]
    res = llm_chain.predict(content=content, max_tokens=1000)
    res = cleanPost(res)
    print(res)
    return res


if __name__ == "__main__":
    post = """Using a new method, Vade increases the confidence of spear-phishing detection by 50% for W2 fraudSAN FRANCISCO, Jan. 31, 2024 /PRNewswire/ — Vade, a global leader in AI-powered threat detection and response with more than 1.4 billion protected mailboxes worldwide, today announced that it has pioneered a new method that improves the confidence of its spear-phishing detection engine. The enhancement, designed to combat advanced threats including those produced by generative AI, leverages threat samples created by artificial technology and human sources.The new method trains Vade’s spear-phishing algorithms on a unique combination of traditional and artificially generated spear-phishing emails. Vade has confirmed that the enhancement increases the confidence of detection across seven spear phishing classifiers, or categories. These range from scams involving W2 fraud, payroll fraud, banking fraud, and more. In the US, W2 fraud accounts for the largest improvement, seeing a 50% increase in confidence, followed by banking fraud at 30%. W2 fraud, which surges during the US tax season, occurs when attackers attempt to fraudulently obtain employee W2s. Vade is implementing the enhancement just as W2 fraud volumes have increased by more than 130% between December and January. Spear phishing is the costliest cyberthreat for businesses and consumers worldwide. According to the Internet Crime Complaint Center (IC3), reported losses globally from spear-phishing attacks amounted to $2.7 billion (USD) in 2022. That figure is expected to increase significantly in the coming years, especially with the emergence of generative AI tools that aid in content creation.“We are entering a period of unprecedented transformation in cybersecurity,” said Adrien Gendre, Chief Technology and Product Officer at Vade. “Generative AI is becoming a gamechanger. It gives hackers new capabilities to deploy advanced attacks at scale and security vendors the opportunity to keep pace. As a leader in cybersecurity, we have long recognized the need to embrace generative AI as a force for good. And we are. We’re fighting fire with fire.”Historically, spear phishing emails commonly contained characteristics that made them easier to detect as fraudulent, such as spelling and grammatical errors. Generative AI platforms can eliminate these factors, producing error-free text in any language. This enables foreign attackers to localize spear phishing emails and increase the appearance of legitimacy.Since generative AI’s growth in popularity, Vade researchers have observed a significant increase in the quality of observed threats. And while generative AI creators have instituted safety controls to prevent misuse of their platforms, Vade analysts have conducted internal tests that demonstrate the ability to circumvent these measures.Vade is implementing the enhancement for its email security suite, Vade for M365. Once complete, organizations will immediately see the benefits of the update.Request a demo of Vade for M365About VadeVade is a leading cybersecurity firm specializing in AI-driven threat detection and response solutions for Microsoft collaboration suite, with a focus on serving Small to Medium-sized Businesses (SMBs) and their Managed Service Providers (MSPs). With a global presence across eight locations, including the United States, France, Japan, Canada, and Israel, Vade’s flagship product, Vade for Microsoft 365, seamlessly provides supplementary cybersecurity services for Microsoft’s collaboration suite. The company’s best-in-class security solutions integrate robust AI-driven protection and automated threat remediation, resulting in improved efficiency, reduced administrative overhead, and optimized cybersecurity investments.Vade provides distinctive protection against phishing, spear phishing, and malware, ensuring error-free configurations and enabling rapid deployment. Vade is a trusted choice for some of the world’s leading internet service providers and security solution providers, ensuring the security of 1.4 billion email inboxes.To learn more, please visit www.vadesecure.com and follow us on Twitter @vadesecure or LinkedIn https://www.linkedin.com/company/vade-secure/.SOURCE Vadehttps://www.prnewswire.com/news-releases/vade-enhances-spear-phishing-detection-using-generative-ai-for-next-generation-threats-302048643.htmlThe post Vade Enhances Spear-Phishing Detection Using Generative AI for Next-Generation Threats first appeared on AITechTrend."""
    getPost(post)
    # getNbTokens("How are you doing bro ?????")
