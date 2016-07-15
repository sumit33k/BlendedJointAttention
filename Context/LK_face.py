import cv2
import numpy as np
from matplotlib import pyplot as plt

# Video capture via webcam
cam = cv2.VideoCapture('../Test/test.mp4')
cam.set(3,640)
cam.set(4,480)
video_capture = cam

# Create some random colors
color = np.random.randint(0,255,(100,3))

# Take first frame and find corners in it
ret, old_frame = cap.read()
print ret
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, 900,0.01,10)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:
		grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		corners = cv2.goodFeaturesToTrack(grey,900,0.01,10)
		corners = np.int0(corners)

		# calculate optical flow
		p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

		# Select good points
		good_new = p1[st==1]
		good_old = p0[st==1]

		# print corners
		# draw the tracks
		for i,(new,old) in enumerate(zip(good_new,good_old)):
		  # print i
		  a,b = new.ravel()
		  c,d = old.ravel()
		  cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
		  cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
		img = cv2.add(frame,mask)

		# Display the resulting frame
		cv2.imshow('Video', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()