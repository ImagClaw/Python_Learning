from questions import Questions
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

import os, json


master = Tk()
master.geometry("500x400")
master.title("Python3 Quiz")
header = Label(master, text="*****************************************\nWELCOME to...\nTHE QUIZ...\nDUN DUN DUUUUN!\n*****************************************", justify="center")
header.destroy()
menubar = Menu(master)

questions = []

def donothing():
   pass

def openQuiz():
    # asks user to open a file and defaults the filetype as JSON
    fname = fd.askopenfilename(initialdir=os.getcwd(), title="Select file...", filetypes=[("JSON", "*.json")])
    return fname

def getQuestions():
    ques = openQuiz()
    try:
        fname = open(ques)
        quiz = json.load(fname)
        fname.close()
    except FileNotFoundError:
        mb.showerror("File Error","Missing/Invalid File")
        # self.main.destroy()
    except ValueError:
        mb.showerror("File Error","Missing/Invalid File")
    
    for i in quiz['questions']:
        questions.append(i)


def about():
    aboutwin = Toplevel(master)
    aboutwin.geometry("400x100")
    aboutwin.title("About Us!")
    label = Label(aboutwin, text="\nPYTHON3 QUIZ CONVERTED FROM A C PROGRAM\n\nDEVELOPED BY MEJIA, OGDEN, AND WHELPLEY\n\n********************* BEST OF LUCK ***********************\n", justify='center')
    label.pack()


def help():  
    helpwin = Toplevel(master)  
    helpwin.geometry("375x70")  
    helpwin.title("Help")  
    label = Label(helpwin, text="What do you need help for?  It's a quiz...\nYou need to get above an 80% to pass.\nThe main window should've been enough to get you going.\nL2Read && Follow the prompts.", justify="center")  
    label.pack()
   

def startQuiz():
    Label(master, text="red", fg="red", bg="green", font=("Helvetica", 32), width=14, height=2, justify=CENTER)
    Label(master, text="white", fg="white", bg="green", font=("Helvetica", 32), width=14, height=2, justify=CENTER)
    Label(master, text="blue", fg="blue", bg="green", font=("Helvetica", 32), width=14, height=2, justify=CENTER) 

# File menu
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)

# File menu options
filemenu.add_command(label ="Open Quiz", command = getQuestions)
filemenu.add_command(label = "Start Quiz", command = startQuiz)

filemenu.add_separator()
filemenu.add_command(label = "Exit", command = master.quit)

# Edit menu
scoremenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Scores", menu = scoremenu)

# Edit menu options
scoremenu.add_command(label ="High Scores", command = donothing)
scoremenu.add_command(label ="Reset Scores", command = donothing)


# Help menu
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Help", menu = helpmenu)

# Help menu options
helpmenu.add_command(label = "Help...", command = help)
helpmenu.add_command(label = "About...", command = about)

master.config(menu = menubar)
master.mainloop()