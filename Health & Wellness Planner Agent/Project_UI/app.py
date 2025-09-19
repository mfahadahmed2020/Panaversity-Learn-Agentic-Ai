import streamlit as st

st.set_page_config(page_title="Agentic AI Project", layout="centered")

st.title("🚀 Agentic AI Project")
st.write("Hello! Your Streamlit app is running successfully 🎉")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Welcome, {name}!")