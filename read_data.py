import cv2 
import numpy as np

<<<<<<< HEAD
cap = cv2.VideoCapture('Test.MOV')
=======
cap = cv2.VideoCapture('Test.MOV')#this is a local path will not run
>>>>>>> 3bf6ec98cf4bac70c95bac9e8e2c067f6e0464ef


while True:
        ret, frame  = cap.read()


        cv2.imshow('frame',frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


<<<<<<< HEAD


=======
>>>>>>> 3bf6ec98cf4bac70c95bac9e8e2c067f6e0464ef
cap.release()
cv2.destroyAllWindows()

