def search_products(df, category=None, price_range=None, stock_available=None, min_stock=None, max_stock=None, min_rating=None):
    df = df.copy()

    if category:
        df = df[df["Category"].str.contains(category, case=False, na=False)]

    if price_range:
        min_price, max_price = price_range
        df = df[(df["Price"] >= min_price) & (df["Price"] <= max_price)]

    if stock_available is not None:
        df = df[df["Stock_Level"] > 0] if stock_available else df[df["Stock_Level"] == 0]

    if min_stock is not None:
        df = df[df["Stock_Level"] >= min_stock]

    if max_stock is not None:
        df = df[df["Stock_Level"] < max_stock]

    if min_rating:
        df = df[df["Rating"] >= min_rating]

    return "No matching products found." if df.empty else df[["Product_Name", "Category", "Price", "Rating", "Stock_Level"]].to_string(index=False)
