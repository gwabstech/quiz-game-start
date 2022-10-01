class Quiz:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def nextQuestion(self):
        self.question_number += 1
        t = self.question_list[self.question_number]
        option = input(f"{t.text}: True or False").upper()

    def hasNext(self):
        if self.question_number < len(self.question_list):
            return True

    def play(self):
        while self.hasNext():
            self.nextQuestion()
