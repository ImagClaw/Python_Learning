#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Write a gui program to do temp calulations
#   for fehrenheit and celsius.
#   Date: 4/29/2019

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "Fehrenheit").grid(row = 0, column = 0, sticky = W)
        Label(self, text = "Celsius").grid(row = 0, column = 3, sticky = E)

        self.fehr = Entry(self)
        self.fehr.grid(row = 2, column = 0, sticky = W)

        self.cel = Entry(self)
        self.cel.grid(row = 2, column = 3, sticky = E)

        self.fehrcalc = Button(self, text = "To Celsius", command = self.fehr2cel)
        self.fehrcalc.grid(row = 4, column = 0, sticky = W)
        
        self.celscalc = Button(self, text = "To Fehrenheit", command = self.cel2fehr)
        self.celscalc.grid(row = 4, column = 3, sticky = E)

    def fehr2cel(self):     # (32°F − 32) × 5/9
        celsius = ((int(self.fehr.get())-32) * (5/9))
        
        self.cel.delete("0", "end")
        self.cel.insert("0", "{cel:.2f}".format(cel=float(celsius)))

    def cel2fehr(self):     # (32°C × 9/5) + 32
        fehrenheit = ((int(self.cel.get()) * (9/5)) + 32)
        
        self.fehr.delete("0", "end")
        self.fehr.insert("0", "{fehr:.2f}".format(fehr=float(fehrenheit)))


# main
root = Tk()
root.title("Tempurature Calculator")
app = Application(root)
root.mainloop()