import streamlit as st
import google.generativeai as genai

# Configure API key from Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Load model
model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit page setup
st.set_page_config(page_title="Aashika Medical Chatbot", page_icon="🩺")

st.title("🩺 Aashika Medical Chatbot")

topic = st.text_input("Enter a medical topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
        st.stop()

    if option == "Explain Concept":
        prompt = f"Explain {topic} in simple language for a beginner."

    elif option == "Real-Life Example":
        prompt = f"Give one real-life hospital example of {topic}."

    elif option == "Generate Quiz":
        prompt = f"Create 5 MCQs on {topic} with answers."

    else:
        prompt = topic

    try:
        response = model.generate_content(prompt)
        st.write(response.text)

    except Exception as e:
        st.error(f"Error: {e}")


        
