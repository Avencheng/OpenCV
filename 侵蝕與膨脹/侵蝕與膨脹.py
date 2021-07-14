#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 11:30:16 2021

@author: user
"""

import cv2

image = cv2.imread('黑點白底.png', 0)
bgblack= cv2.bitwise_not(image)# 轉成黑底
erode = cv2.erode(bgblack, None, iterations=40) #侵蝕
dilate = cv2.dilate(erode, None, iterations=200) #膨脹
image = cv2.hconcat([image, bgblack, erode, dilate])
cv2.imshow('image', image)
cv2.waitKey(0)