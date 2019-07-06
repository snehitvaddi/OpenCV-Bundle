import cv2
import numpy
import matplotlib.pyplot as plt 

cap=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    if(cv2.waitKey(1) == ord('q')):
    #waitKey(1) for contineous capturing
    #waitKey(0) for capturing frame by frame    
       break
cap.release()
cv2.destroyAllWindows()
