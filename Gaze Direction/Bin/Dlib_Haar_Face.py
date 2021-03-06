#Fabian implementation

import cv2
import numpy as np
from matplotlib import pyplot as plt
import dlib 

# Video capture via webcam
cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

faceCascade1 = cv2.CascadeClassifier('../../haarcascades/haarcascade_frontalface_alt2.xml')
predictor = dlib.shape_predictor('../../dlibcascades/shape_predictor_68_face_landmarks.dat')
detector = dlib.get_frontal_face_detector()

while True:
    # Capture frame-by-frame
	ret, frame = video_capture.read()
	if ret:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces1 = faceCascade1.detectMultiScale(gray, 1.1, 5)
		B = dlib.dlib.rectangles()
		A = dlib.dlib.rectangle()
		dets = detector(frame, 1)
		for (x, y, w, h) in faces1:
			A.left = x
			A.top = y
			A.right = x+w
			A.bottom = y+h
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			B.append(A)
		for k, d in enumerate(B):
	        # Get the landmarks/parts for the face in box d.
			print(type(d.left))
			shape = predictor(frame, d)
			cv2.circle(frame,(shape.part(36).x,shape.part(36).y),2,(0,0,255))
			cv2.circle(frame,(shape.part(39).x,shape.part(39).y),2,(0,0,255))
			cv2.circle(frame,(shape.part(42).x,shape.part(42).y),2,(0,0,255))
			cv2.circle(frame,(shape.part(45).x,shape.part(45).y),2,(0,0,255))
			x1 = shape.part(36).x-10
			y1 = shape.part(37).y-10
			x2 = shape.part(39).x+10
			y2 = shape.part(40).y+10
			split = frame[y1:y2,x1:x2]
			cv2.rectangle(frame,(x1,y1), (x2,y2), (0, 0, 255), 2)
			x1 = shape.part(42).x-10
			y1 = shape.part(43).y-10
			x2 = shape.part(45).x+10
			y2 = shape.part(46).y+10
			split = frame[y1:y2,x1:x2]
			cv2.rectangle(frame,(x1,y1), (x2,y2), (0, 0, 255), 2)
		
		# Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
