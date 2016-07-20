__author__ = 'kingc3'
import cv2

cv2.ocl.setUseOpenCL(False)
img1 = cv2.imread("TestImages/Coins2.jpg")
img2 = cv2.imread("TestImages/Coins1.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)



#cv2.waitKey(0)
#cv2.imshow("Original 1", img)

                                                

# create a ORB object, that can run the ORB algorithm.

orb = cv2.ORB_create()
                                                

keypts, des = orb.detectAndCompute(img1, None)

#print "Number of keypoints found:", len(keypts)
keypts2, des2 = orb.detectAndCompute(img2, None)
                                                

img1 = cv2.drawKeypoints(img1, keypts, None, (255, 0, 0), 4)

cv2.imshow("Keypoints 1", img1)

img2 = cv2.drawKeypoints(img2, keypts2, None, (255, 0, 0), 4)

cv2.imshow("Keypoints 2", img2)

cv2.waitKey(0)

cv2.destroyAllWindows()