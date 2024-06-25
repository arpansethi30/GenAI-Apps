from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


###function to load gemini-pro model

model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat(history=[])


def get_gemini_response(question):
    response = chat.send_message(question)
    return response


###Initialize the Streamlit app

st.set_page_config(page_title="Q&A ChatBot demo", layout="centered")

st.header("Gemini Pro LLM ChatBot")

###Initialize session state for chat history if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")
