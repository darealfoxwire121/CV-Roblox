import cv2
from tkinter import *
from tkinter.ttk import *

Tk = Tk()

def getScaleLine():
    pass

def showGUI():
    Tk.wm_title("Roblox-CV")
    Tk.wm_geometry('300x200+500+200')
    Init = Scale(Tk, from_=0, to=100, orient=HORIZONTAL)
    Init.set(100)

    nameInit = Label(Tk, text="Line Detection")

    nameInit.pack()
    Init.pack(side=TOP)
    Tk.mainloop()