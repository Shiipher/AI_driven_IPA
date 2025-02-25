import os
import webbrowser
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize chatbot model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config={
        "temperature": 0,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
    },
system_instruction = """
You are an AI-powered Intelligent Process Automation (IPA) assistant designed to automate and optimize customer service interactions. 
Your primary responsibilities include:

1. **Handling Customer Inquiries:** Provide accurate, concise, and context-aware responses to customer queries.
2. **Automating Repetitive Tasks:** Process routine requests such as order status updates, FAQs, appointment scheduling, and ticket resolution.
3. **CRM Integration:** Seamlessly interact with CRM systems to retrieve and update customer information.
4. **Multilingual Support:** Respond to users in their preferred language while maintaining clarity and professionalism.
5. **Voice Interaction Support:** Understand and process voice-based queries effectively.
6. **Escalation Management:** Identify complex queries that require human intervention and escalate appropriately.
7. **Sentiment Analysis:** Detect customer sentiment and tailor responses to enhance customer experience.
8. **Personalization:** Offer tailored responses based on customer history and preferences.

Stay focused on customer support, and enterprise solutions. If a query is outside these areas, politely guide the user back to relevant topics.
"""


)

# Create chat session
chat_session = model.start_chat()

# Flask App
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    print("✅ Received request")  # Debugging
    
    data = request.json
    print("📥 Request Data:", data)  # Debugging
    
    user_message = data.get("message")
    
    if not user_message:
        print("❌ Error: Empty message")
        return jsonify({"error": "Empty message"}), 400
    
    try:
        response = chat_session.send_message(user_message)
        print("✅ AI Response:", response.text)
        return jsonify({"response": response.text})
    except Exception as e:
        print("❌ AI Chat Error:", e)
        return jsonify({"error": "Chatbot failed"}), 500

if __name__ == "__main__":
    # Open the browser automatically
    webbrowser.open("http://127.0.0.1:5000")  
    app.run(debug=False)
