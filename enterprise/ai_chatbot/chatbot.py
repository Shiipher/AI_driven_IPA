import openai
import os

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with actual API key

def get_chatbot_response(user_query):
    """Generates chatbot response using OpenAI GPT"""
    prompt = f"Customer Support Chatbot: {user_query}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful customer support agent."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    query = "Can I get a copy of my last invoice?"
    response = get_chatbot_response(query)
    print("Chatbot:", response)
