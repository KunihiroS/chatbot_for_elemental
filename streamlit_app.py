import streamlit as st
import random

st.title('ふしぎなこの子になんでもきいてみよう！！')

user_input = st.text_input("なんでもいれててね")
st.write("いれたもじ: ", user_input)

responses = ["That's interesting!", "Tell me more.", "I see.", "Very cool."]
if user_input:
    st.write(random.choice(responses))
