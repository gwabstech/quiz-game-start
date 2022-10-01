from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    newQ: Question = Question(question_text, question_answer)
    question_bank.append(newQ)

for q in question_bank:
    print(q.text, q.answer)
