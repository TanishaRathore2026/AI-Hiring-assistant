# 🤖 AI Hiring Assistant

A simple AI-powered chatbot that automates the initial candidate screening process. Built with Python, Streamlit, and Google's Gemini API.

## Features
- Collects candidate details step-by-step (Name, Contact, Location, Experience, Tech Stack)
- Uses Gemini AI to generate 3 customized interview questions based on the candidate's tech stack
- Built-in error handling — falls back gracefully if the API call fails
- Conversation flow managed using Streamlit's session state

## Tech Stack
- **Frontend/UI:** Streamlit
- **Backend:** Python
- **AI:** Google Gemini API (gemini-1.5-flash)

## How to Run Locally
streamlit run app.py
