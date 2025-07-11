

import streamlit as st
import requests
import json
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

    if response.status_code == 200:
        try:
            response_json = response.json()
            if "choices" in response_json:
                return response_json["choices"][0]["message"]["content"]
            else:
                return "Error: Unexpected API response format."
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return f"Error: {response.status_code}"

# Streamlit app layout
st.title("Advanced Chatbot")
user_input = st.text_input("What would you like to ask?")
if user_input:
    chatbot_response = get_openrouter_response(user_input)
    st.write(f"Chatbot: {chatbot_response}")
