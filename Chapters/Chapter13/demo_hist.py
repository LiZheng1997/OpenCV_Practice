

import cv2
# import numpy as np
# img=cv2.imread("Picture1.jpg")
# hist=cv2.calcHist([img],[0],None,[256],[0,255])
# print(type(hist))
# print(hist.shape)
# print(hist.size)
# print(hist)

import matplotlib.pyplot as plt
# x=[0,1,2,3,4,5,6]
# y=[0.3,0.4,2,5,3,4.5,4]
# plt.plot(x,y)

# a=[0.3,0.4,2,5,3,4.5,4]
# b=[3,5,1,2,1,5,3]
# plt.plot(a,color='r')
# plt.plot(b,color='g')

o=cv2.imread("Picture1.jpg")
# histb=cv2.calcHist([o],[0],None,[256],[0,255])
# plt.plot(histb,color='b')

histb=cv2.calcHist([o],[0],None,[256],[0,255])
histg=cv2.calcHist([o],[1],None,[256],[0,255])
histr=cv2.calcHist([o],[2],None,[256],[0,255])
plt.plot(histb,color='b')
plt.plot(histg,color='g')
plt.plot(histr,color='r')

plt.show()