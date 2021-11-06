#!/bin/python
import cv2
from json import  load

with open("credentials.json") as creds:
    data = load(creds)

# open webcam video stream
cap = cv2.VideoCapture("rtsp://" + data["userid"] + ":" + data["password"]+ "@camera1/Streaming/channels/101")


while True:
    ret, img = cap.read()
    if ret == True:
        cv2.imshow('video output', img)
        k = cv2.waitKey(10)& 0xff
        if k == 27:
            break
cap.release()
cv2.destroyAllWindows()
