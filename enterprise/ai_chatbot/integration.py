from chatbot import get_chatbot_response
from document_fetch import fetch_document

def handle_customer_query(user_query):
    """Handles customer queries with chatbot + document retrieval"""
    
    if "invoice" in user_query.lower():
        doc = fetch_document("Invoice")
        return f"Here is your invoice:\n{doc}"
    
    elif "receipt" in user_query.lower():
        doc = fetch_document("Receipt")
        return f"Here is your receipt:\n{doc}"
    
    else:
        return get_chatbot_response(user_query)

if __name__ == "__main__":
    query = "Can you provide my last invoice?"
    print(handle_customer_query(query))
    