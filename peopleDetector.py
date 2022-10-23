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
#cap = cv2.VideoCapture("/home/nmacgreg/Videos/Surveillance/2-02-20220828220249.mp4")
#cap = cv2.VideoCapture("/home/nmacgreg/Videos/Surveillance/2-03-20220828220352.mp4")
cap = cv2.VideoCapture("/home/nmacgreg/Videos/Surveillance/2-04-20220828220453.mp4")
#2-05-20220828221854.mp4
#2-06-20220828222648.mp4
#2-07-20220828223149.mp4
#2-08-20220828223313.mp4
#2-09-20220828223528.mp4
#2-10-20220828231126.mp4
#2-11-20220828231328.mp4
#2-12-20220828232618.mp4
#2-13-20220828232950.mp4
#KenzieFirstAcroComp.mp4

humanCount = 0
frameCount = 0
badResize=0
badGrayscale=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frameCount += 1

    try:
        frame = cv2.resize(frame, (640, 362))
    except: 
        badResize+=1
        print("Skipping bad frame, while resizing, frame: ", frameCount, "count: ",badResize)
        break
    # using a greyscale picture, also for faster detection
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    except: 
        badGrayscale+=1
        print("Skipping bad frame, while grayscaling, frame: ",frameCount, "count: ", badGrayscale)
        break

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(gray, winStride=(8,8) )

    for (x, y, w, h) in boxes:
        humanCount += 1
    

# When everything done, release the capture
cap.release()
cv2.waitKey(1)
print("Number of frames with humans detected: ", humanCount)
print("Total number of frames in the vid: ", frameCount)
print("Percentage: ", humanCount * 100 / frameCount )
