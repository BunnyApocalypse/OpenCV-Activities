__author__ = 'kingc3'
import numpy as np
import cv2

origIm = cv2.imread('TestImages/Coins1.jpg')
imgray = cv2.cvtColor(origIm,cv2.COLOR_BGR2GRAY)
imgray = cv2.blur(imgray, (3,3))
imgray = cv2.morphologyEx(imgray, cv2.MORPH_OPEN, cv2.MORPH_RECT, (10,80))
ret,thresh = cv2.threshold(imgray,127,255,0)
im2, contrs, hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgray, contrs, -1, (0,255,0), 3)
cv2.imshow("woo",imgray)
cv2.waitKey(0)
