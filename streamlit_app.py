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
        st.write(f'User: {message}')
    else:
        st.write(f'Bot: {message}')
