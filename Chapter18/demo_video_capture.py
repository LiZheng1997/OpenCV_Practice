
import numpy as np

import cv2 as cv

#读取文件或者读取摄像头
# cap = cv.VideoCapture('vtest.avi')

# while(cap.isOpened()):
# 	ret, frame = cap.read()
# 	cv.imshow('frame',frame)
# 	c = cv.waitKey(40) #单位是ms，一般是25，表示每一帧停留的时间。
# 	if c == 27:
# 		break
# cap.release()

# cv.destroyAllWindows()

# 视频读取和保存
#读取视频的每一帧然后进行图像处理，达到处理整个视屏的目的。
cap = cv.VideoCapture("vtest.avi")

while(cap.isOpened()):
	ret, frame = cap.read()
	frame=cv.Canny(frame,100,200)
	cv.imshow('frame',frame)
	c = cv.waitKey(1)
	if c == 27:
		break
cap.release()

cv.destroyAllWindows()