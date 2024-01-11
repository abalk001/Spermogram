
import cv2, imutils
import matplotlib.pyplot as plt
import numpy as np  
import csv 

	
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
CC = ROIs[1]
DD = ROIs[2]

tracker1.init(frame, BB)
tracker2.init(frame, CC)
tracker3.init(frame, DD)

pointXB = []
pointYB = []

pointXC = []
pointYC = []

pointXD = []
pointYD = []



while True:
	
	_,frame = video.read()
	frame = imutils.resize(frame,width=720)
	track_success1,BB = tracker1.update(frame)
	track_success2,CC = tracker2.update(frame)
	track_success3,DD = tracker3.update(frame)
	
	if track_success1 or track_success2 or track_success3:
		
		top_left1 = (int(BB[0]),int(BB[1]))
		bottom_right1 = (int(BB[0]+BB[2]), int(BB[1]+BB[3]))
		
		top_left2 = (int(CC[0]),int(CC[1]))
		bottom_right2 = (int(CC[0]+CC[2]), int(CC[1]+CC[3]))
		
		top_left3 = (int(DD[0]),int(DD[1]))
		bottom_right3 = (int(DD[0]+DD[2]), int(DD[1]+DD[3]))
		
		cv2.rectangle(frame,top_left1,bottom_right1,(0,255,0),5)
		cv2.rectangle(frame,top_left2,bottom_right2,(0,0,255),5)
		cv2.rectangle(frame,top_left3,bottom_right3,(255,0,0),5)
		
		XB = (int(BB[0]+BB[2])+int(BB[0]))/2
		YB = (int(BB[1]+BB[3])+int(BB[1]))/2

		XC = (int(DD[0]+DD[2])+int(DD[0]))/2
		YC = (int(CC[1]+CC[3])+int(CC[1]))/2

		XD = (int(DD[0]+DD[2])+int(DD[0]))/2
		YD = (int(DD[1]+DD[3])+int(DD[1]))/2
		
		pointXB.append(XB)
		pointYB.append(YB)
		pointXD.append(XD)
		pointYD.append(YD)
		pointXC.append(XC)
		pointYC.append(YC)
		
		
	
	cv2.imshow('Output',frame)
	
	key  =  cv2.waitKey(1) & 0xff
	if key == ord('q'):
		break
	

video.release()   
# Closes all the frames 
cv2.destroyAllWindows() 


figure, axis = plt.subplots(2,2)

X1 = np.array(pointXB)
Y1 = np.array(pointYB)

X2 = np.array(pointXC)
Y2 = np.array(pointYC)

X3 = np.array(pointXD)
Y3 = np.array(pointYD)

A = axis[0,0]
B = axis[0,1]
C = axis[1,0]


A.plot([X1[0],X1[-1]],[Y1[0],Y1[-1]],color = 'blue')
A.plot(X1,Y1,color ="green", marker ='o')

B.plot([X2[0],X2[-1]],[Y2[0],Y2[-1]],color = 'blue')
B.plot(X2,Y2,color ="red", marker ='o')

C.plot([X3[0],X3[-1]],[Y3[0],Y3[-1]],color = 'blue')
C.plot(X3,Y3,color ="blue", marker ='o')

A.invert_yaxis()
B.invert_yaxis()
C.invert_yaxis()

plt.show()
figure.savefig("sperm_mobility.png", dpi=600)
