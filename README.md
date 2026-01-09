# 🐍 Python Basic Quiz

## 📘 Project Description
**Python Basics Quiz** is an interactive command-line application designed to help beginners practice core Python concepts.  
The app stores quiz data, makes decisions, repeats tasks, and responds to user input in real time.

---

## Run the quiz app
- python3 main.py

## 🎯 Features
- Interactive quiz system
- Add your own questions
- Randomized question order
- Persistent data storage using JSON
- Beginner-friendly project structure

---

## 🧩 Concepts Covered

### 1. `main.py`
Acts as the controller of the application.  
Displays the menu and directs the program flow based on user input.

---

### 2. Variables & Data Types
Uses core Python data types:
- `int` – scores, counters
- `str` – questions, answers, user input
- `list` – multiple-choice options
- `dict` – structured question data

---

### 3. Functions
- `take_quiz()` – runs the quiz and calculates the score  
- `add_question()` – allows users to add new quiz questions  

Functions help organize code and avoid repetition.

---

### 4. Conditionals (`if / elif / else`)
Used to:
- Handle menu choices
- Check whether answers are correct or incorrect

---

### 5. Loops (`for`)
Used to:
- Display multiple-choice options
- Iterate through quiz questions

---

### 6. Operators (Comparisons)
Comparison operators (`==`, `!=`) are used to compare user answers with correct answers.

---

### 7. File I/O (JSON)
- Loads quiz questions from a JSON file
- Saves new questions for future use  
This ensures data persists even after closing the app.

---

### 8. Randomization
Uses `random.shuffle()` to change the order of questions for each quiz attempt, making the experience more engaging.

---

## ▶️ How to Run
```bash
python main.py
