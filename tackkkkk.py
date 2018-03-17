import cv2
import numpy as np
import win32api, win32con
# create video capture
cap = cv2.VideoCapture(0)
cap.set(3,3000)
cap.set(4,2000)
cap.set(5,25)
#cap.set(15, 0.1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    
while(1):

    # read the frames
    _,frame = cap.read()

    # smooth it
    frame = cv2.blur(frame,(3,3))
    best_cnt = 1
    
    # convert to hsv and find range of colors
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv,np.array((0, 193, 24)), np.array((179, 255, 255)))
    thresh2 = thresh.copy()

    # find contours in the threshold image
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    # finding contour with maximum area and store it as best_cnt
    max_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            best_cnt = cnt
            
    # finding centroids of best_cnt and draw a circle there
    M = cv2.moments(best_cnt)
   
    cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    
    
    cv2.circle(frame,(cx,cy+200),5,255,-1)
    print cx
    print ""
    print cy
    click(cx,cy)

    # Show it, if key pressed is 'Esc', exit the loop
              
    #cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
    cv2.imshow('frame',frame)
    #cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)          
    #cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
    cv2.imshow('thresh',thresh2)
    if cv2.waitKey(33)== 27:
        break

# Clean up everything before leaving
cv2.destroyAllWindows()
cap.release()
