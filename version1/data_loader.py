import pandas as pd

def load_data():
    try:
        product_stats_df = pd.read_csv("Product_Statistics.csv")
        faq_df = pd.read_excel("FAQ.xlsx")
    except Exception as e:
        print(f"Error loading files: {e}")
        exit()

    required_columns = {"Product_Name", "Category", "Price", "Rating", "Stock_Level"}
    if not required_columns.issubset(product_stats_df.columns):
        print("Error: Product_Statistics.csv is missing required columns.")
        exit()

    for col in ["Price", "Rating", "Stock_Level"]:
        product_stats_df[col] = pd.to_numeric(product_stats_df[col], errors="coerce")

    return product_stats_df, faq_df
