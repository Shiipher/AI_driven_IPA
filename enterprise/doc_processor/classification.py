import spacy

nlp = spacy.load("en_core_web_sm")

def classify_document(text):
    """Classifies document type based on extracted text keywords."""
    text_lower = text.lower()
    if "invoice" in text_lower or "total amount" in text_lower:
        return "Invoice"
    elif "receipt" in text_lower or "transaction id" in text_lower:
        return "Receipt"
    elif "contract" in text_lower or "agreement" in text_lower:
        return "Contract"
    else:
        return "Unknown"

if __name__ == "__main__":
    sample_text = "This is an invoice with a total amount of $500."
    doc_type = classify_document(sample_text)
    print("Document Type:", doc_type)
