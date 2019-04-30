# import GUI library
from tkinter import *


# GUI config
root = Tk()
root.title("Simple GUI")
root.geometry("1080x720")


# variables
hiRow = 3


# definitions
def speak():
    Label(root, text="Hi",).grid(row=hiRow, column=0, sticky=W),
    hiRow + 1
def addButton():
    Button(root, text="Say 'Hi'", width=14, command=speak).grid(row=2, column=0, sticky=W)


# content
Label(root, text="This is my GUI").grid(row=0, column=0, sticky=W)

Button(root, text="Add Button", width=9, command=addButton).grid(row=1, column=0, sticky=W)


# start the GUI
root.mainloop()