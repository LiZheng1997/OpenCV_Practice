# -*- coding: utf-8 -*-
#找出圆形物体在图形中,测试是否能够找到图中的圆形盖

import cv2 as cv

import numpy as np

import matplotlib.pyplot as plt

img = cv.imread("../images/circle.jpg",0)

imgo = cv.imread("../images/circle.jpg",-1)
o = cv.cvtColor(imgo, cv.COLOR_BGR2RGB)
oshow = o.copy()
img = cv.medianBlur(img,5)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,300,
param1 = 50, param2 = 30, minRadius=100, maxRadius=200)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
	cv.circle(o, (i[0],i[1]), i[2], (255,0,0),12)
	cv.circle(o, (i[0],i[1]), 2, (255,0,0),12)
plt.subplot(121)
plt.imshow(oshow)
plt.axis('off')
plt.subplot(122)
plt.imshow(o)
plt.axis('off')
plt.show()