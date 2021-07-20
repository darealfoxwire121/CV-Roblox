from ROI import *
from line_detect import *
from GUI import *
import math

def mainloop(windowname):
    showGUI()
    
    while True:
        image = getscreen(windowname, 200, 2, 2)
        FinalImage = draw_lines(image, detect_lines(image, 50, 10, 200))

        displayImage(windowname, image=FinalImage) 

mainloop("File Explorer")