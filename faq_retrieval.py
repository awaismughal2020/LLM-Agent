from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def find_faq_answer(faq_df, query):
    questions = faq_df["Question"].tolist()
    query_embedding = model.encode(query, convert_to_tensor=True)
    question_embeddings = model.encode(questions, convert_to_tensor=True)

    similarities = util.pytorch_cos_sim(query_embedding, question_embeddings)[0]
    best_match_idx = similarities.cpu().numpy().argmax()

    return "Sorry, I couldn't find a relevant FAQ." if similarities[best_match_idx] < 0.5 else faq_df.iloc[best_match_idx]["Answer"]
