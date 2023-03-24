# 图像轮廓是图像中非常重要的一个特征信息，通过对图像轮廓的操作，
# 我们能够获取目标图像的大小、位置、方向等信息

#画出所有图像中识别到的轮廓

import cv2 as cv

o= cv.imread("pic1.png")
cv.imshow("original",o)
gray = cv.cvtColor(o,cv.COLOR_RGB2GRAY)
ret, binary = cv.threshold(gray,127,255,cv.THRESH_BINARY)
contours,hierarchy = cv.findContours(binary, cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
o = cv.drawContours(o,contours, -1, (0,0,255),5)
cv.imshow("result",o)
cv.waitKey()
cv.destroyAllWindows()