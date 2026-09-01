def recommend(gaps):
    recommendations = []

    for skill in gaps:
        recommendations.append(
            f"Improve your {skill} skills"
        )

    return recommendations


if __name__ == "__main__":
    gaps = {
        "SQL": 30,
        "Statistics": 10
    }

    recommendations = recommend(gaps)

    print("Recommendations:")

    for item in recommendations:
        print("-", item)