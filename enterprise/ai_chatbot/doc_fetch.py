import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["document_db"]
collection = db["documents"]

def fetch_document(doc_type):
    """Retrieves the latest document of the requested type"""
    doc = collection.find_one({"document_type": doc_type}, sort=[("_id", -1)])
    return doc["text"] if doc else "No document found."

if __name__ == "__main__":
    print(fetch_document("Invoice"))
