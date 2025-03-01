### *Unified AI-Powered Intelligent Document & Customer Support Automation System*  

#### *💡 Idea*  
Combine the capabilities of *AI-powered document processing* and an *automated customer support chatbot* into a *single intelligent enterprise solution*.  
This system will handle *document classification, data extraction, and automated customer interactions*—creating a seamless, end-to-end automation platform for businesses.  


**System Components**
    ->Document Processing Module (DPM) → Handles OCR, NLP, and document classification.
    ->Customer Support Chatbot (CSC) → Handles user queries, provides responses, and interacts with DPM.
    ->Enterprise Database (EDB) → Stores processed data, customer records, and support tickets.
    ->Automation Layer (RPA/API) → Connects all components, automates workflows.

PHASE 1 : AI-Powered Document Processing System

    This phase handles OCR-based text extraction, document classification, and structured data storage.
    Features Covered in Phase 1
    ✅ Extract text from invoices, receipts, and contracts using OCR (Tesseract + OpenCV)
    ✅ Classify documents using AI-based classification (spaCy/BERT)
    ✅ Validate extracted data using predefined rules
    ✅ Store extracted data in MongoDB/PostgreSQL for retrieval


PHASE 2: AI Chatbot for Customer Support

    This phase focuses on developing an AI-powered chatbot that can:
    ✅ Handle customer queries about invoices, payments, and document-related issues
    ✅ Retrieve stored documents from the document processing system (Phase 1)
    ✅ Process customer requests like "Send me my last invoice"
    ✅ Integrate LLMs (GPT-based) and RPA automation

   ### **Chatbot Setup & Functionality**  
    1. **Clone the repository**: `git clone https://github.com/your-username/chatbot_ipa_solution.git` and navigate to the project folder.  
    2. **Set up a virtual environment**: Run `python -m venv venv` and activate it.  
    3. **Install dependencies**: `pip install -r requirements.txt`. Create a `.env` file and add                  `GEMINI_API_KEY=your_google_gemini_api_key`.  
    4. **Run the chatbot**: Execute `python app.py` to start the Flask server at `http://127.0.0.1:5000`.  
    5. **Troubleshooting**:  
        - Install missing modules: `pip install flask`.  
        - Ensure the correct directory before running `pip install -r requirements.txt`.  
        - Verify API key if AI responses fail.

PHASE 3: Full Integration with Enterprise Automation (RPA & APIs)

    This phase focuses on seamlessly integrating the AI-powered document processing system (Phase 1) with the AIchatbot (Phase 2) into a unified enterprise automation system using RPA tools and APIs.


    How Everything Works Together
    1️⃣ Customer interacts with the AI chatbot (via API or UI interface)
    2️⃣ If the chatbot needs a document, it queries the document processing system
    3️⃣ If invoice validation is required, RPA automatically fills forms
    4️⃣ System integrates with enterprise APIs for ticketing, CRM, and notifications

Project Setup & Installation
    1️⃣Create a Virtual Environment (Recommended)
        python -m venv env
        source env/bin/activate   # On Mac/Linux
        env\Scripts\activate      # On Windows

    2️⃣Install Required Python Dependencies
        pip install -r requirements.txt
        Required Libraries (Inside requirements.txt)
        Flask
        requests
        openai
        pymongo
        opencv-python
        pytesseract
        spaCy
        pyautogui

    3️⃣Start the API Gateway
        cd api_gateway
        python api.py       

        Expected Output: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
        This means the API is live and will handle chatbot & document processing requests.

    4️⃣Run the AI Chatbot
        cd ai_chatbot
        python chatbot.py

    5️⃣Run the Document Processing System
        cd doc_processor
        python ocr_extraction.py

    6️⃣Run the RPA Automation (For Enterprise Tasks)
        cd automation
        python rpa.py




**Final Workflow Integration**
1️⃣ User requests an invoice via chatbot.
2️⃣ Chatbot extracts details from the database (via API).
3️⃣ If the document is missing, chatbot escalates the query to RPA.
4️⃣ If additional validation is needed, RPA updates ERP records.
5️⃣ Response is sent back to the user via chatbot, email, or WhatsApp.