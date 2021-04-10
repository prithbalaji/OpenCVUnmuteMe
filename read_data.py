import cv2 
import sys
import numpy as np

cascPath = 'haarcascade.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
cap = cv2.VideoCapture(0) #cv2.VideoCapture('Test.MOV') #this is a local path will not run

while True:
    ret, frame  = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame',frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # # mouth detection
    # mouth_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_mcs_mouth.xml')

    # if mouth_cascade.empty():
    # raise IOError('Unable to load the mouth cascade classifier xml file')

    # cap = cv2.VideoCapture(0)
    # ds_factor = 0.5

    # while True:
    #     ret, frame = cap.read()
    #     frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #     mouth_rects = mouth_cascade.detectMultiScale(gray, 1.7, 11)
    #     for (x,y,w,h) in mouth_rects:
    #         y = int(y - 0.15*h)
    #         cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
    #         break

    #     cv2.imshow('Mouth Detector', frame)

    #     c = cv2.waitKey(1)
    #     if c == 27:
    #         break            

cap.release()
cv2.destroyAllWindows()

