def estimate_tokens(text):
    # Rough estimate only; use the course tokenizer for official measurements.
    return max(1, (len(text) + 3) // 4)

def select_context(question, documents, limit=2):
    terms = set(question.lower().split())
    ranked = sorted(documents, key=lambda d: sum(t in (d["title"] + " " + d["text"]).lower() for t in terms), reverse=True)
    return ranked[:limit]
