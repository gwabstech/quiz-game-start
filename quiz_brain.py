class Quiz:
    score = 0
    option = ""

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def nextQuestion(self):
        self.question_number += 1
        t = self.question_list[self.question_number]
        self.option = input(f"{t.text}: True or False").upper()
        self.checkAnswer()

    def hasNext(self):
        return self.question_number < len(self.question_list) - 1

    def checkAnswer(self):
        answer = self.question_list[self.question_number].answer

        if self.option.capitalize() == str(answer).capitalize():
            self.score += 10
            print("Yes you got it right")
        else:
            print("Wrong")

    def restart(self):
        self.score = 0
        self.question_number = 0


