from PIL import ImageGrab
import cv2
from win32 import win32gui
import numpy as np

def displayImage(windowname, image):
    cv2.imshow(windowname, image)
    cv2.waitKey(0)

def getscreen(windowname, offset, BoundsX, BoundsY):
    x,y,x2,y2 = win32gui.GetWindowRect(win32gui.FindWindow(0, windowname))
    
    offset = offset
    bounds = (x2/BoundsX-offset, y2/BoundsY-offset, x2/BoundsX+offset, y2/BoundsY+offset)
    image = ImageGrab.grab(bbox=(bounds))
    return image