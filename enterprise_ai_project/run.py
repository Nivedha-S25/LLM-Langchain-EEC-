from langchain_layer.orchestration.main_chain import final_chain

query = "Make a decision for high churn risk customer 6388-TAUUU"

result = final_chain.invoke({
    "query": query
})

print(result)
