



import streamlit as st
import requests

# Configure OpenAI API key
openai_api_key = "sk-akash6680"

def get_openai_response(user_input):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_input}]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except Exception as e:
        return f"Error: {e}"

# Streamlit app layout
st.title("Advanced Chatbot")
user_input = st.text_input("What would you like to ask?")
if user_input:
    chatbot_response = get_openai_response(user_input)
    st.write(f"Chatbot: {chatbot_response}")
