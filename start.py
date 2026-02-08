from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
llm = ChatGroq(
    model="llama-3.1-8b-instant", 
    temperature=1
)
message=[
    SystemMessage(content="u are a very kind agent who motivates them..especially for ppl who are dealing with clg stress,placement..and everything.."),
    HumanMessage(content="i am a student and i am very stressed about my placements and college work..can u motivate me?"),
]
response = llm.invoke(message)
print(response.content)