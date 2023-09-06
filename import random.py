import random

# Define your flashcards as a dictionary with questions as keys and answers as values.
flashcards = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the chemical symbol for gold?": "Au",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the symbol for the element oxygen?": "O",
}

# Function to start the flashcard quiz
def flashcard_quiz():
    print("Welcome to the Flashcard Quiz!")
    print("Type 'exit' to quit the quiz.")

    while True:
        # Select a random flashcard
        question, answer = random.choice(list(flashcards.items()))

        # Display the question and prompt for user input
        user_input = input(f"Question: {question}\nYour Answer: ").strip().lower()

        # Check if the user wants to exit
        if user_input == 'exit':
            print("Thanks for playing!")
            break

        # Check if the user's answer is correct
        if user_input == answer.lower():
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is: {answer}\n")

if __name__ == "__main__":
    flashcard_quiz()
