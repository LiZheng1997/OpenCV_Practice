# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 下午9:09
# @Author  : lizheng
# @FileName: demo6.py.py
# @Software: PyCharm
import cv2

kernel1=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

kernel2=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

kernel3=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

print("kernel1=\n",kernel1)

print("kernel2=\n",kernel2)

print("kernel3=\n",kernel3)


##
import cv2

o=cv2.imread("kernel.bmp",cv2.IMREAD_UNCHANGED)

kernel1=cv2.getStructuringElement(cv2.MORPH_RECT,(59,59))

kernel2=cv2.getStructuringElement(cv2.MORPH_CROSS,(59,59))

kernel3=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(59,59))

dst1=cv2.dilate(o,kernel1)

dst2=cv2.dilate(o,kernel2)

dst3=cv2.dilate(o,kernel3)

cv2.imshow("orriginal",o)

cv2.imshow("dst1",dst1)

cv2.imshow("dst2",dst2)

cv2.imshow("dst3",dst3)

cv2.waitKey()

cv2.destroyAllWindows()