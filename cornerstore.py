__author__ = 'kingc3'
import cv2

img1 = cv2.imread("TestImages/Puzzle1.jpg")

cv2.imshow('kys', img1)

#grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#print goodFeats
# ret, normalImg = feed.read()
#displayHough = normalImg.copy()workImg = normalImg.copy()
workImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
workImg = cv2.GaussianBlur(workImg, (17,17), 0)
# = cv2.addWeighted(gaus, 1.5, workImg, -.5, 0)
#workImg = cv2.equalizeHist(workImg)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))
workImg = cv2.morphologyEx(workImg, cv2.MORPH_OPEN, kernel)
cv2.imshow("progress", workImg)
goodFeats = cv2.goodFeaturesToTrack(workImg, 200, 0.455, 5)



for x in goodFeats:
    cv2.circle(img1, (x[0,0],x[0,1]),3,(0,0,255),-1)
cv2.imshow('dsfa',img1)
cv2.waitKey(0)