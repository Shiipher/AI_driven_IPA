import requests

def enterprise_dashboard():
    """Enterprise AI system main interface"""
    print("🚀 Welcome to the AI-Powered Enterprise Automation System")

    while True:
        print("\n1️⃣ Chat with AI Chatbot")
        print("2️⃣ Process New Document")
        print("3️⃣ Exit")
        choice = input("Select an option: ")

        if choice == "1":
            query = input("You: ")
            response = requests.post("http://127.0.0.1:5000/chatbot", json={"query": query})
            print("Bot:", response.json()["response"])

        elif choice == "2":
            doc_path = input("Enter document path: ")
            response = requests.post("http://127.0.0.1:5000/process_document", json={"document_path": doc_path})
            print("Extracted Data:", response.json()["extracted_data"])

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("❌ Invalid option, try again.")

if __name__ == "__main__":
    enterprise_dashboard()
