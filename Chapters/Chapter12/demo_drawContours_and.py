import cv2 as cv

import numpy as np

o = cv.imread("stuff.jpg") #对于不清楚的图像 这个轮廓很难区分，
cv.imshow("original",o)
gray = cv.cvtColor(o, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
contours,hierarchy = cv.findContours(binary, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

mask = np.zeros(o.shape,np.uint8)
mask = cv.drawContours(o,contours, -1, (0,0,255),-1)
cv.imshow("mask",mask)
loc = cv.bitwise_and(o,mask)
cv.imshow("location",loc)
cv.waitKey()
cv.destroyAllWindows()