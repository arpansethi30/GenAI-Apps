from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel("gemini-pro")


def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        # Access the text content from the response object
        text = response.candidates[0].content.parts[0].text
        return text
    except (KeyError, IndexError, AttributeError) as e:
        return "Sorry, there was an error processing your request."


# Initialize the Streamlit application
st.set_page_config(page_title="Q&A demo")
st.header("Gemini LLM Q&A Demo Application")
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# When the submit button is pressed
if submit:
    response = get_gemini_response(input)
    st.subheader("Response: ")
    st.write(response)
