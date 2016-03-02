import sys
from pymongo import MongoClient
import gridfs
import numpy as np
sys.path.append('/usr/local/lib/python2.7/site-packages')
from bioUtils import procesarImagen
from bioUtils import pruebaThreshhold
import cv2
import json


client= MongoClient('127.0.0.1',3001)
db = client.meteor
images = gridfs.GridFS(db, collection='images')
originalImages = gridfs.GridFS(db, collection='originalImages')
processedImages = gridfs.GridFS(db, collection='processedImages')
print(images.list())



for image in processedImages.find() : 
	imgFile = image.read()
	processedImages.delete(image._id);
	originalImages.put(imgFile, filename = image.filename, contentType = image.contentType,  metadata = image.metadata)
	imgFile = procesarImagen(imgFile)
	# print image.contentType
	processedImage = processedImages.new_file()
	# print imgFile.__class__
	processedImage.write(imgFile)
	processedImages.put(imgFile, filename = image.filename, contentType = image.contentType,  metadata = image.metadata)
	# pruebaThreshhold(imgFile)
# print(processedImages.list())

# print processedImages.find()[0].filename
'''
trialId = sys.argv[1]

trials = db.trials.find()
'''
'''for trial in trials :
	trial['processedImages'] = []
	print(trial['name'])
	for image in trial['images']:
		print(images.list())
		#imgFile = fs.get(image['EJSON$value']['EJSON_id'])
		#imgFile = procesarImagen(imgFile)
		#trial['processedImages'].append(imgFile)
	#db.trials.saveupdate()
'''	
	
# trials.remove({})
