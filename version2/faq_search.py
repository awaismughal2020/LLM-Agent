from data_loader import faq_df

def search_faq(query):
    faq_results = faq_df[faq_df["Question"].str.contains(query, case=False, na=False)]

    if faq_results.empty:
        return "No matching FAQ found."

    return faq_results[["Question", "Answer"]].to_dict(orient="records")
