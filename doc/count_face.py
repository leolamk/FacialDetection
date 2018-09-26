def counting_face():
	import numpy as np
	import cv2
	from matplotlib import pyplot as plt

	# loading OpenCV cascade for haar method with frontal face
	face_cascade = cv2.CascadeClassifier('../lib/haarcascade_frontalface_default.xml')

	# loading test image
	img = cv2.imread('../data/test_image/104.jpg')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.2, 5)

	# implementing model
	for (x,y,w,h) in faces:
	    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),8)

	# showing image
	RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	plt.figure(figsize=(12,8))
	plt.imshow(RGB_img)
	plt.show()
