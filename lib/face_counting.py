#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:14:00 2018

@author: zailchen
"""

import numpy as np
import cv2
from math import sin, cos, radians


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
