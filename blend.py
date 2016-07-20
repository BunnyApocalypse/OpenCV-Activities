__author__ = 'kingc3'
import cv2
import numpy as np
x = .1
y = (1.0-x)
feed = cv2.VideoCapture(0)
ret, image2 = feed.read()
image1 = cv2.imread("TestImages/SnowLeo1.jpg")
(hgt1, wid1, dep1) = image1.shape
(hgt2, wid2, dep2) = image2.shape
newWid = min(wid1, wid2)
newHgt = min(hgt1, hgt2)
image1Crop = image1[0:newHgt, 0:newWid]
image2Crop = image2[0:newHgt, 0:newWid]
cv2.imshow("Im1 Cropped", image1Crop)
cv2.imshow("Im2 Cropped", image2Crop)
cv2.waitKey(0)
while x<.9:
    ret, image2 = feed.read()
    blended = cv2.addWeighted(image1Crop,y,image2Crop,x,0)
    cv2.imshow("Image1 cropped", blended)
    cv2.waitKey(30)
    x+=.009

ret, rawframe = feed.read()
frame=rawframe[0:newHgt, 0:newWid]
prevPic= [frame] * 10
while True:
    ret, curImg = feed.read()
    blurred=cv2.addWeighted(prevPic[0], .3,curImg,.7,0)
    cv2.imshow("blur echo", blurred)
    x = cv2.waitKey(10)
    userChar = chr(x & 0xFF)
    if userChar == 'q':
        break
    prevPic.append(curImg)
    prevPic.pop(0)
#im1 = cv2.imread("TestImages/beachBahamas.jpg")

#im2 = cv2.imread("TestImages/SnowLeo2.jpg")







