import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("Firebase/credentials.json")
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()


def isIn(postId, pageName):
    collection_ref = db.collection("commentedPosts")

    # collection_ref.document(source).set({"blogPostDone": []})
    document_ref = collection_ref.document(pageName)

    doc = document_ref.get()
    if doc.exists:
        data = doc.to_dict()
        if postId in data["liste"]:
            return True
        else:
            return False
    else:
        return False


def addCommentToDatabase(postId, pageName):
    collection_ref = db.collection("commentedPosts")
    print("On add dans la base de donnée")
    print("source : ", pageName)

    document_ref = collection_ref.document(pageName)
    element_to_add = postId  # Replace with your actual data
    res = document_ref.update({"liste": firestore.ArrayUnion([element_to_add])})
    ##print(res)
    print("Added to database")


if __name__ == "__main__":
    print(isIn("100470244", "AINewsRoom"))
    ##addCommentToDatabase("100470244", "AINewsRoom")
