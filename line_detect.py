import cv2
import numpy as np
import math

def get_lines(image):
    lines_list = cv2.HoughLines(np.array(image), 1, np.pi / 180, 150, None, 0, 0)    
    return lines_list

def add_canny(image):
    canny = cv2.Canny(np.array(image), 50, 200, None, 3)
    return canny

def draw_lines(image, lines_list):
    if lines_list is not None:
        for line in range(0, len(lines_list)):
            rho = lines_list[line][0][0]
            theta = lines_list[line][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(-b)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(-b)))

            cv2.line(np.array(image), pt1, pt2, (255, 255, 255), 3, cv2.LINE_AA)
            return image

def detect_lines(image):
    canny = add_canny(image)
    lines = get_lines(canny)
    return lines
