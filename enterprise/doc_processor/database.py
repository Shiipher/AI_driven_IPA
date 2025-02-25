import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["document_db"]
collection = db["documents"]

def store_document(text, doc_type):
    """Stores extracted document details in the database."""
    document_data = {"text": text, "document_type": doc_type}
    collection.insert_one(document_data)
    print("Document stored successfully.")

if __name__ == "__main__":
    sample_text = "This is an invoice with a total amount of $500."
    doc_type = "Invoice"
    store_document(sample_text, doc_type)
