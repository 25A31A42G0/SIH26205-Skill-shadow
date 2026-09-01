import json


def load_challenges():
    with open("challenges/challenges.json", "r") as file:
        return json.load(file)


def get_challenges_by_skill(skill):
    challenges = load_challenges()

    return [
        challenge
        for challenge in challenges
        if challenge["skill"].lower() == skill.lower()
    ]


def get_challenge(skill, level="Beginner"):
    challenges = get_challenges_by_skill(skill)

    for challenge in challenges:
        if challenge["level"].lower() == level.lower():
            return challenge

    return None
    