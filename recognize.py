import cv2
import sqlite3
cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#database

def InsertorUpdate(Id, Name):
	conn = sqlite3.connect('facedb.db')
	cmd = "SELECT * FROM people WHERE ID = "+str(Id)
	cursor = conn.execute(cmd)
	isRecordExist = 0
	for row in cursor:
		isrecordExist = 1
	if(isRecordExist ==1):
		cmd= "UPDATE people SET name="+str(Name)+" WHERE ID="+str(Id)
	else:
		cmd= "INSERT INTO people(ID,Name) values("+str(Id)+", "+str(Name)+")"
	conn.execute(cmd)
	conn.commit()
	conn.close()

#creating dataset id
Id = input('Enter your id : ')
Name= input('Enter your name: ')
InsertorUpdate(Id, Name)

sampleNum = 0

while(True):
	ret, img = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = detector.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
	
		cv2.rectangle(img,(x,y),(x+w,y+h), (255,0,0),2)

		#incrementing sample number
		sampleNum = sampleNum+1

		#saving the captured face in the dataset folder
		cv2.imwrite("dataset/user." +Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

	cv2.imshow('frame', img)

	#waiting for 100 milisecods
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
	#break if the sample number is morethan 20
	elif sampleNum>20:
		break
cam.release()
cv2.destroyAllWindows()