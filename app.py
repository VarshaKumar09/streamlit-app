import streamlit as st

st.title("Simple Streamlit App")
st.write("Hello, welcome to my first web app!")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write(f"Hello, {name}!")
