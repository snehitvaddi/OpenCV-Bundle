import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv',hsv) #tocheck whats happeing in hsv statement
    lower_blue = np.array([50,50,150])
    upper_blue = np.array([255,100,180])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)#returns true/false
    res = cv2.bitwise_and(frame,frame,mask=mask)

##    cv2.imshow('frame',frame)
##    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
     
