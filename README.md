# HeAIapp

Deployment Link 
https://heaiapp-4wyuwjvcnulnhxourlt5tb.streamlit.app/

Youtube Link
https://youtu.be/JrFAiuxpUuQ


![image](https://github.com/user-attachments/assets/ce9613a8-18db-4435-9c97-5ce7ae116737)

![image](https://github.com/user-attachments/assets/326e4cf3-eb3a-4398-ba0e-4784f95b87e6)



AI Chemist App: Project Report
Made by 
Sudeep Sarkar
skyohanyt@gmail.com 
Thakur College of Engineering and Technology

Deployment link 
https://heaiapp-4wyuwjvcnulnhxourlt5tb.streamlit.app/

Github Link 
https://github.com/Sudeep1212/HeAIapp/ 

Video Link
https://youtu.be/JrFAiuxpUuQ 



Introduction
The AI Chemist App is an innovative web-based application designed to assist pharmaceutical professionals and enthusiasts by analyzing and identifying tablets from images. The application uses Google's Generative AI to analyze images of tablets and provide detailed insights such as the tablets’ uses, purposes, distinguishing features, and more. This app is built with Streamlit, a Python library, and integrates Google Generative AI for deep image analysis. This report details the development, features, technologies, challenges, and future scope of the project.


Project Overview
The AI Chemist App aims to provide detailed analysis of tablets through the combination of image recognition and AI-driven descriptions. The user uploads an image of a tablet, inputs a textual prompt, and the app generates an in-depth analysis of the tablet’s functionality, uses, and other related specifications.


Core Features
1.	Image Upload: Users can upload images of tablets for analysis.
2.	Prompt Input: A text input area allows users to provide prompts for the AI model to generate specific analysis or descriptions of the tablets.
3.	AI Integration: Google’s Generative AI (Gemini 1.5 Flash) model processes the uploaded image and the provided prompt to generate responses based on the visual data.
4.	User-Friendly Interface: The interface is minimalistic, ensuring a clean and easy-to-navigate design.
Technologies Used
•	Python: The backend is developed using Python, which integrates libraries for AI and image processing.
•	Streamlit: Streamlit is used to create the frontend of the app, providing a user-friendly and interactive web interface.
•	Google Generative AI: The generative AI model is responsible for processing the images and generating detailed descriptions of the tablets.
•	dotenv: The dotenv library is used to securely manage environment variables like the Google API key.
•	Cloud Deployment: The app is deployed using Streamlit Cloud, making it accessible on the web.
How It Works
1.	User Interaction: The user visits the app and is prompted to either input a custom prompt or use the default one.
2.	Image Upload: The user uploads an image of tablets, which is then processed by the backend.
3.	Generative AI Processing: Google’s Generative AI model (Gemini 1.5 Flash) is invoked to analyze the uploaded image and interpret the visual data based on the prompt.
4.	Response Generation: The app generates a detailed response, outlining the characteristics, uses, and features of the tablets depicted in the image.
5.	Display of Results: The results are displayed neatly in the app interface for the user to read and understand.
Design and User Experience
The design of the app is kept simple and professional, with a minimalist approach that removes distractions. It follows a clean layout to enhance usability.
•	Input Field for Prompt: Users can type a prompt to guide the AI in generating detailed descriptions.
•	File Upload for Image: Users can upload tablet images, which are processed by the AI model.
•	Response Display: The results are displayed in a structured format to allow users to easily comprehend the output.
The UI is responsive, meaning it adjusts well across different devices, whether on mobile or desktop.


Challenges Faced
1.	Image Quality: The AI model's performance is highly dependent on the quality of the uploaded image. The app needed to handle various image qualities and ensure accurate recognition.
2.	Model Integration: Integrating Google’s Generative AI model smoothly into the app was a technical challenge. However, it was solved with the correct API setup and configuration.
3.	Real-Time Processing: Ensuring real-time image analysis while keeping the app responsive required optimization efforts in both frontend and backend components.
Future Scope
1.	Real-Time Image Recognition: Implementing real-time recognition via a camera would make it more interactive, allowing users to capture images on the go.
2.	Expanded Database: By expanding the database of known tablets, the app could become more versatile and accurate in identifying a wider variety of tablets.
3.	Additional Features: Future versions could offer recommendations on drug interactions, dosages, and alternatives, based on the tablet’s characteristics.


Conclusion
The AI Chemist App serves as an innovative tool for analyzing pharmaceutical tablets. It demonstrates the power of AI in simplifying complex tasks like image analysis and drug identification. With its current capabilities, the app provides pharmaceutical professionals with a new way to analyze tablets, with a clean and user-friendly interface. The future potential of the app includes further features and improvements, including real-time recognition and expanded data integration.
This app is an excellent example of how AI can be applied in practical, real-world scenarios, helping professionals make informed decisions based on visual data.


Code Implementation
Main Application Code
import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title='AI Chemist App', layout="wide")

st.markdown("""
    <style>
        body {
            color: #333333;
            background-color: #F4F4F4;
            font-family: Arial, sans-serif;
        }
        .css-18e3th9 {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .css-18ni7ap {
            border: 1px solid #CCCCCC;
            border-radius: 10px;
            color: #333333;
        }
        input, textarea {
            background-color: #FFFFFF !important;
            color: #333333 !important;
        }
        .stButton>button {
            color: #FFFFFF;
            background-color: #007BFF;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

st.title("AI Chemist App")

def image_reader():
    st.subheader("Input Prompt:")
    input_text = st.text_input(" ", placeholder="Enter your prompt here...")

    st.subheader("Choose an image...")
    uploaded_file = st.file_uploader("Drag and drop file here", type=["jpg", "jpeg", "png"])

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


Explanation of Key Sections in the Code
1.	Frontend Design: We used Streamlit to create the user interface, which includes:
o	A text input field for the prompt.
o	An image uploader for the tablet image.
o	A button to trigger the AI model for analysis.
2.	Image Processing and AI Model: The Google Generative AI is used to process the uploaded image and text prompt. The model analyzes the image and generates a response based on the input.
3.	Response Display: The response is displayed in a neat, formatted text area, providing insights into the tablets.

