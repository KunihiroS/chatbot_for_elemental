import streamlit as st
import random
import openai

openai.api_key = st.secrets["general"]["OPENAI_API_KEY"]

st.title('ふしぎなこの子になんでもきいてみよう！！')

if 'chat_log' not in st.session_state:
    st.session_state.chat_log = []

if 'last_input' not in st.session_state:
    st.session_state.last_input = ""

with st.form(key='chat_form'):
    user_input = st.text_area("なんでもきいてね", height=200)  # text_areaを使用して高さを調整
    send_button = st.form_submit_button("送信")
   
    if send_button and user_input and user_input != st.session_state.last_input:
        # OpenAI APIを使用して応答を取得
        response = openai.Completion.create(
		model="gpt-3.5-turbo",
  		messages=[
        		{"role": "system", "content": "You are a helpful tutor for Japanese elemetary school students."},
        		{"role": "assistant", "content": ""},
        		{"role": "user", "content": user_input}
    			]
		)
        bot_response = response['choices'][0]['message']['content']
        st.session_state.chat_log.insert(0, ("Bot", bot_response ))
        st.session_state.chat_log.insert(0, ("User", user_input))
        st.session_state.last_input = user_input
        
for role, message in st.session_state.chat_log:
    if role == "User":
        st.write(f'<div style="text-align: left; padding: 10px; border-radius: 5px; background-color: #191970; word-wrap: break-word;">{message}</div>', unsafe_allow_html=True)
    else:
        st.write(f'<div style="text-align: right; padding: 10px; border-radius: 5px; background-color: #B1063A; word-wrap: break-word;">{message}</div>', unsafe_allow_html=True)
