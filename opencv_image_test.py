import cv2
import numpy
import matplotlib.pyplot as plt 
img=cv2.imread('C:\\Users\\vsneh\\Downloads\\fresher1.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (960, 540)) 
cv2.imshow('fresher1.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


