import challenges.challenge_engine as challenge_engine
from challenges.evaluator import evaluate_answer
from challenges.recommendations import find_weak_skill, recommend_challenge

print("===== SKILL SHADOW TEST =====")

# 1. Load challenges
challenges = challenge_engine.load_challenges()
print("1. Challenges loaded:", len(challenges))

# 2. Get Python challenges
python_challenges = challenge_engine.get_challenges_by_skill("Python")
print("2. Python challenges:", len(python_challenges))

# 3. Get beginner Python challenge
challenge = challenge_engine.get_challenge("Python", "Beginner")
print("3. Beginner Python challenge:", challenge["title"])

# 4. Evaluate answer
answer = "Use max() to find the largest number in a list."
keywords = ["max", "largest", "list"]

result = evaluate_answer(answer, keywords)

print("4. Answer score:", result["score"])
print("   Matched keywords:", result["matched_keywords"])

# 5. Find weak skill
skill_scores = {
    "Python": 80,
    "Java": 60,
    "JavaScript": 40
}

weak_skill = find_weak_skill(skill_scores)
print("5. Weak skill:", weak_skill)

# 6. Recommend challenge
recommended = recommend_challenge(
    skill_scores,
    challenge_engine
)

if recommended:
    print("6. Recommended challenge:", recommended["title"])
else:
    print("6. No challenge found")

print("===== TEST COMPLETED SUCCESSFULLY =====")