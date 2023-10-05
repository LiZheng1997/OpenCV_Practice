# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:08:41 2019

@author: 14290
"""

import numpy as np
import cv2 as cv

#手动拆分图像通道
demo=cv.imread("../images/lenacolor.png")
#cv.imshow("demo",demo)
#b = demo[:,:,0]
#g = demo[:,:,1]
#r = demo[:,:,2]
#cv.imshow("b", b)
#cv.imshow("g", g)
#cv.imshow("r", r)
#demo[:,:,0]=0
#cv.imshow("demo01",demo)
#demo[:,:,1]=0
#cv.imshow("demo02",demo)
#cv.waitKey()
#cv.destroyAllWindows()

#通过函数拆分
b,g,r=cv.split(demo)
#cv.imshow("B" ,b)
#cv.imshow("G" ,g)
# cv.imshow("R" ,r)



#通道合并
bgr=cv.merge([b,g,r])
rgb=cv.merge([r,g,b])
cv.imshow("demo",demo)
cv.imshow("bgr",bgr)
cv.imshow("rgb",rgb)
cv.waitKey()
cv.destroyAllWindows()