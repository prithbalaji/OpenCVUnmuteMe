from imutils import face_utils
import cv2
import sys
import dlib
import imutils
import numpy as np

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#cap = cv2.VideoCapture('Test.MOV') #this is a local path will not run
cap = cv2.VideoCapture(0) # takes input from default webcam

OPEN = "open"
CLOSED = "closed"

top_mouth_range = [(61, 64)]#, (49, 54)] we only care about inner lips
bottom_mouth_range = [(65, 68)] #(55, 60)]

mouth_open_threshold = 5

def initialize_capture():
    global cap
    cap = cv2.VideoCapture(0) 
    if cap is None or not cap.isOpened():
        return False
    return True

def clear_capture():
    global cap
    cap.release()
    cv2.destroyAllWindows()

def get_mouth_state():
#while True:
    global cap
    if not cap.isOpened():
        return None
    ret, frame  = cap.read()

    image = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 1)

    for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # convert dlib's rectangle to a OpenCV-style bounding box
        # [i.e., (x, y, w, h)], then draw the face bounding box
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # show the face number
        cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # calculate average y positions of top and bottom lip
        average_top_y = 0
        total_points = 0
        for (j, k) in top_mouth_range:
            shape_sub_arr = shape[j:k]
            for (x, y) in shape_sub_arr:
                cv2.circle(image, (x, y), 1, (255, 0, 0), -1)
                average_top_y += y
                total_points += 1
        average_top_y /= total_points

        average_bottom_y = 0
        total_points = 0
        for (j, k) in bottom_mouth_range:
            shape_sub_arr = shape[j:k]
            for (x, y) in shape_sub_arr:
                cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
                average_bottom_y += y
                total_points += 1
        average_bottom_y /= total_points

        # set lip state based on threshold
        face_state = CLOSED
        if 100 * abs(average_top_y - average_bottom_y)/h > mouth_open_threshold:
            face_state = OPEN

        # show face state
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.putText(image, "Face State {}".format(face_state), (w + x - 100, h + y + 15),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        #cv2.imshow('frame',image)
        return face_state == OPEN

    #cv2.imshow('frame',image)

    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

    #return [face_state == OPEN, image]

#cap.release()
#cv2.destroyAllWindows()

