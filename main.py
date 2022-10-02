from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    newQ: Question = Question(question_text, question_answer)
    question_bank.append(newQ)

quiz = Quiz(question_bank)


def play():
    while quiz.hasNext():
        quiz.nextQuestion()


play()
print(f"Your final score is {quiz.score}")
option = input("Game Over.... type ( R ) to restart the quiz or type (Q) to exit")
if option.upper() == "R":
    quiz.restart()
    play()

else:
    print("Bye You exit the game")
