import cv2

vidCap = cv2.VideoCapture(0)

loop = True
frame = 0
font = cv2.FONT_HERSHEY_SIMPLEX
while loop == True:

    frame += 1

    ret, img = vidCap.read()

    cv2.circle(img,(10,10),10, (0,0,255),-1)

    cv2.putText(img, str (frame), (0, 30), font, 1, (255, 255, 255))

    img2 = img[:,::-1,:]

    cv2.imshow("Webcam", img)

    x = cv2.waitKey(10)

    userChar = chr(x & 0xFF)

    if userChar == 'q':

        loop = False

    elif userChar == 'p':

        cv2.imwrite("Snapshot.jpg", img2)

cv2.destroyAllWindows()

vidCap.release()