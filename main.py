from ROI import *
from line_detect import *
import math

def mainloop(windowname):
    while True:
        image = getscreen(windowname, 200, 2, 2)
        FinalImage = draw_lines(np.array(image), detect_lines(image))

        displayImage(windowname, FinalImage)
        

mainloop("File Explorer")