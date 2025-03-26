from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from config import LLM_MODEL
from product_search import search_products
from faq_search import search_faq

# Initialize LLM
llm = OllamaLLM(model=LLM_MODEL)

# Define Tools
tools = [
    Tool(
        name="Product_Search",
        func=search_products,
        description="Search available products based on filters like price, stock, rating, category, and name. Always use this tool for product-related queries.",
    ),
    Tool(
        name="FAQ_Search",
        func=search_faq,
        description="Retrieve answers from the FAQ database based on a given query.",
    ),
]

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    memory=memory,
    agent="conversational-react-description",
    verbose=True,
)

def chatbot_response(user_input):
    return agent.invoke({"input": user_input})["output"]
