from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import tiktoken
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')


with open("contentCreation/AINewsLetter/prepromptMail.txt", "r") as file:
    preprompt = file.read()
# print(preprompt)



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


def getPost(content):
    while getNbTokens(content) > 3500:
        content = content[50:-50]
    res = llm_chain.predict(content=content).strip()
    if res[0] == '"':
        print("Removing the first and last char")
        res = res[1:-1]
    print(res)
    return res




if __name__ == "__main__":
    post = """ntentOpen Navigation MenuMenuStory SavedTo revist this article, visit My Profile, thenView saved stories.Close Alert5 Key Updates in GPT-4 Turbo, OpenAI’s Newest ModelBackchannelBusinessCultureGearIdeasPoliticsScienceSecurityMerchGift GuidesMoreChevronStory SavedTo revist this article, visit My Profile, thenView saved stories.Close AlertSign InSearchSearchBackchannelBusinessCultureGearIdeasPoliticsScienceSecurityMerchGift GuidesPodcastsVideoArtificial IntelligenceClimateGamesNewslettersMagazineEventsWired InsiderJobsCouponsLast-Minute Deals on GiftsToys Worth GiftingGifts Under $100Gifts Under $25WIRED’s 2023 Wish ListMore Gift GuidesGadget Lab NewsletterGet Our Deals NewsletterReece RogersBusinessNov 7, 2023 1:36 PM5 Key Updates in GPT-4 Turbo, OpenAI’s Newest ModelSam Altman, CEO of OpenAI, announced a new model for ChatGPT that can pull from a newer database of information and promises to follow instructions better.Illustration: Andriy Onufriyenko/Getty ImagesSave this storySaveSave this storySaveOpenAI recently announced multiplenew features for ChatGPTand other artificial intelligence tools during its recent developer conference. The upcoming launch of a creator tool for chatbots, calledGPTs(short for generative pretrained transformers), and a new model for ChatGPT, calledGPT-4 Turbo, are two of the most important announcements from the company’s event.This isn’t the first time OpenAI has given ChatGPT a new model. Earlier this year, OpenAIupdated the algorithmfor ChatGPT from GPT-3.5 to GPT-4. Are you curious how the GPT-4 Turbo version of the chatbot will be different when it rolls out later this year? Based on previous releases, it’s likely the model will roll out toChatGPT Plussubscribers first and to the general public later.WhileOpenAIturned down WIRED’s request for early access to the new ChatGPT model, here’s what we expect to be different about GPT-4 Turbo.New Knowledge CutoffSay goodbye to the perpetual reminder from ChatGPT that its information cutoff date is restricted to September 2021. “We are just as annoyed as all of you, probably more, that GPT-4’s knowledge about the world ended in 2021,” said Sam Altman, CEO of OpenAI, at the conference. The new model includes information through April 2023, so it can answer with more current context for your prompts. Altman expressed his intentions to never let ChatGPT’s info get that dusty again. How this information is obtained remains amajor point of contentionfor authors and publishers who are unhappy with how their writing is used by OpenAI without consent.Input Longer PromptsDon’t be afraid to get super long and detailed with your prompts! “GPT-4 Turbo supports up to 128,000 tokens of context,” said Altman. Even though tokens aren’t synonymous with the number of words you can include with a prompt, Altman compared the new limit to be around the number of words from 300 book pages. Let’s say you want the chatbot to analyze an extensive document and provide you with a summary—you can now input more info at once with GPT-4 Turbo.Better Instruction FollowingWouldn’t it be nice if ChatGPT were better at paying attention to the fine detail of what you’re requesting in a prompt? According to OpenAI, the new model will be a better listener. “GPT-4 Turbo performs better than our previous models on tasks that require the careful following of instructions, such as generating specific formats (e.g., ‘always respond in XML’),” reads the company’sblog post. This may be particularly useful for people who write code with the chatbot’s assistance.Cheaper Prices for DevelopersIt might not be front-of-mind for most users of ChatGPT, but it can be quite pricey for developers to use the application programming interface from OpenAI. “So, the new pricing is one cent for a thousand prompt tokens and three cents for a thousand completion tokens,” said Altman. In plain language, this means that GPT-4 Turbo may cost less for devs to input information and receive answers.Multiple Tools in One ChatSubscribers to ChatGPT Plus may be familiar with the GPT-4 dropdown menu where you can select which chatbot tools you’d like to use. For example, you could pick theDall-E 3 betaif you want some AI-generated images or theBrowse with Bing versionif you need links from the internet. That dropdown menu is soon headed to the software graveyard. “We heard your feedback. That model picker was extremely annoying,” said Altman. The updated chatbot with GPT-4 Turbo will pick the right tools, so if you request an image, for example, it’s expected to automatically use Dall-E 3 to answer your prompt.Most PopularCultureThe 15 Best Movies on Amazon Prime Right NowMatt KamenCultureThe 30 Best Shows on Amazon Prime Right NowMatt KamenCultureBaldur's Gate 3Captures the Magic of D&DGeek's Guide to the GalaxyGearGet Ready for a ‘Tsunami’ of AI at CESBoone AshworthYou Might Also Like …📩 Get the long view on tech with Steven Levy’sPlaintext newsletterThe spy who dumped the CIA, went to therapy, and now makes incredible TVBlood, guns, and broken scooters:The chaotic rise and fall of BirdA demographic time bomb is about tohit the beef industryInside America’sschool internet censorship machineDispatch from the future: The must-havegadgets and gear of 2053🎁 Still looking for gift ideas? Check out ourgift guides🌲 Our Gear team has branched out with a new guide to the bestsleeping padsand fresh picks for thebest coolersandbinocularsReece Rogersis WIRED's service writer, focused on explaining crucial topics and helping readers get the most out of their technology. Prior to WIRED, he covered streaming atInsider.Service WriterXTopicsartificial intelligencehow-toChatGPTOpenAIalgorithmschatbotsMore from WIREDHow to Use OpenAI’s ChatGPT to Create Your Own Custom GPTI created an experimental chatbot with 50 of my WIRED articles. Try it out for yourself.Reece RogersGoogle DeepMind's Demis Hassabis Says Gemini Is a New Breed of AIGoogle’s new AI model Gemini launched today inside the Bard chatbot. It could go on to advance robotics and other projects, says Demis Hassabis, the AI executive leading the project.Will KnightOpenAI Agreed to Buy $51 Million of AI Chips From a Startup Backed by CEO Sam AltmanDocuments show that OpenAI signed a letter of intent to spend $51 million on brain-inspired chips developed by startup Rain. OpenAI CEO Sam Altman previously made a personal investment in Rain.Paresh DaveHow to Stop Another OpenAI MeltdownOpenAI designed its governance structure to protect humanity—and it imploded. The company could take pointers from Mozilla and other projects combining lofty goals with for-profit ventures.Paresh DaveOpenAI Cofounder Reid Hoffman Gives Sam Altman a Vote of ConfidenceLinkedIn and OpenAI cofounder Reid Hoffman says he's glad Sam Altman is leading the AI company again. Hoffman and other AI experts discussed the perils and potential of AI at a WIRED event Tuesday.Paresh DaveMy Surprisingly Unbiased Week With Elon Musk’s ‘Politically Biased’ ChatbotSome Elon Musk fans are concerned that Grok, xAI's answer to ChatGPT, is too politically liberal. The nature of the underlying AI technology will make “fixing” its outlook difficult.Will KnightSam Altman Officially Returns to OpenAI—With a New Board Seat for MicrosoftThe CEO’s memo to staff announces a nonvoting seat for Microsoft but leaves questions about the future of chief scientist Ilya Sutskever.Will KnightInnovation-Killing Noncompete Agreements Are Finally DyingMore US states are moving to bar companies from binding workers with noncompete agreements. Research shows the move could boost wages and innovation.Caitlin HarringtonWIRED is where tomorrow is realized. It is the essential source of information and ideas that make sense of a world in constant transformation. The WIRED conversation illuminates how technology is changing every aspect of our lives—from culture to business, science to design. The breakthroughs and innovations that we uncover lead to new ways of thinking, new connections, and new industries.More From WIREDSubscribeNewslettersFAQWIRED StaffEditorial StandardsArchiveRSSAccessibility HelpReviews and GuidesReviewsBuying GuidesCouponsMattressesElectric BikesFitness TrackersStreaming GuidesAdvertiseContact UsCustomer CareJobsPress CenterCondé Nast Store©2023Condé Nast. All rights reserved. Use of this site constitutes acceptance of ourUser AgreementandPrivacy Policy and Cookie StatementandYour California Privacy Rights.WIREDmay earn a portion of sales from products that are purchased through our site as part of our Affiliate Partnerships with retailers. The material on this site may not be reproduced, distributed, transmitted, cached or otherwise used, except with the prior written permission of Condé Nast.Ad ChoicesSelect international siteUnited StatesLargeChevronUKItaliaJapónCzech Republic & SlovakiaFacebookXPinterestYouTubeInstagramTiktokDo Not Sell M"""
    getPost(post)
