from ocr_extraction import extract_text
from classification import classify_document
from database import store_document

def process_document(image_path):
    """Processes a document by extracting text, classifying it, and storing in DB."""
    extracted_text = extract_text(image_path)
    doc_type = classify_document(extracted_text)
    store_document(extracted_text, doc_type)
    print(f"✅ Processed Document: {doc_type}")

if __name__ == "__main__":
    process_document("sample_docs/invoice1.png")
