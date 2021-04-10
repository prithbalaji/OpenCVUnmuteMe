import cv2
#import dlib
import numpy as np

cap = cv2.VideoCapture("Test.MOV")

while True:
    ret, frame = cap.read()
    roi = frame[620: 810, 600:750]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    _, threshold = cv2.threshold(gray_roi, 10 ,255, cv2.THRESH_BINARY_INV)
    cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Threshold", threshold)
    cv2.imshow("Roi", roi)
    key = cv2.waitKey(30)
    if key == 27:
        break
cv2.destroyAllWindows()

