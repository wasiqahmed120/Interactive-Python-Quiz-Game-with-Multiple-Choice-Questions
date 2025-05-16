# quiz_game.py

def load_questions():
    """Load quiz questions and options."""
    return [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Rome", "D) Berlin"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A) Charles Dickens", "B) J.K. Rowling", "C) William Shakespeare", "D) Mark Twain"],
            "answer": "C"
        }
    ]

def start_quiz():
    """Start the quiz game."""
    print("\n🎮 Welcome to the Python Quiz Game!\n")
    questions = load_questions()
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("\nYour answer (A, B, C, D): ").strip().upper()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

    print(f"\n🎯 You scored {score} out of {len(questions)}.")

def main():
    while True:
        start_quiz()
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("\n✅ Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
