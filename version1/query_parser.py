import re

def parse_product_query(query, product_stats_df):
    query = query.lower()
    category, price_range, min_rating, stock_available, min_stock, max_stock = None, None, None, None, None, None

    for cat in product_stats_df["Category"].unique():
        if isinstance(cat, str) and cat.lower() in query:
            category = cat
            break

    price_match = re.search(r"(\d+)(?:\s*-\s*(\d+))?", query)
    if price_match:
        min_price, max_price = int(price_match.group(1)), int(price_match.group(2)) if price_match.group(2) else None
        price_range = (0, min_price) if max_price is None else (min_price, max_price)

    if "less than" in query or "<" in query:
        price_range = (0, int(re.search(r"(\d+)", query).group(1)))
    elif "greater than" in query or ">" in query:
        price_range = (int(re.search(r"(\d+)", query).group(1)), float("inf"))

    rating_match = re.search(r"(\d(\.\d)?)\s*stars?", query)
    if rating_match:
        min_rating = float(rating_match.group(1))

    stock_available = True if "in stock" in query else False if "out of stock" in query else None

    min_stock = int(re.search(r"(?:stock|stock level)\s*(?:greater than|>\s*)(\d+)", query).group(1)) if re.search(r"(?:stock|stock level)\s*(?:greater than|>\s*)(\d+)", query) else None
    max_stock = int(re.search(r"(?:stock|stock level)\s*(?:less than|<\s*)(\d+)", query).group(1)) if re.search(r"(?:stock|stock level)\s*(?:less than|<\s*)(\d+)", query) else None

    return {
        "category": category,
        "price_range": price_range,
        "min_rating": min_rating,
        "stock_available": stock_available,
        "min_stock": min_stock,
        "max_stock": max_stock,
    }
