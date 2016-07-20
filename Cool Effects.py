
import cv2
import numpy
transform = False
blur = False

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
feed = cv2.VideoCapture(0)
ret, origImg = feed.read()
height, width, depth = origImg.shape

# make a copy and set up the window to display it
workImg = origImg.copy()
cv2.namedWindow("Working image")

# assign mouse_response to be the callback function for the Working image window
cv2.setMouseCallback("Working image", mouseResponse)

# Keep re-displaying the window, and look for user to type 'q' to quit
while True:
    x = cv2.waitKey(20)
    ch = chr(x & 0xFF)
    if ch == 'q':
        break
    elif ch == 't':
        if transform is False:
            transform = True
        else:
            transform = False
    elif ch == 'b':
        if blur is False:
            blur = True
        else:
            blur = False
    if (uppLeft is not None) and (uppRight is not None) and (lowLeft is not None) and (transform is True):

        (rows, cols, depth) = workImg.shape

        origPts = numpy.float32([uppLeft, lowLeft, uppRight])

        newPts = numpy.float32([[0, 0], [0, height - 1], [width - 1, 0]])

        mat = cv2.getAffineTransform(origPts, newPts)

        finalImg = cv2.warpAffine(workImg, mat, (cols, rows))
    if blur is True:
        if transform is True:
            finalImg = cv2.GaussianBlur(finalImg, (11, 11), 0)
        else:
            finalImg = cv2.GaussianBlur(workImg, (11, 11), 0)
    if (blur is True) or ((transform is True) and (uppLeft is not None) and (uppRight is not None) and (lowLeft is not None)):
        cv2.imshow("Working image", finalImg)
    else:
        cv2.imshow("Working image", workImg)

    ret, origImg = feed.read()
    workImg = origImg.copy()

cv2.destroyAllWindows()