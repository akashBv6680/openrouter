import streamlit as st
import requests

# Configure OpenRouter API key
openrouter_api_key = "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"

def get_openrouter_response(user_input):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {openrouter_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # or any other model available on OpenRouter
        "messages": [{"role": "user", "content": user_input}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

# Streamlit app layout
st.title("Advanced Chatbot")
user_input = st.text_input("What would you like to ask?")
if user_input:
    chatbot_response = get_openrouter_response(user_input)
    st.write(f"Chatbot: {chatbot_response}")
