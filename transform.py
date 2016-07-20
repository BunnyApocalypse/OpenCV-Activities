import cv2
import numpy

def mouseResponse(event, x, y, flags, param):
    global uppLeft, lowLeft, uppRight
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(workImg, (x, y), 5, (255, 0, 255), -1)
        print "foo"
        if uppLeft is None:
            uppLeft = [x, y]
            print uppLeft
        elif uppRight is None:
            uppRight = [x, y]
            print uppRight
        elif lowLeft is None:
            lowLeft = [x, y]
            print lowLeft
vidCap = cv2.VideoCapture(0)
uppLeft = None
lowLeft = None
uppRight = None
transform = False
blur = False
cv2.namedWindow("Working image")
cv2.setMouseCallback("Working image", mouseResponse)
ret, origImg = vidCap.read()
height, width, depth = origImg.shape

# make a copy and set up the window to display it
workImg = origImg
finalImg = workImg

loop = True
font = cv2.FONT_HERSHEY_SIMPLEX
while loop == True:


    x = cv2.waitKey(10)

    userChar = chr(x & 0xFF)
    if userChar == 't':
        if transform == False:
            transform = True
            print "changed"
        else:
            transform = False
    elif userChar == "b":
        if blur == False:
            blur = True
            print "k"
        else:
            blur = False


    if (uppLeft is not None) and (uppRight is not None) and (lowLeft is not None) and (transform == True):
        (rows, cols, depth) = workImg.shape
        origPts = numpy.float32([uppLeft, lowLeft, uppRight])
        newPts = numpy.float32([[0, 0], [0, height - 1], [width -1, 0]])
        mat = cv2.getAffineTransform(origPts, newPts)
        finalImg = cv2.warpAffine(workImg, mat, (cols, rows))
        #cv2.imshow("Working image", workImg)


    if blur == True:
        if transform is True:
            finalImg = cv2.blur(finalImg, (11,11))
            #cv2.imshow("final image", finalImg)
        else:
            finalImg= cv2.blur(workImg, (11,11))
            #cv2.imshow("Working image", workImg)
        print "roo"


    if ((uppLeft is not None) and (uppRight is not None) and (lowLeft is not None) and (transform is True)) or (blur is True):
        cv2.imshow ("Working image", finalImg)
    else:
        cv2.imshow("Working image", workImg)


    #cv2.circle(img,(10,10),10, (0,0,255),-1)
    ret, origImg = vidCap.read()
    workImg = origImg
    cv2.putText(workImg, "B for blur, Click 3 times for transform and Q for quit", (0, 30), font, 1, (255, 255, 255))



    if userChar == 'q':

        loop = False


cv2.destroyAllWindows()

vidCap.release()