#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 20:24:20 2018

@author: zailchen
"""

def face_dectect_image(directory = '../data/test_image/cascade/', scaleFactor = 1.3, minNeighbors = 5):

    import numpy as np
    import cv2
    import tensorflow
    import os
    from matplotlib import pyplot as plt
    
    
      # I followed Harrison Kingsley's work for this
      # Much of the source code is found https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/
    
    def rotate_image(img, angle):
        if angle == 0: return img
        # print("checked for shape".format(image.shape))
        height, width = img.shape[:2]
        rot_mat = cv2.getRotationMatrix2D((width/2, height/2), angle, 0.9)
        result = cv2.warpAffine(img, rot_mat, (width, height), flags=cv2.INTER_LINEAR)
        return result
    
    def rotate_point(pos, img, angle):
        if angle == 0: return pos
        x = pos[:,0] - img.shape[1]*0.4
        y = pos[:,1] - img.shape[0]*0.4
        newx = x*cos(radians(angle)) + y*sin(radians(angle)) + img.shape[1]*0.4
        newy = -x*sin(radians(angle)) + y*cos(radians(angle)) + img.shape[0]*0.4
        return np.array((newx, newy, pos[:,2], pos[:,3]), int).T
    
    
    face_cascade = cv2.CascadeClassifier('../lib/haarcascade_frontalface_default.xml')
    
    
    PATH_TO_TEST_IMAGES_DIR = directory
    TEST_IMAGES_NAMES = os.listdir(directory)
    TEST_IMAGE_PATHS = [os.path.join(PATH_TO_TEST_IMAGES_DIR, TEST_IMAGES_NAMES[i]) for i in range(1,len(TEST_IMAGES_NAMES))]
    n = len(TEST_IMAGE_PATHS)

    for image in TEST_IMAGE_PATHS: 
    
        img = cv2.imread(image)
        length = int(max(img.shape[0:2]))
        height = int(min(img.shape[0:2]))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        i = 0
        
        for angle in [0, -30, 30]:
            rimg = rotate_image(gray, angle)
            faces = face_cascade.detectMultiScale(rimg, scaleFactor, minNeighbors)
            
            if len(faces):
                    faces = rotate_point(faces, img, -angle)
                    break
        
        
        if len(faces) == 0:
            print("No faces found")
         
        else:         
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),10)
            cv2.rectangle(img, ((0,img.shape[0] -25)),(270, img.shape[0]), (255,255,255), -1)
            
        if type(faces) == tuple:
            cv2.putText(img, "Number of faces detected: 1" , (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
        else:
            cv2.putText(img, "Number of faces detected: " + str(faces.shape[0]), (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
                    
        RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.figure(figsize=(12,8))
        plt.imshow(RGB_img)
        plt.show()
            
        cv2.imwrite('../output/processed_{}'.format(TEST_IMAGES_NAMES[i+1]),img)
        i +=1
        



