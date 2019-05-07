#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Write a gui to display "red", "white", "blue"... in those colors 
#   and give the message box a green background
#   Date: 4/29/2019

from tkinter import *

window = Tk()

window.title("'Merica Colors")

window.geometry('355x310')

redlbl = Label(window, text="red", fg="red", bg="green", font=("Helvetica", 32), width=14, height=2, justify=CENTER)
redlbl.grid(row=0)
whtlbl = Label(window, text="white", fg="white", bg="green", font=("Helvetica", 32), width=14, height=2, justify=CENTER)
whtlbl.grid(row=1)
blulbl = Label(window, text="blue", fg="blue", bg="green", font=("Helvetica", 32), width=14, height=2, justify=CENTER)
blulbl.grid(row=2)


window.mainloop()