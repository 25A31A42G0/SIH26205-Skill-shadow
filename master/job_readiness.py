import json


def calculate_readiness(user_skills, job_name):

    with open("job_data.json", "r") as file:
        jobs = json.load(file)

    required_skills = jobs[job_name]

    total_score = 0
    total_required = 0

    for skill, required_score in required_skills.items():

        user_score = user_skills.get(skill, 0)

        total_score += min(user_score, required_score)
        total_required += required_score

    readiness = (total_score / total_required) * 100

    return round(readiness, 2)


if __name__ == "__main__":

    user_skills = {
        "Python": 80,
        "SQL": 40,
        "Excel": 75,
        "Statistics": 50
    }

    result = calculate_readiness(
        user_skills,
        "Data Analyst"
    )

    print("Job Readiness:", result, "%")