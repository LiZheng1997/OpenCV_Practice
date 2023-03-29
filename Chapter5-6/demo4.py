# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 上午2:20
# @Author  : lizheng
# @FileName: demo4.py.py
# @Software: PyCharm

import cv2

import numpy as np

img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)

rows,cols=img.shape

mapx=np.ones(img.shape,np.float32)*3

mapy=np.ones(img.shape,np.float32)*0

rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)

print("img=\n",img)

print("mapx=\n",mapx)

print("mapy=\n",mapy)

print("rst=\n",rst)