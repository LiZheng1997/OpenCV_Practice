
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

o=cv2.imread("erode.bmp",cv2.IMREAD_UNCHANGED)

kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(o,kernel)

cv2.imshow("orriginal",o)

cv2.imshow("erosion",erosion)

cv2.waitKey()

cv2.destroyAllWindows()

#膨胀的操作和腐蚀刚好相反。
img=np.zeros((5,5),np.uint8)
img[2:3,1:4]=1
kernel=np.ones((3,1),np.uint8)
dilation=cv2.dilate(img,kernel)
print("img=\n",img)
print("kernel=\n",kernel)
print("dilation\n",dilation)


##
import cv2

import numpy as np

o=cv2.imread("dilation.bmp",cv2.IMREAD_UNCHANGED)

kernel=np.ones((9,9),np.uint8)

dilation=cv2.dilate(o,kernel)

cv2.imshow("original",o)

cv2.imshow("dilation",dilation)

cv2.waitKey()

cv2.destroyAllWindows()
