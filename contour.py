import cv2    
im=cv2.imread('Untitled.png') # read picture

imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) # BGR to grayscale

ret,thresh=cv2.threshold(imgray,200,255,cv2.THRESH_BINARY_INV)

countours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(im,countours,-1,(255,0,0),3)
cv2.imshow("Contour",im)

cv2.waitKey(0)
cv2.destroyAllWindows()
