import streamlit as st

st.title('Hello, Streamlit!')

user_input = st.text_input("なんでも入力してね")
st.write("入力: ", user_input)
