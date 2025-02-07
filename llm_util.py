import os
from langchain_google_genai  import ChatGoogleGenerativeAI


def create_openai_qa_model(temperature=0.1):
    qa = ChatGoogleGenerativeAI(
        model="models/gemini-1.5-pro",
        google_api_key=os.environ['GOOGLE_TOKEN'],
        temperature=temperature
    )
    return qa

def create_gpt4o():
    qa = create_openai_qa_model(0.8)
    return qa