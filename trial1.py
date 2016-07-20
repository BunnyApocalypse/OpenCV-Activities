import cv2

vidCap = cv2.VideoCapture(0)
running = bool(True)
vidData = "Wee"
circlex = 30
circley = 30
curFrame = 1
frame = "1"

while running:
    ret, img = vidCap.read()
    img2 = img[:,::-1,:].copy()

    if ret:
        cv2.circle(img2, (circlex, circley), 30, (0, 0, 300), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(img2, "TeamName", (1000, 700), font, 1, (150, 150, 150))

    frame = str(curFrame)
    cv2.putText(img2, frame, (50, 700), font, 1, (150, 150, 150), 2)

    if curFrame < 1000000000000:  #resets frame counter
        curFrame += curFrame + 1
    else:
        curFrame = 0

    x = cv2.waitKey(16)
    ioChr = chr(x & 0xFF)
    if ioChr == "q":
        running = False
    elif ioChr == " ":
        cv2.imwrite("snapshot.jpg", img2)
    elif ioChr == "w":
        if circley >= 10:
            circley -= 10
    elif ioChr == "s":
        if circley <= 720:
            circley += 10
    elif ioChr == "a":
        if circlex >= 10:
            circlex -= 10
    elif ioChr == "d":
        if circlex <= 1250:
            circlex += 10
    cv2.imshow("Webcam", img2)


cv2.destroyAllWindows()

vidCap.release()