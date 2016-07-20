__author__ = 'kingc3'
import cv2
import numpy as np

feed = cv2.VideoCapture(0)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
test = feed.read()
while True:
    ret, normalImg = feed.read()
    displayHough = normalImg.copy()
    workImg = normalImg.copy()
    workImg = cv2.cvtColor(workImg, cv2.COLOR_BGR2GRAY)
    workImg = cv2.GaussianBlur(workImg, (5,5), 0)
    workImg = cv2.equalizeHist(workImg)




    cannyImg = cv2.Canny(workImg, 100, 200)

    lines = cv2.HoughLinesP(cannyImg, 1, np.pi/180,

                            threshold = 5,

                            minLineLength = 20, maxLineGap = 10)

    for lineSet in lines:

        for line in lineSet:

            cv2.line(displayHough, (line[0], line[1]), (line[2], line[3]),

                     (255, 255, 0))

    cv2.imshow("HoughLines", displayHough)



    sobelValsHorz = cv2.Sobel(workImg, cv2.CV_32F, 1, 0)

    horzImg = cv2.convertScaleAbs(sobelValsHorz)

    #cv2.imshow("horizontal gradient", horzImg)

    # Compute gradient in vertical direction (Detects horizontal edges)

    sobelValsVerts = cv2.Sobel(workImg, cv2.CV_32F, 0, 1)

    vertImg = cv2.convertScaleAbs(sobelValsVerts)

    #cv2.imshow("vertical gradient", vertImg)

    # Combine the two gradients

    sobelComb = cv2.addWeighted(sobelValsHorz, 0.5,

                                sobelValsVerts, 0.5, 0)

    # Convert back to uint8

    sobelImg = cv2.convertScaleAbs(sobelComb)

    cv2.imshow("Sobel", sobelImg)





    x = cv2.waitKey(10)
    ch = chr(x & 0xFF)
    if ch == 'q':
        break

