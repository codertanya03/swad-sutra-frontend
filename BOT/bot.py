# swadsutra_bot.py

import os
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage

# Environment setup
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = ""
if not os.environ.get(""):
    os.environ[""] = ""

# Initialize model
model = init_chat_model("llama3-8b-8192", model_provider="groq")

# Create graph with a model node
workflow = StateGraph(state_schema=MessagesState)

def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}

workflow.add_node("model", call_model)
workflow.add_edge(START, "model")
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# Exported function
def ask_swadsutra(query: str, data):
    input_messages = [HumanMessage(query)]
    config = {
    "configurable": {
        "thread_id": data["thread_id"],
        "food_preference": data["food_preference"],
        "taste_preference": data["taste_preference"],
        "allergic_foods": data["allergic_foods"]
    }
}

    try:
        output = app.invoke({"messages": input_messages}, config)
        return output["messages"][-1].content
    except Exception as e:
        return f"Error: {e}"
