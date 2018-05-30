import cv2, os
import numpy as np
from PIL import Image
#recognizer = cv2.LBPHFaceRecognizer_create()
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
path = 'dataset'

def getImagesAndLabels(path):
	#to load the image we create the paths to the image 
	imagepaths = [os.path.join(path,f) for f in os.listdir(path)]
	#print (imagepaths)
	#lists to store the faces and ids
	faceSamples=[]
	#create emptty ID list
	Ids=[]

	#loop images using the image path and load these images and ids
	for imagepath in imagepaths:
		#loading the image and converting it to gray scale
		pilimage = Image.open(imagepath).convert('L')
		#now we are converting the PIL image into numpy array
		imagenp = np.array(pilimage, 'uint8')
		#getting the Id from the images 
		Id = int(os.path.split(imagepath)[-1].split(".")[1])
		#extract the face from the training image sample
		#faces = detector.detectMultiScale(imagenp)

	#if a face is there then append that in the list as well id of it
		#for(x,y,w,h) in faces:
		faceSamples.append(imagenp)
		print (Id)
		Ids.append(Id)
		cv2.imshow("training",imagenp) 
		#cv2.waitkey(10)
	return Ids, faceSamples

Ids, faceSamples = getImagesAndLabels(path)
recognizer.train(faceSamples, np.array(Ids))
recognizer.save('trainer/trainer.yml')
cv2.destroyAllWindows()