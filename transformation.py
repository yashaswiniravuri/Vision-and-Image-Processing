#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 14:28:12 2022

@author: matlab
"""

from matplotlib import pyplot as plt
from skimage import io
from skimage.transform import rescale, resize, downscale_local_mean
img = io.imread('index.jpeg', as_gray=True)
plt.imshow(img)

#After I read the image Perfom transformation operation

""" For rescale - use rescale module, rescale the image by  1/4 (0.25), rescale for 25% 
Anti_aliasing True - removes jagged edges by adding subtle color changes around the lines"""


""" Resized image - image is rezied by 200, 200"""

img_rescaled = rescale(img, 1.0/4.0, anti_aliasing=True)
'''img_resized = resize(img, (50, 100), anti_aliasing=True)
plt.imshow(img)
plt.imshow(img, cmap='gray')'''
plt.imshow(img_rescaled, cmap='gray')
'''plt.imshow(img_resized, cmap='gray')
img_downscaled = downscale_local_mean(img, (8,3))   # it strech the image by 8 by 3
plt.imshow(img_downscaled, cmap='gray')'''