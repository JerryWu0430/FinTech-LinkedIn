import imaplib
import email
import time
from contentCreation.AINewsLetter.GeneratePost import getPost
import sys
import random

sys.path.append("reverseEngineering/post")
from postFunction import post

# account credentials
username = "ainews@maxencehabar.com"
password = "3&dKE9d!Pihe&Cgz"

imap_server = "imap.hostinger.com"

mail = imaplib.IMAP4_SSL(imap_server)
mail.login(username, password)


def getUnseenJunk():
    mail.select("INBOX.Junk")
    type, data = mail.search(None, "UNSEEN")
    email_ids = data[0].split()
    print(email_ids)
    return email_ids


def getUnseen():
    mail.select("INBOX")
    type, data = mail.search(None, "ALL")
    email_ids = data[0].split()
    print(email_ids)
    return email_ids


def fetchEmailContent(emailId):
    result, email_data = mail.fetch(emailId, "(RFC822)")
    raw_email = email_data[0][1]
    parsed_email = email.message_from_bytes(raw_email)
    # print(parsed_email)
    if parsed_email.is_multipart():
        for part in parsed_email.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode()
                # print(body)
                return body
    else:
        # print(parsed_email.get_payload(decode=True).decode())
        return parsed_email.get_payload(decode=True).decode()


def mainInbox():
    res = getUnseen()
    if len(res) != 0:
        print("We read :")
        content = fetchEmailContent(res[random.randint(0, len(res) - 1)])
        print("Here is the content : ", content)
        return content
    else:
        print("No new email in Inbox")
        return None



def mainInboxJunk():
    res = getUnseenJunk()
    if len(res) != 0:
        print("We read :")
        content = fetchEmailContent(res[0])
        print("Here is the content : ", content)
        return content
    else:
        print("No new email in Junk")
        return None



if __name__ == "__main__":
    while True:
        content = mainInboxJunk()
        content = mainInbox()
        time.sleep(10)
        postText = getPost(content=content)
        print("Here is the post text : ", postText)
        #print("We post")
        #post(postText, pageId="100470244")
