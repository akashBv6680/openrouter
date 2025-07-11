import streamlit as st
import requests

# Configure Together API key
together_api_key = "tgp_v1_1xrFFEnjo40wgE3Gj0Cx4rq_Zr3IvXoVXvOGuv4oYQY"  # Replace with your actual Together API key

def get_together_response(user_input):
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {together_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",  # or any other model available on Together
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
    chatbot_response = get_together_response(user_input)
    st.write(f"Chatbot: {chatbot_response}")
