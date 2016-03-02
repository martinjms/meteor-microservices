import sys
import numpy as np
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
from matplotlib import pyplot as plt

def procesarImagen(binary) : 
	print()
	#img = cv2.imread("/home/msuarez/code/celulas/ENSAYO1/magneto/t1.jpg",1)
	nparr = np.fromstring(binary , np.uint8)
	img = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
	img = img[55:425,243:430]
	
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	
	plt.subplot(131),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	
	kernel = np.ones((5,5),np.uint8)
	e = (1,1,1,1)
	while e > (0,0,0,0):
		'''img2 = cv2.dilate(img,kernel,iterations = 1)
		img3 = cv2.max(cv2.erode(img2,kernel,iterations = 1),img)'''
		img3 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
		d = cv2.absdiff(img,img3)
		e = cv2.sumElems(d)
		img = img3
	
	plt.subplot(132),plt.imshow(img),plt.title('Paso 1')
	plt.xticks([]), plt.yticks([])
		
	e = (1,1,1,1)
	while e > (0,0,0,0):
		'''img2 = cv2.erode(img,kernel,iterations = 1)
		img3 = cv2.min(cv2.dilate(img2,kernel,iterations = 1),img)'''
		img3 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)	
		d = cv2.absdiff(img,img3)
		e = cv2.sumElems(d)
		img = img3
	
	plt.subplot(133),plt.imshow(img),plt.title('Final')
	plt.xticks([]), plt.yticks([])
	# plt.show()
	nparr2 = cv2.imencode('.jpg',img)
	binary2 =  cv2.imencode('.jpg', img)[1].tostring()
	return binary2
	

def pruebaThreshhold(binary) :
	nparr = np.fromstring(binary , np.uint8)
	img = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
	ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
	ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
	ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
	ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
	ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
	 
	thresh = ['img','thresh1','thresh2','thresh3','thresh4','thresh5']
	 
	for i in xrange(6):
	    plt.subplot(2,3,i+1),plt.imshow(eval(thresh[i]),'gray')
	    plt.title(thresh[i])
	 
	plt.show()