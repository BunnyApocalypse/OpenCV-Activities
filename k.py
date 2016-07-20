import cv2
import numpy
import random

feed = cv2.VideoCapture(0)
while True:

    ret, img1 = feed.read()
    (bc, gc, rc) = cv2.split(img1)
    channelList = [bc, gc, rc]
    random.shuffle(channelList)
    coloring = cv2.merge(channelList)
    cv2.imshow("wow",coloring)
    x = cv2.waitKey(10)
    userChar = chr(x & 0xFF)

    if userChar == 'q':
        break