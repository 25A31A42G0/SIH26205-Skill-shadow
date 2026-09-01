def calculate_score(correct, total):
    if total <= 0:
        return 0

    score = (correct / total) * 100

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    return round(score, 2)


def get_skill_level(score):
    if score >= 80:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Needs Improvement"


def evaluate_skills(data):
    result = {}

    for skill, values in data.items():
        correct = values.get("correct", 0)
        total = values.get("total", 0)

        score = calculate_score(correct, total)

        result[skill] = {
            "score": score,
            "level": get_skill_level(score)
        }

    return result