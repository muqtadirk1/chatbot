import streamlit as st
from openai import OpenAI

# -----------------------------
# Configure OpenAI
# -----------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
# OR (not recommended)
# client = OpenAI(api_key="YOUR_API_KEY")

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot using Streamlit")

# -----------------------------
# Initialize chat history
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# -----------------------------
# Display previous messages
# -----------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])

# -----------------------------
# User input box
# -----------------------------
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    st.chat_message("user").write(user_input)

    # Call OpenAI
    response = client.responses.create(
        model="gpt-5.2",
        input=st.session_state.messages
    )

    bot_reply = response.output_text

    # Show assistant response
    st.chat_message("assistant").write(bot_reply)

    # Save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
