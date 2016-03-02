import sys
import numpy as np
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("/home/msuarez/code/celulas/ENSAYO1/magneto/t1.jpg",1)

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