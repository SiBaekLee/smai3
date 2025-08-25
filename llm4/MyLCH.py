from langchain_community.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from openai import OpenAI
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

def getOpenAI():
    llm = ChatOpenAI(temperature=0, model_name='gpt-4o')
    return llm


def getGenAI():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        max_output_tokens=200,
        google_api_key=GOOGLE_API_KEY
    )
    return llm
