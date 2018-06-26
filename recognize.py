import cv2
import sqlite3
cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
database = input('Create a student or lecture database(student.db or lecturer.db) : ')

if database == 'lecturer.db':

	#database
	def InsertorUpdate(Id, name, contact, courseUnit):
		conn = sqlite3.connect(database)
		cusor = conn.cursor()
		cusor.execute("CREATE TABLE IF NOT EXISTS lecturer(ID INTEGER , Name TEXT , Contact INTEGER, CourseUnit TEXT)")
		cmd = "SELECT * FROM lecturer WHERE ID = "+str(Id)
		cursor = conn.execute(cmd)
		isRecordExist = 0
		for row in cursor:
			isrecordExist = 1
		if(isRecordExist ==1):
			cmd= "UPDATE lecturer SET Name="+str(name)+", Contact="+str(contact)+", CourseUnit="+str(courseUnit)+" WHERE ID="+str(Id)
		else:
			cmd= "INSERT INTO lecturer(ID,Name,Contact,CourseUnit) values("+str(Id)+", "+str(name)+", "+str(contact)+", "+str(courseUnit)+")"
		conn.execute(cmd)
		conn.commit()
		conn.close()


	#creating dataset id
	Id = input('Enter your id : ')
	name= input('Enter your name: ')
	contact = input('Enter contact name: ')
	courseUnit = input('Enter yo: ')

	InsertorUpdate(Id, name, contact, courseUnit)

else:
	#database

	def InsertorUpdate(Id, name, regno, course):
		conn = sqlite3.connect(database)
		cusor = conn.cursor()
		cusor.execute("CREATE TABLE IF NOT EXISTS students(ID INTEGER , Name TEXT , RegNo TEXT, Course TEXT)")
		cmd = "SELECT * FROM students WHERE ID = "+str(Id)
		cursor = conn.execute(cmd)
		isRecordExist = 0
		for row in cursor:
			isrecordExist = 1
		if(isRecordExist ==1):
			cmd= "UPDATE students SET Name="+str(name)+", RegNo="+str(regno)+", course="+str(Course)+" WHERE ID="+str(Id)
		else:
			cmd= "INSERT INTO students(ID,Name,RegNo,Course) values("+str(Id)+", "+str(name)+", "+str(regno)+", "+str(course)+")"
		conn.execute(cmd)
		conn.commit()
		conn.close()

	#creating dataset id
	Id = input('Enter your id : ')
	name= input('Enter your : ')
	regno = input('Enter your regno : ')
	course = input('Enter your course: ')

	InsertorUpdate(Id, name, regno, course)

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
		if database == 'lecturer.db':
			cv2.imwrite("dataset/lecturer." +Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
		else:
			cv2.imwrite("dataset/std." +Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

	cv2.imshow('frame', img)

	#waiting for 100 milisecods
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
	#break if the sample number is morethan 20
	elif sampleNum>20:
		break
cam.release()
cv2.destroyAllWindows()