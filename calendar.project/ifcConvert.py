#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project:    1) input gregorian date, output International Fixed Calendar.
#               2) output current date in human calendar format, and have it updated by system time.
#   Date:5/6/2019


from tkinter import *
import datetime, calendar

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.drawZgui()
    
    def drawZgui(self):
        Label(self, text = "Enter Gregorian date (YYYY/MM/DD) -> ").grid(row = 0, column = 0, sticky = W)

        self.gregorian = Entry(self)
        self.gregorian.grid(row = 0, column = 1, sticky = W)

        Button(self, text = "Convert", command = self.getGreg).grid(row = 3, column = 1, sticky = W)

        Label(self, text = "International Fixed Date ->").grid(row = 6, column = 0, sticky = W)
        self.text = Text(self, width = 15, height = 1, wrap = WORD)
        self.text.grid(row = 6, column = 1, sticky=W)

        Label(self, text="Current Gregorian Date:").grid(row = 13, column = 0, sticky = W)
        Label(self, text=datetime.datetime.now().strftime("%Y/%m/%d")).grid(row = 14, column = 0, sticky = W)

        Label(self, text="Current IFC Date:").grid(row = 13, column = 1, sticky = W)
        Label(self, text=self.convertZdate(datetime.datetime.now().strftime("%Y/%m/%d"))).grid(row = 14, column = 1, sticky = W)
    
    
    def getGreg(self):
        getGregDate = self.gregorian.get()
        getGregDate = self.convertZdate(getGregDate)

        self.text.delete(0.0, END)
        self.text.insert(0.0, getGregDate)
    
    def convertZdate(self, date):
        gregDate = (date)

        dateArr = str(gregDate).split("/")
        dateIn = datetime.date(int(dateArr[0]), int(dateArr[1]), int(dateArr[2]))

        if calendar.isleap(int(dateArr[0])) == True:
            dayofyear = dateIn.timetuple().tm_yday
            mon = (dayofyear/28)+1
            day = dayofyear % 28
            convDate = str(dateArr[0])+"/"+str(int(mon))+"/"+str(day-1)
            return convDate
            
        else:
            dayofyear = dateIn.timetuple().tm_yday
            mon = (dayofyear/28)+1
            day = dayofyear % 28
            convDate = str(dateArr[0])+"/"+str(int(mon))+"/"+str(day)
            return convDate
        
    


root = Tk()
root.title("International Fixed Calendar Converter")
app = Application(root)
root.mainloop()