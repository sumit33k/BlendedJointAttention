# Head pose estimation via dlib

import cv2
import numpy as np
import dlib 

# Video capture via webcam
cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../dlibcascades/shape_predictor_68_face_landmarks.dat')

while True:
    # Capture frame-by-frame
	ret, frame = video_capture.read()
	if ret:
		dets = detector(frame, 1)
		for k, d in enumerate(dets):
		    # Get the landmarks/parts for the face in box d.
			shape = predictor(frame, d)
			mid_x = [(shape.part(1).x+shape.part(15).x)/2, (shape.part(1).y+shape.part(15).y)/2]
			mid_y = [(shape.part(2).x+shape.part(14).x)/2, (shape.part(2).y+shape.part(14).y)/2]
			nose = [(shape.part(30).x+shape.part(29).x)/2,(shape.part(30).y+shape.part(29).y)/2]
			final_x = 3*nose[0]-2*mid_x[0]
			final_y = 3*nose[1]-2*mid_y[1]
			# print nose,final_x
			cv2.circle(frame,(final_x,final_y),2,(0,0,255))
			cv2.circle(frame,(nose[0],nose[1]),2,(0,0,255))
			cv2.line(frame,(nose[0],nose[1]), (final_x,final_y),(255,0,0),3)
	# Display the resulting frame
	out.write(frame)
	cv2.imshow('Video', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break
# Release video capture
out.release()
video_capture.release()
cv2.destroyAllWindows()