


import streamlit as st
import requests

# Configure Google Gemini API key
google_api_key = "sk-akash6680"


def get_gemini_response(user_input):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={google_api_key}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": user_input}]}]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"Something went wrong: {err}"
    except KeyError as e:
        return f"KeyError: {e}"

# Streamlit app layout
st.title("Advanced Chatbot")
user_input = st.text_input("What would you like to ask?")
if user_input:
    chatbot_response = get_gemini_response(user_input)
    st.write(f"Chatbot: {chatbot_response}")
