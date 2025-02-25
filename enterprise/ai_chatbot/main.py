from integration import handle_customer_query

def chatbot_interface():
    """Simple chatbot interface for customer support"""
    print("💬 AI Chatbot for Customer Support (type 'exit' to stop)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = handle_customer_query(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chatbot_interface()
