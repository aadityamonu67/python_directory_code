import cv2
import numpy as np
cap = cv2.Video.Capture(1)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,0,0])
    upper_red = np.array([255,255,255])

   mask = cv2.inRange(hsv, lower_red, upper_red)
   res = cv2.bitwise_and(frame, frame, mask = mask)

cv2.imshow('frame',frame)
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
       break

    cv2.destroyAllWindows()
    cap.release()