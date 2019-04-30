# import gui library
from tkinter import *

gui = Tk()
gui.title("Simple GUI")
gui.geometry("1080x720")
hiRow = 3


def addHiRow():
    hiRow += 1
def speak():
    Label(gui, text="Hi",).grid(row=hiRow, column=0, sticky=W),
    addHiRow()
def addButton():
    Button(gui, text="Say 'Hi'", width=14, command=speak()).grid(row=2, column=0, sticky=W)


# add a label
Label(gui, text="This is my GUI").grid(row=0, column=0, sticky=W)

# add a button
Button(gui, text="Add Button", width=9, command=addButton).grid(row=1, column=0, sticky=W)

# start the gui
gui.mainloop()