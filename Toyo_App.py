import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env (optional if you use an API key directly)
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=GOOGLE_API_KEY
)

# Configure Streamlit page
st.set_page_config(page_title="Toyo App", layout="centered")
st.title("🧠 Toyo App")

# Initialize session state
if "mode" not in st.session_state:
    st.session_state.mode = "Chat"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Mode selection buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("💬 Toyo Chat"):
        st.session_state.mode = "Chat"
with col2:
    if st.button("🌐 Toyo Translate"):
        st.session_state.mode = "Translate"

st.divider()

# Shared output parser
output_parser = StrOutputParser()

# --------------------------
# Chat Mode with History
# --------------------------
if st.session_state.mode == "Chat":
    st.subheader("💬 Toyo Chat")

    input_text = st.text_input("Enter your question:")

    if st.button("📤 Submit", key="chat_submit"):
        if input_text:
            # Define the prompt
            chat_prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a chatbot"),
                ("human", "Question: {question}")
            ])

            # Create the chain
            chat_chain = chat_prompt | llm | output_parser

            # Get the response
            response = chat_chain.invoke({"question": input_text})

            # Store question & response in history
            st.session_state.chat_history.append(("You", input_text))
            st.session_state.chat_history.append(("Bot", response))
        else:
            st.warning("Please enter a question.")

    # Display Chat History
    if st.session_state.chat_history:
        st.markdown("### 🕘 Chat History")
        for speaker, text in st.session_state.chat_history:
            if speaker == "You":
                st.markdown(f"**🧑 {speaker}:** {text}")
            else:
                st.markdown(f"**🤖 {speaker}:** {text}")

# --------------------------
# Translate Mode
# --------------------------
elif st.session_state.mode == "Translate":
    st.subheader("🌐 Toyo Translate")
    
    languages = [
    "English", "Sinhala", "Tamil", "Hindi", "Arabic", "Chinese (Simplified)",
    "Chinese (Traditional)", "French", "German", "Spanish", "Japanese",
    "Korean", "Russian", "Portuguese", "Italian", "Bengali", "Malayalam",
    "Telugu", "Urdu", "Thai", "Turkish", "Polish", "Vietnamese"
    ]


    input_text = st.text_input("Enter text to translate:")
    col1, col2 = st.columns(2)
    with col1:
        input_lang = st.selectbox("Input Language:", languages)
    with col2:
        output_lang = st.selectbox("Output Language:", languages)

    if st.button("📤 Submit", key="translate_submit"):
        if input_text:
            # Define the prompt
            translate_prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
                ("human", "{input}")
            ])

            # Create the chain
            translate_chain = translate_prompt | llm | output_parser

            # Get the response
            response = translate_chain.invoke({
                "input_language": input_lang,
                "output_language": output_lang,
                "input": input_text
            })

            st.success(response)
        else:
            st.warning("Please enter text to translate.")
