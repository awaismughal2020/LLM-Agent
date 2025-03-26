from data_loader import load_data
from product_search import search_products
from faq_retrieval import find_faq_answer
from query_parser import parse_product_query


def route_query(query, product_stats_df, faq_df):
    keywords = ["price", "stock", "rating", "category", "show me", "show", "list"]
    if any(keyword in query.lower() for keyword in keywords):
        return search_products(product_stats_df, **parse_product_query(query, product_stats_df))
    return find_faq_answer(faq_df, query)


def chatbot():
    product_stats_df, faq_df = load_data()
    print("\nWelcome to the E-Commerce Chatbot! Type 'exit' to quit.")

    while True:
        user_query = input("\nYou: ")
        if user_query.lower() == "exit":
            print("Goodbye!")
            break
        response = route_query(user_query, product_stats_df, faq_df)
        print("\nBot:", response)


if __name__ == "__main__":
    chatbot()
