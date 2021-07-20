from PIL import ImageGrab
import cv2
from win32 import win32gui
import numpy as np
import time

def displayImage(windowname, image):
    cv2.imshow(windowname, image)
    cv2.waitKey(1)

def getscreen(windowname, offset, BoundsX, BoundsY):
    x,y,x2,y2 = win32gui.GetWindowRect(win32gui.FindWindow(0, windowname))
    
    offset = offset
    bounds = (x2/BoundsX-offset, y2/BoundsY-offset, x2/BoundsX+offset, y2/BoundsY+offset)
    image = ImageGrab.grab(bbox=(bounds))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    return image