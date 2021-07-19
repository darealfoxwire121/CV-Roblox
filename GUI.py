import cv2
from tkinter import *

Tk = Tk()

def showGUI():
    Tk.wm_title("Roblox-CV")
    Tk.wm_geometry('300x400+500+200')
    #insert icon for window
    Init = Button(Tk, text = "Start Roblox-CV", padx = 10, pady = 10, )
    Init.pack(side=LEFT)
    Tk.mainloop()
