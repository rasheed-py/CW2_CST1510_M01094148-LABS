import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["AIzaSyBoX_a2R-iVE9T0hB9HAbajDAua9vAzIxs"])

model = genai.GenerativeModel('gemini-2.5-flash')

st.title("💬 Gemini Chat with Streaming")

if 'chat' not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Say something...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    response = st.session_state.chat.send_message(prompt, stream=True)

    with st.chat_message("assistant"):
        container = st.empty()
        full_reply = ""

        for chunk in response:
            full_reply += chunk.text
            container.markdown(full_reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_reply
    })