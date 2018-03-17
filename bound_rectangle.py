import numpy as np
import cv2
cam=cv2.VideoCapture(0)
kernel=np.ones((5,5),np.uint8)
while(True):
    ret, frame=cam.read()
    rangomax=np.array([100,188,0])
    rangomin=np.array([179,255,255])
    mascara=cv2.inRange(frame,rangomin,rangomax)
    opening=cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
    x,y,w,h = cv2.boundingRect(opening)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.circle((x+w/2,y+h/2),5,(0,0,255), 1)
    cv2.imshow("Show",frame)
    cv2.waitKey()
    cv2.destroyAllWindows()
