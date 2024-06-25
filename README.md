# Gemini LLM Q&A Demo Application

This repository contains a Streamlit-based web application that leverages Google Generative AI to provide responses to user inputs. The application utilizes the `gemini-pro` model to generate text based on the provided input.

## Files in this Repository

- `vision.py`: This file contains the Streamlit application for image-based input and text generation using the `gemini-pro-vision` model.
- `app.py`: This file contains the Streamlit application for text-based input and question answering using the `gemini-pro` model.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/gemini-llm-demo.git
    cd gemini-llm-demo
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Google API key:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

## Running the Applications

### Running the Vision Demo

1. Navigate to the directory containing the `vision.py` file.
2. Run the Streamlit application:
    ```sh
    streamlit run vision.py
    ```

### Running the Q&A Demo

1. Navigate to the directory containing the `app.py` file.
2. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

## Usage

### Vision Demo
- Upload an image and provide a prompt. The application will generate a response based on the image and the prompt.

### Q&A Demo
- Enter a question in the input field and click the "Ask the question" button. The application will generate a response based on the input question.

## Dependencies

- `streamlit`
- `python-dotenv`
- `google-generativeai`
- `Pillow`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the [Google Generative AI](https://developers.google.com/generative-ai) API.

## Author

- Your Name - [ArpanSethi30](https://github.com/ArpanSethi30)
