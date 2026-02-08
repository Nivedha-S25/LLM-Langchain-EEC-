from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

# 1. Initialize the LLM and Parser once (Global access)
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7) # Slightly higher temp for better storytelling
str_parser = StrOutputParser()

# 2. Define the GOOD NEWS logic
def good_news_logic(input_dict: dict):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a positive and optimistic news reporter."),
        ("human", "Write a short piece of GOOD NEWS about {topic}. Keep it under 5 sentences.")
    ])
    # Build and invoke the internal chain
    chain = prompt | llm | str_parser
    return chain.invoke(input_dict)

# 3. Define the BAD NEWS logic
def bad_news_logic(input_dict: dict):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a pessimistic and dramatic news reporter."),
        ("human", "Write a short piece of BAD NEWS about {topic}. Keep it under 5 sentences.")
    ])
    # Build and invoke the internal chain
    chain = prompt | llm | str_parser
    return chain.invoke(input_dict)

# 4. Construct the main Pipeline
# We skip the unnecessary first LLM call and go straight to branching
final_chain = RunnableParallel(
    good_news=RunnableLambda(good_news_logic),
    bad_news=RunnableLambda(bad_news_logic)
)

if __name__ == "__main__":
    # The input flows directly into both branches simultaneously
    response = final_chain.invoke({"topic": "The Future of Artificial Intelligence"})
    
    print("--- OPTIMISTIC VIEW ---")
    print(response['good_news'])
    print("\n--- PESSIMISTIC VIEW ---")
    print(response['bad_news'])