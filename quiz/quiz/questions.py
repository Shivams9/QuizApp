class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answer

    def __str__(self) -> str:
        return "{0}".format(self.question)
