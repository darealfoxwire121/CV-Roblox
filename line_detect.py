import cv2
import numpy as np
import math

def get_lines(image, minlength, gap, thresh):
    lines_list = cv2.HoughLinesP(image, 1, np.pi / 180, minLineLength=minlength, maxLineGap=gap, threshold=thresh)
    return lines_list

def add_canny(image):
    color = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, Thresh = cv2.threshold(color, 100, 150, cv2.THRESH_BINARY)

    canny = cv2.Canny(Thresh, 50, 150)
    return canny

def draw_lines(image, lines_list):
    if lines_list is not None:
        for i in range(0, len(lines_list)):
            line_arr = lines_list[i][0]
            
            cv2.line(image, (line_arr[0], line_arr[1]), (line_arr[2], line_arr[3]), (255, 100, 100), 3, cv2.LINE_AA)
    else:
        pass
        # print("No lines found")
        
    return image

def detect_lines(image, minlength, gap, thresh):
    canny = add_canny(image)
    lines = get_lines(canny, minlength, gap, thresh)
    return lines
