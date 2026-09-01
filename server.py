from fastapi import FastAPI
from models import (
    UserCreate,
    SkillCreate,
    ChallengeCreate,
    ResultCreate,
    ResponseCreate,
    ProgressCreate
)
from database import get_connection, create_tables

app = FastAPI()

create_tables()


@app.get("/")
def home():
    return {"message": "Skill Shadow Backend is Running!"}


@app.post("/users")
def create_user(user: UserCreate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO users (name, email, target_job) VALUES (?, ?, ?)",
        (user.name, user.email, user.target_job)
    )

    connection.commit()
    user_id = cursor.lastrowid
    connection.close()

    return {
        
        "message": "User created successfully",
        "user_id": user_id
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )

    user = cursor.fetchone()
    connection.close()

    if user is None:
        return {"error": "User not found"}

    return dict(user)


@app.post("/skills")
def add_skill(skill: SkillCreate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO skills (user_id, skill_name, score) VALUES (?, ?, ?)",
        (skill.user_id, skill.skill_name, skill.score)
    )

    connection.commit()
    skill_id = cursor.lastrowid
    connection.close()

    return {
        "message": "Skill added successfully",
        "skill_id": skill_id
    }


@app.get("/skills/{user_id}")
def get_skills(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT skill_name, score FROM skills WHERE user_id = ?",
        (user_id,)
    )

    skills = cursor.fetchall()
    connection.close()

    return [dict(skill) for skill in skills]


@app.post("/challenges")
def create_challenge(challenge: ChallengeCreate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO challenges (title, skill, difficulty) VALUES (?, ?, ?)",
        (challenge.title, challenge.skill, challenge.difficulty)
    )

    connection.commit()
    challenge_id = cursor.lastrowid
    connection.close()

    return {
        "message": "Challenge created successfully",
        "challenge_id": challenge_id
    }


@app.get("/challenges")
def get_challenges():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM challenges")

    challenges = cursor.fetchall()
    connection.close()

    return [dict(challenge) for challenge in challenges]


@app.post("/results")
def create_result(result: ResultCreate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO results (user_id, challenge_id, score) VALUES (?, ?, ?)",
        (result.user_id, result.challenge_id, result.score)
    )

    connection.commit()
    result_id = cursor.lastrowid
    connection.close()

    return {
        "message": "Result saved successfully",
        "result_id": result_id
    }


@app.get("/results/{user_id}")
def get_results(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM results WHERE user_id = ?",
        (user_id,)
    )

    results = cursor.fetchall()
    connection.close()

    return [dict(result) for result in results]

@app.post("/responses")
def create_response(response: ResponseCreate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO responses (user_id, challenge_id, response) VALUES (?, ?, ?)",
        (response.user_id, response.challenge_id, response.response)
    )

    connection.commit()
    response_id = cursor.lastrowid
    connection.close()

    return {
        "message": "Response saved successfully",
        "response_id": response_id
    }


@app.get("/responses/{user_id}")
def get_responses(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM responses WHERE user_id = ?",
        (user_id,)
    )

    responses = cursor.fetchall()
    connection.close()

    return [dict(item) for item in responses]

@app.post("/progress")
def create_progress(progress: ProgressCreate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO progress (user_id, completed_challenges, total_score) VALUES (?, ?, ?)",
        (
            progress.user_id,
            progress.completed_challenges,
            progress.total_score
        )
    )

    connection.commit()
    progress_id = cursor.lastrowid
    connection.close()

    return {
        "message": "Progress saved successfully",
        "progress_id": progress_id
    }


@app.get("/progress/{user_id}")
def get_progress(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM progress WHERE user_id = ?",
        (user_id,)
    )

    progress = cursor.fetchall()
    connection.close()

    return [dict(item) for item in progress]    