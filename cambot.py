'''
Zak Mineiko
Created: 2/4/2021
Modified: 10/22/2022

Robotic Camera Man

This is a color-based object detection algorithm used to control
servos on an Arduino to make an automatic camera man effectively
always ensuring the camera stays pointed at a subject!
'''

from collections import deque
import cv2
import numpy as np
import serial
import imutils
import time
import argparse
ser = serial.Serial('/dev/cu.usbmodem143301', 9600) # usb port for serial comm
pos=90
ser.write(90) # set servo's intial position
# set up live video
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=32,
	help="max buffer size")
args = vars(ap.parse_args())
# set lower and upper bound for the reference frame
lowerBound=np.array([29, 86, 6])
upperBound=np.array([64, 255, 255])

# set vars
pts = deque(maxlen=args["buffer"])
counter = 0
(dX, dY) = (0, 0)
direction = ""
cam = cv2.VideoCapture(1)
# for on screen text
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor=(255,255,255)

numb = np.arange(1,100,1)
def sendValue(ex):
    ex = nx
    ex =str(ex)
    ex =ex.encode()
    if nx<55:
        pos+=2
        ser.write(pos)
    time.sleep(.01)


while True:
    ret, img = cam.read()
    # for font, ended up causing issues
    #ont= cv2.putText(img, str('MANDOLORIAN SUCKS'), (100,100), fontFace, fontScale, fontColor)
    # do operations on image to make object more detectable
    img = cv2.resize(img, (540,590))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(imgHSV, lowerBound, upperBound)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # setup contours
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None
    
    # draw border around object 
    if len(cnts)>0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        x1=int((x/540)*180)
        # move servo only in certain threshold
        if x1<75:
            pos+=2
            xx=pos
            xx=str(xx)
            xx=xx.encode()
            ser.write(xx)
        if x1>105:
            pos-=2
            xx=pos
            xx=str(xx)
            xx=xx.encode()
            ser.write(xx)
        print(x1)

		# only proceed if the radius meets a minimum size
        if radius > 10:
            cv2.circle(img, center, 5, (0, 0, 255), -1)
            pts.appendleft(center)
        
    cv2.imshow("mask", mask)
    cv2.imshow("cam", img)
    
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

    
