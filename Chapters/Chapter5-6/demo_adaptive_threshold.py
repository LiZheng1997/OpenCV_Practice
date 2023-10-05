import cv2

#自适应阈值处理模式 自适应阈值可以保留更多的细节。
# img=cv2.imread("home.jpg",0)
# t1,thd=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# athdMEAN=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,3)
# athdGAUS=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,3)
# cv2.imshow("img",img)
# cv2.imshow("thd",thd)
# cv2.imshow("athdMEAN",athdMEAN)
# cv2.imshow("athdGAUS",athdGAUS)
# cv2.waitKey()


img=cv2.imread("licenseplate_motion.jpg",0)
t1,thd=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
t2,otsu=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("img",img)
cv2.imshow("thd",thd)
cv2.imshow("otus",otsu)
cv2.waitKey()
cv2.destroyAllWindows()