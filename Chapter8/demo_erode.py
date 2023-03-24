
#腐蚀操作中，需要定义卷积和大小和迭代的次数，如果迭代多，核越大 腐蚀越严重
import cv2
import numpy as np
# img=np.zeros((5,5),np.uint8)
# img[1:4,1:4]=1
# kernel=np.ones((3,1),np.uint8)
# erosion=cv2.erode(img,kernel)
# print("img=\n",img)
# print("kernel=\n",kernel)
# print("erosion=\n",erosion)

#膨胀的操作和腐蚀刚好相反。
img=np.zeros((5,5),np.uint8)
img[2:3,1:4]=1
kernel=np.ones((3,1),np.uint8)
dilation=cv2.dilate(img,kernel)
print("img=\n",img)
print("kernel=\n",kernel)
print("dilation\n",dilation)