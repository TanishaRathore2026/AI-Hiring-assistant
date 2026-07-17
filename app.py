import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Hiring Assistant Bot", layout="centered")
st.title("🤖 AI Hiring Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your Hiring Assistant. Let's start with your **Full Name**."}
    ]

if "step" not in st.session_state:
    st.session_state.step = "NAME"

if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {}

# Show all previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Take new input from user
if prompt := st.chat_input("Type your response..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = ""

    if st.session_state.step == "NAME":
        st.session_state.candidate_data["name"] = prompt
        response = f"Nice to meet you, {prompt}! What is your **Email** and **Phone Number**?"
        st.session_state.step = "CONTACT"

    elif st.session_state.step == "CONTACT":
        st.session_state.candidate_data["contact"] = prompt
        response = "Where are you **Located**, and what's your **Desired Position**?"
        st.session_state.step = "LOCATION"

    elif st.session_state.step == "LOCATION":
        st.session_state.candidate_data["location"] = prompt
        response = "How many **Years of Experience** do you have?"
        st.session_state.step = "EXP"

    elif st.session_state.step == "EXP":
        st.session_state.candidate_data["experience"] = prompt
        response = "Please list your **Tech Stack** (e.g., Python, SQL, React)."
        st.session_state.step = "TECH"

    elif st.session_state.step == "TECH":
        st.session_state.candidate_data["tech"] = prompt
        with st.spinner("AI is generating questions..."):
            try:
                ai_prompt = f"As a technical recruiter, generate 3 interview questions for a candidate skilled in: {prompt}. Keep them short."
                ai_response = model.generate_content(ai_prompt)
                response = f"Thanks! Based on your skills, here are some questions:\n\n{ai_response.text}\n\nType 'exit' to end."
            except Exception as e:
                response = f"Thanks! We've noted your skills in {prompt}. Our team will contact you soon. Type 'exit' to end."
        st.session_state.step = "DONE"

    elif "exit" in prompt.lower() or "bye" in prompt.lower():
        response = "Thank you for applying! Have a great day. 👋"

    else:
        response = "Thank you! We already have all your details."

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)