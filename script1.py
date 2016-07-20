__author__ = 'kingc3'
import cv2

imageNames = ['Blowhole013.jpg',
              'Blowhole021.jpg',
              'Coins1.jpg',
              'Coins2.jpg',
              'DollarCoin.jpg',
              'frame0017.jpg',
              'frame0019.jpg',
              'frankenstein.jpg',
              'garden.jpg'
              ]
for i in imageNames:
    x = cv2.imread("TestImages/"+i)
    cv2.line(x, (0,0),(100,100),(255,0,0),3)
    cv2.imshow(i,x)
    cv2.waitKey(0)
    cv2.destroyAllWindows()