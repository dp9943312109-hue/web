import streamlit as st

name = st.text_input("Enter your name:")
# You can then use the 'name' variable later in your script, for example:
if name:
    st.write(f"Hello, {name}!") #
