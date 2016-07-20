
import cv2
import numpy



def mouseResponse(event, x, y, flags, param):
    global uppLeft, lowLeft, uppRight
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(workImg, (x, y), 5, (255, 0, 255), -1)
        if uppLeft is None:
            uppLeft = [x, y]
            print uppLeft
        elif lowLeft is None:
            lowLeft = [x, y]
            print lowLeft
        elif uppRight is None:
            uppRight = [x, y]
            print uppRight

uppRight = None
uppLeft = None
lowLeft = None

# read in an image
origImg = cv2.imread("TestImages/SnowLeo1.jpg")
height, width, depth = origImg.shape

# make a copy and set up the window to display it
workImg = origImg.copy()
cv2.namedWindow("Working image")

# assign mouse_response to be the callback function for the Working image window
cv2.setMouseCallback("Working image", mouseResponse)

# Keep re-displaying the window, and look for user to type 'q' to quit
while True:
    cv2.imshow("Working image", workImg)
    if (uppLeft is not None) and (uppRight is not None) and (lowLeft is not None):

        (rows, cols, depth) = workImg.shape

        origPts = numpy.float32([uppLeft, lowLeft, uppRight])

        newPts = numpy.float32([[0, 0], [0, height - 1], [width - 1, 0]])

        mat = cv2.getAffineTransform(origPts, newPts)

        warpImg = cv2.warpAffine(workImg, mat, (cols, rows))

        cv2.imshow("Working image", warpImg)

    x = cv2.waitKey(20)
    ch = chr(x & 0xFF)
    if ch == 'q':
        break

cv2.destroyAllWindows()
