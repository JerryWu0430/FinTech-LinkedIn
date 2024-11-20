import firebase_admin
from firebase_admin import credentials, firestore
import time
cred = credentials.Certificate("Firebase/credentials.json")
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

def addSource(document):
    collection_ref = db.collection("articleRSS")
    document_ref = collection_ref.document(document)
    document_ref.set({})

def checkIfIn(articleLink, source):
    collection_ref = db.collection("articleRSS")
    
    #collection_ref.document(source).set({"blogPostDone": []})
    document_ref = collection_ref.document(source)
    
    doc = document_ref.get()
    if doc.exists:
        data = doc.to_dict()
        if articleLink in data["blogPostDone"]:
            return True
        else:
            return False
    else:
        return False


def addArticleToFirebase(articleLink, source):
    collection_ref = db.collection("articleRSS")
    print("On add dans la base de donnée")
    print("source : ", source)
    
    document_ref = collection_ref.document(source)
    element_to_add = articleLink  # Replace with your actual data
    try:
        document_ref.update({"blogPostDone": firestore.ArrayUnion([element_to_add])})
    except:
        document_ref.set({"blogPostDone": [element_to_add]})


if __name__ == "__main__":
    article = {
        "title": "Vade Enhances Spear-Phishing Detection Using Generative AI for Next-Generation Threats",
        "link": "https://www.prnewswire.com/news-releases/vade-enhances-spear-phishing-detection-using-generative-ai-for-next-generation-threats-302048643.html",
        "content": "test",
    }
    print(checkIfIn(article["link"], source="aitechtrends32"))
