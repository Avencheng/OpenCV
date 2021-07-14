#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 11:07:21 2021

@author: user
"""

import cv2 
import time
cap = cv2.VideoCapture(0)
time.sleep(3)
bg= None
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (400, 225))
    frame = cv2.flip(frame, 1)
    blur = cv2.GaussianBlur(frame, (11, 11), 0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    if bg is None:
        bg= gray
        continue
    
    diff = cv2.absdiff(bg, gray)
    diff = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)[1]
    diff = cv2.erode(diff, None, iterations=10)
    diff = cv2.dilate(diff, None, iterations=10)
    out = cv2.bitwise_and(frame, frame, mask=diff)
    
    cnts, hierarchy = cv2.findContours(
        diff, 
        cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        if cv2.contourArea(c) < 400: #contours是外框矩形
            continue
        (x, y, w, h) = cv2.boundingRect(c) #boundingRect會在不規則矩形外面匡一個最小外接矩形
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.drawContours(frame, cnts,-1,(255,255,0),2)
    cv2.imshow("frame", frame)
    
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break