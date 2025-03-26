import re
from data_loader import product_stats_df

def parse_product_query(query):
    filters = {}

    category_match = re.search(r"(smartphone|laptop|earbuds|watch|mouse|electronics|computers|accessories|wearables)",
                               query, re.IGNORECASE)
    if category_match:
        filters["category"] = category_match.group(1)

    product_match = re.search(r"(Smartphone X|Laptop Pro|Wireless Earbuds|Smartwatch Z|Gaming Mouse)", query,
                              re.IGNORECASE)
    if product_match:
        filters["product_name"] = product_match.group(1)

    price_match = re.search(r"less than (\d+)", query)
    if price_match:
        filters["max_price"] = float(price_match.group(1))

    stock_match = re.search(r"available stock more than (\d+)", query)
    if stock_match:
        filters["min_stock"] = int(stock_match.group(1))

    rating_match = re.search(r"rating above (\d+)", query)
    if rating_match:
        filters["min_rating"] = float(rating_match.group(1))

    return filters

def search_products(query):
    df = product_stats_df.copy()  # Only available products
    filters = parse_product_query(query)

    if "category" in filters:
        df = df[df["Category"].str.contains(filters["category"], case=False, na=False)]
    if "product_name" in filters:
        df = df[df["Product_Name"].str.contains(filters["product_name"], case=False, na=False)]
    if "max_price" in filters:
        df = df[df["Price"] <= filters["max_price"]]
    if "min_stock" in filters:
        df = df[df["Stock_Level"] >= filters["min_stock"]]
    if "min_rating" in filters:
        df = df[df["Rating"] >= filters["min_rating"]]

    if df.empty:
        return "No available products match your query."

    product_list = "\n".join([
        f"{row['Product_Name']} ({row['Category']}) - ${row['Price']} | Stock: {row['Stock_Level']} | Rating: {row['Rating']}"
        for _, row in df.iterrows()
    ])

    return f"Here are the available products:\n{product_list}"
