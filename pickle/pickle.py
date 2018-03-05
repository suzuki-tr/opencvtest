# -*- coding: utf-8 -*-
"""
https://docs.python.jp/2/library/pickle.html
"""

import pickle
import cv2
#import matplotlib.pyplot as plt

fkp = 'temp.kp.pickle'
fdes = 'temp.des.pickle'

#obj = {'key':'data'} # pickable
im = cv2.imread('images/20170709_001.jpg') # pickable

detector = cv2.AKAZE_create()
kp1, des1 = detector.detectAndCompute(im, None)

with open(fkp,'wb') as f:
    pickle.dump(kp1,f)

with open(fdes,'wb') as f:
    pickle.dump(des1,f)

with open(fkp,'rb') as f:
    kpout =pickle.load(f)

with open(fdes,'rb') as f:
    desout =pickle.load(f)


#plt.imshow(out)
#plt.show()
#print (out['key'])