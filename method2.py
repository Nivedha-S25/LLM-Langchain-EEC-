import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model="llama-3.1-8b-instant", 
    temperature=1, 
    groq_api_key=api_key
)
try:
    response = llm.invoke("let's say you are in ur pre final year in your bachelor's degree and you have to do a final year project..what would u do to stand out? and u are also going to put a paper on it..so what will it be in sodtware and using computer vision?")
    print("Response from Groq:")
    print("-" * 20)
    print(response.content)
except Exception as e:
    print(f"An error occurred: {e}")