from tkinter import messagebox
from tkinter import *
import json
import random


class ProgramGUI:
    def __init__(self):
        self.main = Tk()
        self.main.title('Python 3 Quiz')
        self.main.geometry('350x150')
        self.main.resizable(width=True, height=True)

        self.main.configure(bg='White', cursor='circle')

        self.main.attributes('-alpha', 1)
        self.main.attributes('-topmost', True)

        self.var = StringVar()
        self.label = Label(self.main, textvariable=self.var)
        self.label.pack()

        self.loadQuestion()
        """
        the constructor should end by doing
        Shuffle the items in the questions list to randomise the order of the questions.
        Call the class’s “loadQuestion()” method and to place the first question
        (and its answers) into the GUI and start the timer.tkinter.mainloop()
        """


##Sets the timer into label
        self.label = Label(self.main, textvariable=self.timer)
        self.label.pack()


        self.button1 = Button(self.buttonFrame, text=self.button.configure, command=self.clickCorrect)
        self.button1.pack(side='left')

        self.button2 = Button(self.buttonFrame)
        self.button2.pack(side='left')

        self.button3 = Button(self.buttonFrame)
        self.button3.pack(side='left')

        self.button4 = Button(self.buttonFrame)
        self.button4.pack(side='left')

        self.buttonFrame.pack(side='top')

        self.updateTimer() # call updateTimer as the program begins

        mainloop()


    def loadQuestion(self):
        questions = getQuestions()
        for i, que in enumerate(questions):
            self.var.set(que['question']).random.shuffle()

        self.buttonList = []
        self.buttonList.append(self.button1)
        self.buttonList.append(self.button2)
        self.buttonList.append(self.button3)
        self.buttonList.append(self.button4)

    def clickCorrect(self):
        self.score = 0
        if not self.buttonclicked:
            self.timer.set(self.timer.get() - 1)
        else:
            score += score
            if self.timer.get() == 0:
                self.button1.configure(text=self.question['correct_answer'], command=self.clickCorrect)
                messagebox.showinfo('Game Over', 'Score:', score)

    def ClickWrong(self):
        self.button2.configure(text=self.questions['incorrect_answer'][0], command=self.clickWrong)
        self.button2.configure(text=self.questions['incorrect_answer'][1], command=self.clickWrong)
        self.button2.configure(text=self.questions['incorrect_answer'][2], command=self.clickWrong)

    def getQuestions(self):
        questions = None
        try:
            file = open("questions.json", "r")
            questions = json.load(file)
            file.close()
        except FileNotFoundError:
            messagebox.showerror("File Error","Missing/Invalid File")
            # self.main.destroy()
        except ValueError:
            messagebox.showerror("File Error","Missing/Invalid File")
        return questions


gui = ProgramGUI()