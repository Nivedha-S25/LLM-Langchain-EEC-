from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq

# Load environment variables from .env file

load_dotenv()

# Health Check for your API Key
if not os.getenv("GROQ_API_KEY"):
    print("❌ Critical Error: GROQ_API_KEY not found in environment.")
    exit()

# Initialize the LLM
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0 ,groq_api_key="Enter your api key here")

# 1. Define the Schema
class JokeSchema(BaseModel):
    setup: str = Field(description="The setup or lead-up to the joke")
    punchline: str = Field(description="The funny payoff or conclusion")

# 2. Bind the schema to the LLM
structured_llm = llm.with_structured_output(JokeSchema)

# 3. Execution
try:
    response = structured_llm.invoke("Tell me a developer joke")
    
    if response:
        print(f"Setup: {response.setup}")
        print(f"Punchline: {response.punchline}")
        print(f"Type: {type(response)}")
    else:
        print("The LLM returned None. Check your prompt or model capacity.")

except Exception as e:
    print(f"Error: {e}")