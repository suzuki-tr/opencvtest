#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: suzuki

https://docs.opencv.org/3.3.0/d8/dfe/classcv_1_1VideoCapture.html
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
"""

import cv2

VIDEO='Reaviling_Sjusjoen_Ski_Senter.mp4'

cap = cv2.VideoCapture(VIDEO)
print('start')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == False:
        print('video finish')
        break

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('frame.jpg',gray)
    print('wrote frame')
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
print('finish')

