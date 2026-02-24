"""
llm.py

Provides Gemini model instance.

Requires:
- GOOGLE_API_KEY environment variable set
"""
# This file doesn't need any other changes. 
import os
from langchain_google_genai import ChatGoogleGenerativeAI


def get_llm():
    return ChatGoogleGenerativeAI(
        model="models/gemini-1.5-pro",
        google_api_key=os.environ["GOOGLE_API_KEY"],
    )
