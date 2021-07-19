from ROI import *
from line_detect import *
from GUI import *
import math

def mainloop(windowname):
    while True:
        image = getscreen(windowname, 200, 2, 2)
        FinalImage = draw_lines(np.array(image), detect_lines(np.array(image)))
        
        displayImage(windowname, np.array(FinalImage))

mainloop("Lightshot")