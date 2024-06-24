from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to load OpenAI model and get responses
def get_gemini_response(input_text, image):
    model = genai.GenerativeModel("gemini-pro-vision")
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)

    # Debugging: print response to understand its structure
    print(response)

    # Assuming response object has a 'parts' attribute which contains the 'text' part
    if hasattr(response, "parts") and len(response.parts) > 0:
        return response.parts[0].text
    else:
        return "No valid response received."


# Initialize the Streamlit app
st.set_page_config(page_title="Gemini Image Demo", layout="centered")

# Custom CSS for better UI
st.markdown(
    """
    <style>
    .main {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .stButton button {
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border: none;
        border-radius: 8px;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 8px;
    }
    footer {
        text-align: center;
        padding: 10px;
        margin-top: 20px;
        border-radius: 10px;
    }
    .light-theme .main {
        background-color: #f9f9f9;
    }
    .light-theme .stButton button {
        background-color: #4CAF50;
        color: white;
    }
    .light-theme .stButton button:hover {
        background-color: #45a049;
    }
    .light-theme .stTextInput>div>div>input {
        border: 2px solid #4CAF50;
    }
    .light-theme footer {
        background-color: #f1f1f1;
    }
    .dark-theme .main {
        background-color: #333;
    }
    .dark-theme .stButton button {
        background-color: #1F8A70;
        color: white;
    }
    .dark-theme .stButton button:hover {
        background-color: #166356;
    }
    .dark-theme .stTextInput>div>div>input {
        border: 2px solid #1F8A70;
    }
    .dark-theme footer {
        background-color: #444;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# JavaScript to detect theme and add appropriate class to the body
st.markdown(
    """
    <script>
    (function() {
        const body = document.querySelector('body');
        const observer = new MutationObserver(() => {
            const theme = window.localStorage.getItem('streamlit-theme');
            if (theme === 'dark') {
                body.classList.remove('light-theme');
                body.classList.add('dark-theme');
            } else {
                body.classList.remove('dark-theme');
                body.classList.add('light-theme');
            }
        });
        observer.observe(body, { attributes: true, attributeFilter: ['class'] });
    })();
    </script>
    """,
    unsafe_allow_html=True,
)

# Application Header
st.title("🌟 Gemini Image Demo")
st.subheader(
    "Upload an image and provide a prompt to get a descriptive response from the Gemini model."
)
st.markdown("---")

# Input section
input_text = st.text_input(
    "Input Prompt: ", key="input", help="Type a prompt to describe the image."
)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Submit button
submit = st.button("Tell me about the image")

# If submit button is clicked
if submit:
    if image is None:
        st.error("Please upload an image before submitting.")
    else:
        with st.spinner("Processing..."):
            response = get_gemini_response(input_text, image)
        st.subheader("Response:")
        st.write(response)

# Footer
st.markdown(
    """
    <footer>
        Created by Arpan Sethi - <a href="https://github.com/ArpanSethi30" target="_blank">GitHub</a>
    </footer>
    """,
    unsafe_allow_html=True,
)
