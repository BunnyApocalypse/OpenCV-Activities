__author__ = 'huangb3'
import cv2

origIm = cv2.imread('TestImages/Coins1.jpg')
imGray = cv2.cvtColor(origIm, cv2.COLOR_BGR2GRAY)
cv2.imshow("normal", imGray)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
imGray = cv2.morphologyEx(imGray, cv2.MORPH_OPEN, kernel)
imGray = cv2.GaussianBlur(imGray, (5, 5), 0)
res, imGray = cv2.threshold(imGray, 190, 255, cv2.THRESH_TRUNC)
res, imGray = cv2.threshold(imGray, 0, 150, cv2.THRESH_TOZERO)
imGray = cv2.morphologyEx(imGray, cv2.MORPH_OPEN, (kernel*2))
cv2.imshow("threshol", imGray)
ret, thresh = cv2.threshold(imGray, 100, 190, 0)
im2, contrs, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(origIm, contrs, -1, (0, 255, 0), 3)


cv2.imshow("final", origIm)
cv2.waitKey(0)