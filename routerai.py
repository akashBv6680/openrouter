

import streamlit as st
import requests

# Configure Google Gemini API key
google_api_key = "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"

def get_gemini_response(user_input):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=" + google_api_key
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": user_input}]}]
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Error: {response.status_code}"

# Streamlit app layout
st.title("Advanced Chatbot")
user_input = st.text_input("What would you like to ask?")
if user_input:
    chatbot_response = get_gemini_response(user_input)
    st.write(f"Chatbot: {chatbot_response}")
