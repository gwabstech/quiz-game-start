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
while quiz.hasNext():
    quiz.nextQuestion()



