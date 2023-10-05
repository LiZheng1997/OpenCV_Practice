# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 上午3:52
# @Author  : lizheng
# @FileName: demo1.py.py
# @Software: PyCharm

##图像平滑处理-均值滤波、方框滤波、高斯滤波、中值滤波、双边滤波
import cv2

o=cv2.imread("../images/lenacolor.png")#读取待处理图像

r=cv2.blur(o,(5,5))#使用blur函数处理

cv2.imshow("original",o)

cv2.imshow("result",r)

cv2.waitKey()

cv2.destroyAllWindows()


#
o=cv2.imread("image\\noise.bmp")

r5=cv2.blur(o,(5,5))

r30=cv2.blur(o,(30,30))

cv2.imshow("original",o)

cv2.imshow("result5",r5)

cv2.imshow("result30",r30)

cv2.waitKey()

cv2.destroyAllWindows()


##
o=cv2.imread("../images/lenacolor.png")

r=cv2.boxFilter(o,-1,(5,5))

cv2.imshow("original",o)

cv2.imshow("result",r)

cv2.waitKey()

cv2.destroyAllWindows()

##
o=cv2.imread("../images/lenacolor.png")

r=cv2.boxFilter(o,-1,(5,5),normalize=0)

cv2.imshow("original",o)

cv2.imshow("result",r)

cv2.waitKey()

cv2.destroyAllWindows()


##

o=cv2.imread("../images/lenacolor.png")

r=cv2.boxFilter(o,-1,(2,2),normalize=0)

cv2.imshow("original",o)

cv2.imshow("result",r)

cv2.waitKey()


##

r=cv2.GaussianBlur(o,(5,5),0,0)

cv2.imshow("original",o)

cv2.imshow("result",r)

cv2.waitKey()

cv2.destroyAllWindows()

##
r=cv2.medianBlur(o,3)

cv2.imshow("original",o)

cv2.imshow("result",r)

cv2.waitKey()

##

import cv2

o=cv2.imread("../images/lenacolor.png")

r=cv2.bilateralFilter(o,25,100,100)

cv2.imshow("original",o)

cv2.imshow("result",r)

cv2.waitKey()

cv2.destroyAllWindows()


##

g=r=cv2.GaussianBlur(o,(55,55),0,0)

b=cv2.bilateralFilter(o,55,100,100)

cv2.imshow("original",o)

cv2.imshow("Gaussian",g)

cv2.imshow("bilateral",b)

cv2.waitKey()

cv2.destroyAllWindows()


##

import cv2

import numpy as np

o=cv2.imread("../images/lenacolor.png")

kernel=np.ones((9,9),np.float32)/81

r=cv2.filter2D(o,-1,kernel)

cv2.imshow("original",o)

cv2.imshow("Gaussian",r)

cv2.waitKey()

cv2.destroyAllWindows()