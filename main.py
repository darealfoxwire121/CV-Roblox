from ROI import *
from line_detect import *
from GUI import *
import math

def mainloop(windowname):
    showGUI()
    
    while True:
        image = getscreen(windowname, 200, 2, 2)
        FinalImage = draw_lines(image, detect_lines(image))

        displayImage(windowname, image=FinalImage) 

mainloop("Lightshot")