#!/usr/bin/python

# import the necessary packages
import numpy as np
import cv2
from json import  load

with open("credentials.json") as creds:
    data = load(creds)
 
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

# open webcam video stream
#cap = cv2.VideoCapture("rtsp://" + data["userid"] + ":" + data["password"]+ "@camera1/Streaming/channels/102")
#cap = cv2.VideoCapture("/home/nmacgreg/Videos/Surveillance/KenzieFirstAcroComp.mp4")
#cap = cv2.VideoCapture("/home/nmacgreg/Videos/Surveillance/2-01-20220828220133.mp4")
cap = cv2.VideoCapture("/home/nmacgreg/Videos/Surveillance/2-02-20220828220249.mp4")
#2-03-20220828220352.mp4
#2-04-20220828220453.mp4
#2-05-20220828221854.mp4
#2-06-20220828222648.mp4
#2-07-20220828223149.mp4

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # resizing for faster detection
    frame = cv2.resize(frame, (640, 362))
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(gray, winStride=(8,8) )

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Kenzie\'s first comp',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
# and release the output
#out.release()
# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)
