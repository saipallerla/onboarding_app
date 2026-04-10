# =========================
# Conversational AI for Customer Onboarding
# Full End-to-End Mini Project (Submission Ready)
# Tech Stack: Python + Streamlit + OpenAI API (or rule-based fallback)
# =========================

# ----------- STEP 1: INSTALL DEPENDENCIES -----------
# Run in terminal:
# pip install streamlit openai

# ----------- STEP 2: PROJECT STRUCTURE -----------
# onboarding_app.py  (this file)

# ----------- STEP 3: IMPORTS -----------
import streamlit as st
import datetime

# ----------- STEP 4: SIMPLE RULE-BASED CHATBOT -----------
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! Welcome to our onboarding assistant. What's your name?"

    elif "name" in user_input:
        return "Nice to meet you! Can you provide your email ID?"

    elif "@" in user_input:
        return "Great! Please share your phone number."

    elif any(char.isdigit() for char in user_input):
        return "Thanks! What service are you interested in? (Banking / Insurance / Loan)"

    elif "bank" in user_input:
        return "You selected Banking. Your onboarding is almost complete!"

    elif "insurance" in user_input:
        return "You selected Insurance. Our agent will contact you soon."

    elif "loan" in user_input:
        return "You selected Loan services. Processing your request..."

    else:
        return "I'm sorry, I didn't understand. Could you rephrase?"

# ----------- STEP 5: STREAMLIT UI -----------
st.set_page_config(page_title="Customer Onboarding AI", layout="centered")

st.title("🤖 Conversational AI - Customer Onboarding")
st.write("This app collects customer details via chat interface.")

# Initialize session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Bot response
    response = chatbot_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

# ----------- STEP 6: SAVE DATA -----------
if st.button("Save Conversation"):
    with open("onboarding_data.txt", "a") as f:
        f.write(str(datetime.datetime.now()) + "\n")
        for msg in st.session_state.messages:
            f.write(msg["role"] + ": " + msg["content"] + "\n")
        f.write("\n---------------------\n")
    st.success("Conversation Saved Successfully!")

# ----------- STEP 7: RUN APP -----------
# Command:
# streamlit run onboarding_app.py

# ----------- STEP 8: FEATURES INCLUDED -----------
# 1. Chat-based onboarding
# 2. Collects Name, Email, Phone
# 3. Service selection
# 4. Saves conversation to file
# 5. Ready-to-submit mini project

# ----------- STEP 9: OPTIONAL (ADVANCED) -----------
# Replace chatbot_response() with OpenAI API for GenAI version
# Example:
# from openai import OpenAI
# client = OpenAI(api_key="YOUR_API_KEY")
# response = client.chat.completions.create(...)

# ----------- END PROJECT -----------
