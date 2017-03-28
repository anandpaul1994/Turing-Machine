from imutils import contours
import numpy as np
import imutils
import cv2,os

def det():
	#read image and find dimensions
	os.system('python cam.py')
	img=cv2.imread("test.jpg")
	height, width, channels = img.shape

	# Convert BGR to HSV
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# define range of green color in HSV
	lower_green = np.array([55,50,70])
	upper_green = np.array([95,255,255])

	# Threshold the HSV image to get mask of only green color region
	mask = cv2.inRange(hsv, lower_green, upper_green)
	#crop mask to get required window and blur it to reduce errors
	mask = mask[:,120:350]
	#cv2.imwrite("new3.jpg",img)
	mask = cv2.GaussianBlur(mask, (5, 5), 0)
	cv2.imwrite("mask.jpg",mask)

	#find contours in mask
	(cnts,_) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	#discard all detected contours except for the largest one
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:1]

	for c in cnts:
		area = cv2.contourArea(c)
		print area
		
		if area<1000:
			return(' ')
		elif area<3500:
			return('1')
		else:
			return('0')

	return(' ')
#cv2.imwrite("new4.jpg",mask)
#cv2.imshow("mask",mask)
#cv2.waitKey(0)
#det()
