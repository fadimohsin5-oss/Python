class Question:

    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer


def run_quiz():

    questions = [
        Question(
            "1. What is the capital of England?",
            ["A. London", "B. Paris", "C. Rome", "D. Madrid"],
            "A"
        ),
        Question(
            "2. Which planet is known as the Red Planet?",
            ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "B"
        ),
        Question(
            "3. What is 5 + 3?",
            ["A. 6", "B. 7", "C. 8", "D. 9"],
            "C"
        ),
        Question(
            "4. Which language are we using to create this quiz?",
            ["A. Java", "B. C++", "C. HTML", "D. Python"],
            "D"
        ),
        Question(
            "5. Which animal is known as the King of the Jungle?",
            ["A. Tiger", "B. Lion", "C. Elephant", "D. Bear"],
            "B"
        )
    ]

    score = 0

    print("================================")
    print("      WELCOME TO THE QUIZ!")
    print("================================")
    print("Choose A, B, C, or D.")
    print()

    for q in questions:
        print(q.question)

        for option in q.options:
            print(option)

        while True:
            answer = input("Your answer: ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid choice! Please enter A, B, C, or D.")

        if answer == q.answer:
            print("Correct! Well done!")
            score += 1
        else:
            print("Incorrect!")
            print("Correct answer:", q.answer)

        print()

    total = len(questions)
    percentage = (score / total) * 100

    print("================================")
    print("          QUIZ RESULTS")
    print("================================")
    print("Your score:", score, "out of", total)
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent work!")
    elif percentage >= 50:
        print("Good job! Keep practising.")
    else:
        print("Keep learning and try again!")

    print("Thank you for playing!")


run_quiz()