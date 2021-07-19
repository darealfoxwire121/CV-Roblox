import cv2
import numpy as np
import math

def get_lines(image):
    lines_list = cv2.HoughLines(image, 1, np.pi / 180, 200)
    return lines_list

def add_canny(image):
    color = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, Thresh = cv2.threshold(color, 100, 150, cv2.THRESH_BINARY)

    canny = cv2.Canny(Thresh, 50, 150)
    return canny

def draw_lines(image, lines_list):
    if lines_list is not None:
        for line in lines_list:
            rho = line[0][0]
            theta = line[0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))

            cv2.line(image, pt1, pt2, (255, 100, 100), 3, 2)
    else:
        pass
        # print("No lines found")
        
    return image

def detect_lines(image):
    canny = add_canny(image)
    lines = get_lines(canny)
    return lines
