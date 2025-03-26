import pandas as pd
from config import PRODUCT_STATS_FILE, FAQ_FILE

def load_data():
    try:
        product_stats_df = pd.read_csv(PRODUCT_STATS_FILE)
        faq_df = pd.read_excel(FAQ_FILE)
    except Exception as e:
        print(f"Error loading files: {e}")
        exit()

    # Ensure required columns exist
    required_columns = {"Product_Name", "Category", "Price", "Rating", "Stock_Level"}
    if not required_columns.issubset(product_stats_df.columns):
        print("Error: Product_Statistics.csv is missing required columns.")
        exit()

    # Convert numeric columns
    for col in ["Price", "Rating", "Stock_Level"]:
        product_stats_df[col] = pd.to_numeric(product_stats_df[col], errors="coerce")

    # Filter only available products (Stock_Level > 0)
    product_stats_df = product_stats_df[product_stats_df["Stock_Level"] > 0]

    return product_stats_df, faq_df

# Load data at module level
product_stats_df, faq_df = load_data()
