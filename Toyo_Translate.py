import getpass
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt=ChatPromptTemplate.from_messages(
    [
        ("system",
        "You are a helpfull assistant that translates {input_language} to {output_language}"
        ),
        ("human","{input}")
    ] 
)

st.title('Toyo Translate')
input_text=st.text_input("Enter your text here")

output_parser = StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke(
    {
        "input_language":"English",
        "output_language":"Sinhala",
        "input": input_text,
    }
    )
)
    