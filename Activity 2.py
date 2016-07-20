__author__ = 'huangb3'
import cv2
import random
import numpy

feed = cv2.VideoCapture(0)
while True:
    ret, img1 = feed.read()
    (bc, gc, rc) = cv2.split(img1)

    channelList = [bc, gc, rc]
    random.shuffle(channelList)
    colorImg = cv2.merge(channelList)

    x = cv2.waitKey(16)
    x = chr(x & 0xFF)
    if x == "q":
        break
    cv2.imshow("Webcam", colorImg)

cv2.destroyAllWindows()