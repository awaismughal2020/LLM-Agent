# E-Commerce Chatbot

This chatbot allows users to search for products based on various criteria and retrieve answers to frequently asked questions (FAQs). It uses a **SentenceTransformer** model for semantic similarity and integrates with **LangChain tools** for query routing.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/awaismughal2020/LLM-Agent
   cd LLM-Agent
   ```

2. Set up and activate a virtual environment:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate 
   ```
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have the required data files:
   - `Product_Statistics.csv` (Product details)
   - `FAQ.xlsx` (Frequently asked questions)

5. Run the chatbot:
   ```bash
   python chatbot.py
   ```

---

## Usage

### Example Queries

#### Product Search

1. **Find electronics:**
   ```
   You: Show me Electronics
   Bot: 
   Product_Name  Category      Price  Rating  Stock_Level
   Smartphone X  Electronics   699    4.5     150
   ```

2. **Find laptops under $1500:**
   ```
   You: Show me Computers under 1500
   Bot: 
   Product_Name  Category   Price  Rating  Stock_Level
   Laptop Pro    Computers  1299   4.7     75
   ```

3. **Find accessories with a rating of at least 4.3:**
   ```
   You: Show me Accessories with 4.3 stars or more
   Bot: 
   Product_Name       Category     Price  Rating  Stock_Level
   Gaming Mouse       Accessories   79    4.4     120
   ```

4. **Find wearables in stock:**
   ```
   You: Show me Wearables in stock
   Bot: 
   Product_Name   Category  Price  Rating  Stock_Level
   Smartwatch Z   Wearables 199    4.6     50
   ```

#### FAQ Search

1. **Ask an FAQ question:**
   ```
   You: What is the return policy?
   Bot: Our return policy allows returns within 30 days of purchase with a receipt.
   ```

2. **Ask about warranty:**
   ```
   You: Do you offer a warranty on laptops?
   Bot: Yes, all laptops come with a 1-year manufacturer warranty.
   ```

---

## Project Structure

```
├── LLM-Agent
|   ├── chatbot.py         # Main LLM-Agent script
│   ├── data_loader.py    # Handles loading of data
│   ├── product_search.py # Product search functionality
│   ├── faq_retrieval.py  # FAQ retrieval functionality
│   ├── query_parser.py   # Parses user queries
│   ├── requirements.txt      # Python dependencies
│   ├── README.md             # Documentation
│   ├── Product_Statistics.csv # Product data file
│   ├── FAQ.xlsx              # FAQ data file
```

---

## Notes
- The chatbot uses **all-MiniLM-L6-v2** from SentenceTransformers for semantic search.
- Products and FAQs should be kept updated in their respective CSV and Excel files.

---
