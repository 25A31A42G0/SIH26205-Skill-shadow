from ai.skill_scorer import evaluate_skills


def analyze_response(data):
    scores = evaluate_skills(data)

    strengths = []
    weaknesses = []
    feedback = []

    for skill, details in scores.items():
        score = details["score"]

        if score >= 70:
            strengths.append(skill)
        else:
            weaknesses.append(skill)

        if score >= 80:
            feedback.append(f"{skill}: Excellent performance.")
        elif score >= 70:
            feedback.append(f"{skill}: Good performance. Keep practicing.")
        elif score >= 50:
            feedback.append(f"{skill}: Average performance. More practice is needed.")
        else:
            feedback.append(f"{skill}: Needs improvement. Practice more problems.")

    return {
        "scores": scores,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "feedback": feedback
    }


if __name__ == "__main__":

    sample_data = {
        "Python": {
            "correct": 8,
            "total": 10
        },
        "Problem Solving": {
            "correct": 7,
            "total": 10
        },
        "Debugging": {
            "correct": 4,
            "total": 10
        }
    }

    result = analyze_response(sample_data)

    print("AI Skill Analysis")
    print("-----------------")
    print("Scores:", result["scores"])
    print("Strengths:", result["strengths"])
    print("Weaknesses:", result["weaknesses"])
    print("Feedback:", result["feedback"])