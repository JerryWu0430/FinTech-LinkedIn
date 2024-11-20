import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("Firebase/credentials.json")
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()


def isIn(postId):
    collection_ref = db.collection("quotes")

    # collection_ref.document(source).set({"blogPostDone": []})
    document_ref = collection_ref.document("alreadyDone")

    doc = document_ref.get()
    if doc.exists:
        data = doc.to_dict()
        if postId in data["liste"]:
            return True
        else:
            return False
    else:
        return False


def addCommentToDatabase(postId):
    collection_ref = db.collection("quotes")
    print("On add dans la base de donnée")
    
    document_ref = collection_ref.document("alreadyDone")
    element_to_add = postId  # Replace with your actual data
    document_ref.update({"liste": firestore.ArrayUnion([element_to_add])})


if __name__ == "__main__":
    print(isIn("salut.png"))
    
