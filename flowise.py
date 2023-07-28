import requests
import streamlit as st
import time
import os
from dotenv import load_dotenv
load_dotenv() 
key = os.getenv('authorization_key')
#replace API_URL and headers with API endpoint supplied by Flowise
API_URL = ""
headers = {}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title(':red[AU] :orange[GPT]')
if "messages" not in st.session_state: 
    st.session_state.messages = [] 
for message in st.session_state.messages:
    with st.chat_message(message['role']): 
        st.markdown(message['content'])
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        #feeding the prompt to API 
        response = query({'question':prompt})
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + " ")
        message_placeholder.markdown(full_response)
