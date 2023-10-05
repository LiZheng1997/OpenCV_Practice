import cv2
import numpy as np

#二值化阈值，
# img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
# t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# print("img=\n",img)
# print("t=",t)
# print("rst=\n",rst)

# img=cv2.imread("lena.bmp")
# t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# cv2.imshow("img",img)
# cv2.imshow("rst",rst)
# cv2.waitKey()
# cv2.destroyAllWindows()

#反二值化阈值处理 大于阈值的为255， 小于为0
# img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
# t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# print("img=\n",img)
# print("t=",t)
# print("rst=\n",rst)

#反二值化阈值处理 大于阈值的为0， 小于为255
# img=cv2.imread("lena.bmp")
# t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# cv2.imshow("img",img)
# cv2.imshow("rst",rst)
# cv2.destroyAllWindows()
# cv2.waitKey()

# 截断化阈值处理 小于等于阈值的不变大于阈值的设定为阈值
# img=cv2.imread("lena.bmp")
# t,rst=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# cv2.imshow("img",img)
# cv2.imshow("rst",rst)
# cv2.waitKey()

#超阈值0处理 超过阈值的进行0赋值
# img=cv2.imread("lena.bmp")
# t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# cv2.imshow("img",img)
# cv2.imshow("rst",rst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 低阈值处理 低于阈值的0处理方式
# img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
# t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# print("img=\n",img)
# print("t=",t)
# print("rst=\n",rst)
# cv2.imshow("img",img)
# cv2.imshow("rst",rst)
# cv2.waitKey()
# cv2.destroyAllWindows()


img=cv2.imread("../images/lena.bmp")
t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
cv2.imshow("img",img)
cv2.imshow("rst",rst)
cv2.waitKey()
cv2.destroyAllWindows()