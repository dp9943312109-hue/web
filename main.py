import streamlit as st
st.title("hello i am working in streamlit")
name = st.text_input("Enter your name:")
if st.button("submit"):
st.weite(f'Hello!{name} Creating a simple web")

