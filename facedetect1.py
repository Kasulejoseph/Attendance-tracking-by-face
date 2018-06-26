import cv2
import numpy as np 
import sqlite3

faceDetect = cv2.CascadeClassifier ('haarcascade_frontalface_default.xml')
#eye_detect = cv2.CascadeClassifier ('haarcascade_eye.xml')

def getProfile(id):
	conn= sqlite3.connect("facedb.db")
	cmd = "SELECT * FROM people WHERE ID ="+str(id)
	cursor = conn.execute(cmd)

	profile =None
	for row in cursor:
		profile = row
	conn.close()
	return profile




cam = cv2.VideoCapture(0);
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read('trainer/trainer.yml')
id = 0
font=cv2.FONT_HERSHEY_SIMPLEX
while(True):
	ret, img = cam.read()									
	if ret:
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# Get all face from the video frame
	faces = faceDetect.detectMultiScale(gray, 1.3, 5)
	# For each face in faces
	for(x,y,w,h) in faces:
		# Recognize the face belongs to which ID
		id, conf=rec.predict(gray[y:y+y,x:x+w])

		# Create rectangle around the face
		cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),2)
		
		profile = getProfile(id)
		if (profile!=None):
			if (id == 2):
				cv2.putText(img,"Name:"+str(profile[1]),(x,y+h+30),font, 2, (0,0,255),2)
				cv2.putText(img, "regNo:"+str(profile[2]),(x,y+h+90),font, 2, (0,0,255), 2)
				cv2.putText(img,"code:"+(profile[3]),(x,y+h+150),font, 2, (0,0,255), 2)
				cv2.putText(img,"school: "+(profile[4]),(x,y+h+210),font, 2, (0,0,255), 2)
			elif (id == 6):
				cv2.putText(img,"Name:"+str(profile[1]),(x,y+h+30),font, 2, (0,0,255),2)
				cv2.putText(img, "regNo:"+str(profile[2]),(x,y+h+90),font, 2, (0,0,255), 2)
				#cv2.putText(img,"code:"+(profile[3]),(x,y+h+150),font, 2, (0,0,255), 2)
				#cv2.putText(img,"school: "+(profile[4]),(x,y+h+210),font, 2, (0,0,255), 2)
			else:
				print("unknown")
				cv2.putText(img,"unknown",(x,y+h+30),font, 2, (0,0,255),2)

		
		'''roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		eyes = eye_detect.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color, (ex, ey), (ex+ew,ey+eh), (255,0,0), 2)'''

	cv2.imshow("Face",img)
	if(cv2.waitKey(30)==ord('q')):
		break
cam.release()
cv2.destroyAllWidows()