#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:03:31 2018

@author: suzuki
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def histgram(imgpath):
    '''
    #http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html
    '''
    img = cv2.imread(imgpath,cv2.IMREAD_COLOR)
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()

def histgram2d(imgpath):
    '''
    #https://docs.opencv.org/3.1.0/dd/d0d/tutorial_py_2d_histogram.html
    '''
    img = cv2.imread(imgpath,cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv],[0,1],None,[18,25],[0,180,0,256])
    plt.imshow(hist,interpolation='nearest')
    plt.show()
    

def histgram2d_test():
    math = np.asarray([85, 90, 60, 55, 72, 91, 82, 91, 60, 65], dtype = 'uint8')
    eng  = np.asarray([65, 80, 50, 60, 80, 60, 86, 95, 74, 54], dtype = 'uint8')
    hist3 = cv2.calcHist([math,eng],[0,1],None,[5,5],[0,100,0,100])
    plt.imshow(hist3,interpolation='nearest')
    plt.show()
   
    ret, hist4 = cv2.threshold(hist3,thresh=1,maxval=10,type=cv2.THRESH_TOZERO)
    plt.imshow(hist4,interpolation='nearest')
    plt.show()

    #http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_histograms/py_histogram_backprojection/py_histogram_backprojection.html
    norm = cv2.normalize(hist4, hist4, 0, 255, cv2.NORM_MINMAX)
    dst = cv2.calcBackProject([math,eng][0,1], norm, [0,100,0,100], 1)
    plt.imshow(dst,interpolation='nearest')
    plt.show()


def main():
    
    path = 'images/20170709_001.jpg'
    
    bgr_img = cv2.imread(path,cv2.IMREAD_COLOR)
    plt.imshow(bgr_img)
    plt.show()

    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_img)
    plt.show()
    
    gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
    plt.imshow(gray_img)
    plt.show()
 
    histgram(path)    
    histgram2d(path)    
    histgram2d_test()    
    
if __name__=='__main__':
    main()
    