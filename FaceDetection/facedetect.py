import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
 
image = cv2.imread('a.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
faces = face_cascade.detectMultiScale(grayImage)
 
#print type(faces)
 
if len(faces) == 0:
    print ('No faces found')
else:
    print ('Number of faces detected:'+ str(faces.shape[0]))
 
    
