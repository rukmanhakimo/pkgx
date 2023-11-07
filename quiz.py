class Question:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

    def check_answer(self, user_choice):
        return user_choice == self.correct_choice

# List of questions
questions = [
    Question("What is the capital of Indonesia?", ["Jakarta", "Surabaya", "Bandung", "Medan"], "Jakarta"),
    Question("Who discovered gravity?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"], "Isaac Newton"),
    Question("How many planets are there in the solar system?", ["7", "8", "9", "10"], "8"),
    Question("Who is the author of the novel '1984'?", ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.K. Rowling"], "George Orwell"),
]

def run_quiz(questions):
    score = 0

    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question.text}")
        for j, choice in enumerate(question.choices, start=1):
            print(f"{j}. {choice}")
        user_choice = input("Enter the number of your answer: ")
        if question.check_answer(question.choices[int(user_choice) - 1]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {question.correct_choice}\n")

    print(f"You got {score} out of {len(questions)} questions correct!")

if __name__ == "__main__":
    run_quiz(questions)