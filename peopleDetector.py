#!/usr/bin/python

# import the necessary packages
import numpy as np
import cv2
from json import load

with open("credentials.json") as creds:
    data = load(creds)
 
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# open a local file
#cap = cv2.VideoCapture("/home/nmacgreg/Videos/Surveillance/KenzieFirstAcroComp.mp4")
cap = cv2.VideoCapture("/home/nmacgreg/Videos/Surveillance/2-02-20220828220249.mp4")


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.resize(frame, (640, 362))
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(gray, winStride=(8,8) )

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes:
        print ("HumanDetected")
    

# When everything done, release the capture
cap.release()
cv2.waitKey(1)
