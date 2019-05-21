from tkinter import *

class Questions():
    def __init__(self, question, incorrect_answers, correct_answer):
        self.question = question
        self.incorrect_answers = incorrect_answers
        self.correct_answer = correct_answer

        self.optionA = StringVar()
        self.optionB = StringVar()
        self.optionC = StringVar()
        self.optionD = StringVar()

        self.selectedAns = StringVar()
        self.correctAns = ""
        self.question = StringVar()

    def get_question(self):
        return self.question

    def get_correct_answer(self):
        return self.correct_answer
    
    def get_incorrect_answers(self):
        return self.incorrect_answers