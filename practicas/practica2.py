import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

template = cv2.imread('messi5.jpg',0)
w, h = template.shape[::-1]
x,y = 0,0

while(True):
    ret, frame = cap.read()
    i= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    res = cv2.matchTemplate(i,template,3)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    x = (top_left[0] + bottom_right[0])/2
    y = (top_left[1] + bottom_right[1])/2

    #Draw Rectangle Match
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 3)
    cv2.putText(frame, "["+ str(x)+","+str(y)+"]", (bottom_right[0]+10,bottom_right[1]+10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.imshow('output',frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break

cv2.destroyAllWindows()
