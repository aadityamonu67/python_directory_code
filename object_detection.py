import numpy as np
import cv2

img = cv2.imread('test.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
_,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#Displays the border
#cv2.drawContours(img, contours, -1, (0,255,0), 3)


cv2.drawContours(img, contours, 3, (0,255,0), 3)

#cnt = contours[4]
#cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

cv2.imshow('Contour Pic', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
