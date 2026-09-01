import json
from recommender import recommend


def analyze_gap(user_skills, job_name):

    with open("job_data.json", "r") as file:
        jobs = json.load(file)

    required_skills = jobs[job_name]

    gaps = {}

    for skill, required_score in required_skills.items():

        user_score = user_skills.get(skill, 0)

        if user_score < required_score:
            gaps[skill] = required_score - user_score

    return gaps


if __name__ == "__main__":

    user_skills = {
        "Python": 80,
        "SQL": 40,
        "Excel": 75,
        "Statistics": 50
    }

    result = analyze_gap(user_skills, "Data Analyst")

    print("Skill Gaps:")
    print(result)

    recommendations = recommend(result)

    print("\nRecommendations:")

    for item in recommendations:
        print("-", item)