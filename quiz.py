import json
import random

FILE_PATH = "data/questions.json"

def load_questions():
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def take_quiz():
    questions = load_questions()
    random.shuffle(questions)  # Randomize question order
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for i, opt in enumerate(q["options"], 1):
            print(f"{i}. {opt}")
        answer = input("Enter the number of your answer: ")

        # Validate input
        if not answer.isdigit() or int(answer) < 1 or int(answer) > len(q["options"]):
            print("Invalid choice. Skipping question.")
            continue

        if q["options"][int(answer)-1] == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

    print(f"\nYour final score: {score}/{len(questions)}")
