import json

categories = [
    "Basics", "Variables", "Data Types", "Operators", "Conditionals",
    "Loops", "Functions", "Lists", "Tuples", "Sets",
    "Dictionaries", "Strings", "File Handling", "JSON",
    "Modules", "Random", "Error Handling", "OOP", "Advanced Basics"
]

hardness_levels = ["Easy", "Medium", "Hard"]

questions = []

for i in range(1, 501):
    questions.append({
        "question": f"Sample Python question number {i}?",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "answer": "Option A",
        "category": categories[i % len(categories)],
        "hardness": hardness_levels[i % len(hardness_levels)]
    })

with open("questions_500.json", "w") as f:
    json.dump(questions, f, indent=4)

print("✅ 500-question JSON file created!")
