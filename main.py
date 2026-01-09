from quiz import take_quiz
from utils import add_question

def main():
    while True:
        print("\n--- Python Basics Study App ---")
        print("1. Take Quiz")
        print("2. Add Your Own Question")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            take_quiz()
        elif choice == "2":
            add_question()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
