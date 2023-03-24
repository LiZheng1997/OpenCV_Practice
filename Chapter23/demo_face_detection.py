# -*- coding: utf-8 -*-
#!/usr/bin/python

#这个demo用来检测人脸的， 用的是官方的casscade，测试用

import  cv2 as cv
import time



cap = cv.VideoCapture(1)
time.sleep(1)

ok, image = cap.read()
# image = cv.imread("lena.bmp")

faceCascade = cv.CascadeClassifier('/home/lizheng/opencv/data/haarcascades/haarcascade_frontalface_alt.xml')

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray,scaleFactor = 1.15,minNeighbors = 5,minSize = (5,5))

print(faces)

print("detect {0} faces!" .format(len(faces)))

for(x,y,w,h) in faces:
	cv.circle(image, (int((x+x+w)/2), int((y+y+h)/2)), int(w/2), (0,255,0), 2)

cv.imshow("dect", image)

cv.imwrite("re.jpg", image)

cv.waitKey()

cap.release()
cv.destroyAllWindows()