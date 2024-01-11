
import cv2, imutils
import matplotlib.pyplot as plt
import numpy as np  


	
tracker1 = cv2.TrackerCSRT_create()
tracker2 = cv2.TrackerCSRT_create()
tracker3 = cv2.TrackerCSRT_create()
track = [cv2.TrackerCSRT_create(),cv2.TrackerCSRT_create()]
camera=False 
if camera: 
	video  = cv2.VideoCapture(0)
else:
	video = cv2.VideoCapture('Sperm_Motility.mp4')
_,frame = video.read()
frame = imutils.resize(frame,width=720)
ROIs = cv2.selectROIs("Select Rois",frame)
print(ROIs)
BB = ROIs[0]
# CC = ROIs[1]
# DD = ROIs[2]

tracker1.init(frame, BB)
# tracker2.init(frame, CC)
# tracker3.init(frame, DD)

pointXB = []
pointYB = []

"""pointXC = []
pointY = []

pointXD = []
pointYD = []"""

while True:
	
	_,frame = video.read()
	frame = imutils.resize(frame,width=720)
	track_success1,BB = tracker1.update(frame)
	# track_success2,CC = tracker2.update(frame)
	# track_success3,DD = tracker3.update(frame)
	
	if track_success1 : #and track_success2 and track_success3:
		
		top_left1 = (int(BB[0]),int(BB[1]))
		bottom_right1 = (int(BB[0]+BB[2]), int(BB[1]+BB[3]))
		
		"""top_left2 = (int(CC[0]),int(CC[1]))
		bottom_right2 = (int(CC[0]+CC[2]), int(CC[1]+CC[3]))
		
		top_left3 = (int(DD[0]),int(DD[1]))
		bottom_right3 = (int(DD[0]+DD[2]), int(DD[1]+DD[3]))"""
		
		cv2.rectangle(frame,top_left1,bottom_right1,(0,255,0),5)
		# cv2.rectangle(frame,top_left2,bottom_right2,(0,0,255),5)
		# cv2.rectangle(frame,top_left3,bottom_right3,(255,0,0),5)
		
		X = (int(BB[0]+BB[2])+int(BB[0]))/2
		Y = (int(BB[1]+BB[3])+int(BB[1]))/2
		
		pointXB.append(X)
		pointYB.append(Y)
		
		
	
	cv2.imshow('Output',frame)
	
	key  =  cv2.waitKey(1) & 0xff
	if key == ord('q'):
		break
	

video.release()   
# Closes all the frames 
cv2.destroyAllWindows() 
   
X = np.array(pointXB)
Y = np.array(pointYB)
plt.plot([X[0],X[-1]],[Y[0],Y[-1]],color = 'blue')
plt.plot(X,Y,color ="green", marker ='o')

plt.gca().invert_yaxis()
plt.savefig("sperm_mobility.png", dpi=600)
plt.show()