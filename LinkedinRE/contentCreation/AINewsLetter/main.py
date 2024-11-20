from readMail import mainInboxJunk, mainInbox
import time

print("Import 1")
from ExtractInfo import extractInfo
from FilterEmail import filterEmail
from ExtractMainSuject import extractSubject
from contentCreation.AINewsLetter.GeneratePost import getPost

import sys

sys.path.append("reverseEngineering/post")
from postFunction import post


if __name__ == "__main__":
    i = 0
    getEmails = [mainInbox, mainInboxJunk]

    print("We read :")
    content = getEmails[i % 2]()
    if content is not None:
        if filterEmail(content):
            print("Filter email is true")
            """subject = extractSubject(content)
            print("Here is the subject : ", subject)
            time.sleep(5)
            info = extractInfo(subject, content)
            print("Here is the info : ", info)
            time.sleep(5)
            postText = getPost(content=info)
            print("Here is the post text : ", postText)"""
            #print("We post")
            #post(postText, pageId="100470244")
        else:
            print("Not enough AI news")
            
        i += 1
        time.sleep(10)
