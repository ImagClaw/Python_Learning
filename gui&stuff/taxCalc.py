#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Write a gui program to do tax calculation
#   with dependents as input.
#   Date: 4/29/2019

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    

    def create_widgets(self):
        Label(self, text = "Gross Income -> ").grid(row = 0, column = 0, sticky = W)
        Label(self, text = "# of Dependents - >").grid(row = 2, column = 0, sticky = W)

        self.income = Entry(self)
        self.income.grid(row = 0, column = 1, sticky = W)

        self.dependents = Entry(self)
        self.dependents.grid(row = 2, column = 1, sticky = W)

        Button(self, text = "Compute", command = self.calculate).grid(row = 3, column = 1, sticky = W)

        Label(self, text = "Total Tax ->").grid(row = 6, column = 0, sticky = W)
        self.text = Text(self, width = 10, height = 1, wrap = WORD)
        self.text.grid(row = 6, column = 1, sticky=W)

    def calculate(self):
        tax = (int(self.income.get()) *.064) + (int(self.dependents.get()) *100)

        self.text.delete(0.0, END)
        self.text.insert(0.0, tax)



root = Tk()
root.title("Tax Calculation")
app = Application(root)
root.mainloop()