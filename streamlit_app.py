import streamlit as st
import random

st.title('ふしぎなこの子になんでもきいてみよう！！')

responses = ["That's interesting!", "Tell me more.", "I see.", "Very cool."]

if 'chat_log' not in st.session_state:
    st.session_state.chat_log = []

with st.form(key='chat_form'):
    user_input = st.text_input("なんでもきいてね")
    send_button = st.form_submit_button("送信")
   
    if send_button and user_input:
        st.session_state.chat_log.append(("User", user_input))
        st.session_state.chat_log.append(("Bot", random.choice(responses)))

for role, message in reversed(st.session_state.chat_log):
    if role == "User":
        st.write(f'<div style="text-align: left; padding: 10px; border-radius: 5px; background-color: #191970;">{message}</div>', unsafe_allow_html=True)
    else:
        st.write(f'<div style="text-align: right; padding: 10px; border-radius: 5px; background-color: #B1063A;">{message}</div>', unsafe_allow_html=True)
