import streamlit as st
import random

st.title('ふしぎなこの子になんでもきいてみよう！！')

responses = ["That's interesting!", "Tell me more.", "I see.", "Very cool."]
chat_log = []

user_input = st.text_input("なんでもきいてね")

if user_input:
    chat_log.append(("User", user_input))
    chat_log.append(("Bot", random.choice(responses)))

for role, message in chat_log:
    if role == "User":
        st.write(f'<div style="text-align: left; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">{message}</div>', unsafe_allow_html=True)
    else:
        st.write(f'<div style="text-align: right; padding: 10px; border-radius: 5px; background-color: #e0e0e0;">{message}</div>', unsafe_allow_html=True)
