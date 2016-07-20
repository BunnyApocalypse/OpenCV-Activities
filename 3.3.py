__author__ = 'huangb3'
import cv2

origIm = cv2.imread('TestImages/Coins2.jpg')
imGray = cv2.cvtColor(origIm, cv2.COLOR_BGR2GRAY)
cv2.imshow("normal", imGray)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
imGray = cv2.morphologyEx(imGray, cv2.MORPH_OPEN, kernel)
imGray = cv2.GaussianBlur(imGray, (5, 5), 0)
imGray = cv2.equalizeHist(imGray)
imGray = cv2.morphologyEx(imGray, cv2.MORPH_OPEN, (kernel*2))
cv2.imshow("threshol", imGray)
circles = cv2.HoughCircles(imGray, cv2.HOUGH_GRADIENT, 1 ,20,

                              param1 = 40, param2 = 45,

                              minRadius = 30, maxRadius = 70)
for x in circles[0]:
    cv2.circle(origIm, (x[0], x[1]), x[2], (0, 0, 255), 2)
cv2.imshow("Cricles", origIm)
cv2.waitKey(0)