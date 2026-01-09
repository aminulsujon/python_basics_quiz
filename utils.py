import json

FILE_PATH = "data/questions.json"

def add_question():
    question = input("Enter the question: ")
    options = []
    for i in range(4):
        opt = input(f"Option {i+1}: ")
        options.append(opt)
    answer = input("Enter the correct answer (exactly as typed in options): ")

    new_question = {
        "question": question,
        "options": options,
        "answer": answer
    }

    try:
        with open(FILE_PATH, "r") as f:
            questions = json.load(f)
    except FileNotFoundError:
        questions = []

    questions.append(new_question)

    with open(FILE_PATH, "w") as f:
        json.dump(questions, f, indent=4)

    print("Question added successfully!")
