import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

#cap = cv2.VideoCapture(0)
#while(cap.isOpened()):
for count in xrange(30):
	#ret, img = cap.read()
	cv2.namedWindow("output", cv2.WINDOW_NORMAL)
	img = cv2.imread("images/IMG_2270.JPG")
	img = cv2.resize(img, (800, 600))
	#cv2.namedWindow("img", cv2.WINDOW_NORMAL)
	#cv2.imshow("output", img)
	
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	cv2.imshow('gray',gray)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	#cv2.imshow('blur',blur)
	ret,thresh1 = cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	cv2.imshow('thresholded', thresh1)
	k = cv2.waitKey(10)
	if k == 27:
		break