def evaluate_answer(answer, keywords):
    answer_lower = answer.lower()

    matched = 0

    for keyword in keywords:
        if keyword.lower() in answer_lower:
            matched += 1

    score = int((matched / len(keywords)) * 100)

    return {
        "score": score,
        "matched_keywords": matched,
        "total_keywords": len(keywords)
    }