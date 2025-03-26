# LLM Agent

## Overview
This is an AI-powered chatbot for an e-commerce platform that helps users search for products and find answers to frequently asked questions (FAQs). The chatbot uses **LangChain** and **Ollama LLM** to process user queries.

## Versions

- **Version 1:** Simple LangChain tools using SentenceTransformer.
- **Version 2:** Chatbot using the Ollama agent.


## Features
- **Product Search:** Find products based on filters like price, stock availability, rating, and category.
- **FAQ Search:** Retrieve answers from a predefined FAQ dataset.
- **Conversational Memory:** Remembers previous interactions for a better chat experience.

## File Structure
```
/LLM Agent
│── main.py              # Entry point of the chatbot
│── data_loader.py       # Loads product and FAQ data
│── product_search.py    # Handles product-related queries
│── faq_search.py        # Handles FAQ searches
│── chatbot.py           # Initializes LangChain agent
│── config.py            # Configuration settings
│── Product_Statistics.csv  # Product dataset (CSV format)
│── FAQ.xlsx             # FAQ dataset (Excel format)
│── README.md            # Project documentation
```

## Setup Instructions
### 1. Install Ollama on macOS
Ollama is required to run the chatbot’s LLM model. Follow these steps to install it:
```sh
brew install ollama
```
Or, download and install Ollama manually from [Ollama's official website](https://ollama.ai/).

### 2. Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies. Run the following commands:
```sh
python3.10 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Required Packages
```sh
pip install -r requirements.txt
```

### 4. Start Ollama Server
Before running the chatbot, ensure that the Ollama server is running in a separate terminal outside the virtual environment:
```sh
ollama serve
```

### 5. Run the Chatbot
Start the chatbot by running:
```sh
python main.py
```
The chatbot will start interacting with you. Type a query or type `exit` to quit.

## Configuration
Modify `config.py` to change the data source or LLM model:
```python
PRODUCT_STATS_FILE = "Product_Statistics.csv"
FAQ_FILE = "FAQ.xlsx"
LLM_MODEL = "mistral" 
```

## How It Works
1. The chatbot receives user input.
2. It determines whether the query is related to products or FAQs.
3. Based on the query, it calls either `search_products()` or `search_faq()`.
4. The response is generated using LangChain and returned to the user.

## Example Usage
```
You: Show me laptops under $1000 with good ratings.
Bot: Here are the available products:
    - Laptop Pro (Computers) - $950 | Stock: 10 | Rating: 4.5
```

