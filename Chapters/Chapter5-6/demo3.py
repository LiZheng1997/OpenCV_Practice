# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 上午2:07
# @Author  : lizheng
# @FileName: demo3.py.py
# @Software: PyCharm

import cv2

import numpy as np

img=cv2.imread('../images/lena.bmp')

rows,cols=img.shape[:2]

print(rows,cols)

pts1=np.float32([[150,50],[400,50],[60,450],[310,450]])

pts2=np.float32([[50,50],[rows-50,50],[50,cols-50],[rows-50,cols-50]])

M=cv2.getPerspectiveTransform(pts1,pts2)

dst=cv2.warpPerspective(img,M,(cols,rows))

cv2.imshow("img",img)

cv2.imshow("dst",dst)

cv2.waitKey()

cv2.destroyAllWindows()