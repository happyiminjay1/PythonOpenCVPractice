#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:41:11 2019

@author: happyiminjay
"""

import numpy
import cv2

img = cv2.imread('lena.jpg',1)

print(img)

cv2.imshow('image',img)
key = cv2.waitKey(0) & 0xFF

print(key)
if key != 's': #s is a key
      cv2.destroyAllWindows()
    
elif key == ord('s'):
    cv2.imwrite('lena_copy1.png',img)
    cv2.destroyAllWindows()
    print("Saved")

print("Ended")
