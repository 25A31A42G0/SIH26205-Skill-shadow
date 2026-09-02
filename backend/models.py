from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    target_job: str | None = None


class SkillCreate(BaseModel):
    user_id: int
    skill_name: str
    score: float = 0


class ChallengeCreate(BaseModel):
    title: str
    skill: str
    difficulty: str


class ResultCreate(BaseModel):
    user_id: int
    challenge_id: int
    score: float
class ResponseCreate(BaseModel):
    user_id: int
    challenge_id: int
    response: str


class ProgressCreate(BaseModel):
    user_id: int
    completed_challenges: int = 0
    total_score: float = 0    