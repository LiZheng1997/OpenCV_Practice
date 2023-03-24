
#计算出两个采样方式之后的差异，说明两个方向的采样不是可逆的。
import cv2
o=cv2.imread("lena.bmp")
down=cv2.pyrDown(o)
up=cv2.pyrUp(down)
diff=up-o #构造diff图像，查看up与o的区别
print("o.shape=",o.shape)
print("up.shape=",up.shape)
cv2.imshow("original",o)
cv2.imshow("up",up)
cv2.imshow("difference",diff)
print(o.shape)
cv2.waitKey()
cv2.destroyAllWindows()