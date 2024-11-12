import google.generativeai as genai
import streamlit as st

GOOGLE_API_KEY = "AIzaSyABqFScfhJ49Gwwsxb7OnHV-yPsH1jONRc"

st.set_page_config(page_title='AI Chemist App', layout="centered")

st.markdown("""
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #F5F5F5;
            color: #333;
            margin: 0;
            padding: 0;
        }

        .stApp {
            background-color: #FFFFFF;
            padding: 20px;
        }

        .stTitle {
            color: #333;
            font-size: 28px;
            font-weight: 600;
            text-align: center;
            margin-bottom: 20px;
        }

        input, textarea {
            background-color: #FFF;
            color: #333;
            border: 1px solid #CCC;
            border-radius: 5px;
            padding: 12px;
            width: 100%;
            margin-bottom: 15px;
            font-size: 16px;
        }

        input:focus, textarea:focus {
            border-color: #007BFF;
            outline: none;
        }

        .stButton>button {
            color: white;
            background-color: #007BFF;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            font-weight: 600;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #0056b3;
        }

        .stFileUploader>div {
            background-color: #FFF;
            border: 1px solid #CCC;
            border-radius: 5px;
            padding: 25px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.title("AI Chemist App")

def image_reader():
    st.subheader("Enter your analysis prompt:")
    input_text = st.text_area(" ", value="""You are an expert pharmaceutical chemist. Analyze the tablets shown in the image, and provide the details for each tablet with the following format:

1. Examine the image carefully and identify the tablets depicted.
2. Describe the uses and functionalities of each tablet.
3. Provide information on the intended purposes, features, and typical applications.
4. Include specifications or distinguishing characteristics of each tablet, if available.
5. Ensure clarity and conciseness in your descriptions.""", height=220)

    st.subheader("Upload the image to analyze:")
    uploaded_file = st.file_uploader("Drag and drop an image here", type=["jpg", "jpeg", "png"])

    genai.configure(api_key=GOOGLE_API_KEY)

    def get_gemini_response(input_text, image, prompt):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([input_text, image[0], prompt])
        return response.text

    def input_image_setup(uploaded_file):
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
            return image_parts
        else:
            st.error("Please upload a valid image file.")
            return None

    if st.button("Analyze Tablets"):
        image_parts = input_image_setup(uploaded_file)
        if image_parts:
            prompt = "Analyze the image and provide details based on the text input."
            response = get_gemini_response(input_text, image_parts, prompt)
            st.subheader("AI Response")
            st.text_area("", response, height=300)

if __name__ == "__main__":
    image_reader()
