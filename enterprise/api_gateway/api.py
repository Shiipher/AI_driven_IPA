from flask import Flask, request, jsonify
from ai_chatbot.integration import handle_customer_query
from document_processing.ocr_processing import process_document

app = Flask(__name__)

@app.route("/chatbot", methods=["POST"])
def chatbot_api():
    """API endpoint to interact with chatbot"""
    user_query = request.json.get("query")
    response = handle_customer_query(user_query)
    return jsonify({"response": response})

@app.route("/process_document", methods=["POST"])
def document_api():
    """API endpoint for document processing"""
    document_path = request.json.get("document_path")
    extracted_data = process_document(document_path)
    return jsonify({"extracted_data": extracted_data})

if __name__ == "__main__":
    app.run(debug=True)
