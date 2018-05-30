import cv2
import numpy as np
cam = cv2.Videocapture(0);


faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
	ret, img = cam.read()
	if ret:
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = faceDetect.detectMultiScale(gray, 1.3, 5)
	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255,0), 2)

	cv2.imshow("Face", img)
	if (cv2.waitkey(30)==ord('q')):
		break
cam.release()
cv2.destroyAllWindows()