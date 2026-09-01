def find_weak_skill(skill_scores):
    if not skill_scores:
        return None

    weak_skill = min(skill_scores, key=skill_scores.get)

    return weak_skill


def recommend_challenge(skill_scores, challenge_engine):
    weak_skill = find_weak_skill(skill_scores)

    if weak_skill is None:
        return None

    challenge = challenge_engine.get_challenge(
        weak_skill,
        "Beginner"
    )

    return challenge