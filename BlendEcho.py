__author__ = 'huangb3'
import cv2
import numpy
x = .1

img1 = cv2.imread("TestImages/SnowLeo1.jpg")
feed = cv2.VideoCapture(0)
ret, img2 = feed.read()
(hgt1, wid1, dep1) = img1.shape
(hgt2, wid2, dep2) = img2.shape
newWid = min(wid1, wid2)
newHgt = min(hgt1, hgt2)
im1Crop = img1[0:newHgt, 0:newWid]
im2Crop = img2[0:newHgt, 0:newWid]
cv2.imshow("Img1 Cropped", im1Crop)

cv2.waitKey(0)
while x < .9:
    ret, img2 = feed.read()
    dst = cv2.addWeighted(im1Crop, (1-x), im2Crop, x, 0)
    cv2.imshow("Img1 Cropped", dst)
    cv2.waitKey(30)
    x += .01
ret, frame = feed.read()
prevPics = [frame] * 5
while True:
    ret, frame = feed.read()
    dst = cv2.addWeighted(prevPics[0], .4, frame, .6, 0)
    cv2.imshow("Img1 Cropped", dst)
    x = cv2.waitKey(20)
    x = chr(x & 0xFF)
    if x == 'q':
        break
    prevPics.append(frame)
    prevPics.pop(0)
cv2.destroyAllWindows()