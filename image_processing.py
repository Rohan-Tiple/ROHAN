# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:51:34 2019

@author: ROHAN
"""
from matplotlib import cm
import matplotlib.cm as cm
from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog,blob_log, blob_doh
from skimage.color import rgb2gray
import glob
from skimage.io import imread
from math import sqrt



# import image 

example_file = glob.glob(r"C:\Users\ROHAN\Desktop\MIZAR.jpg")[0]
im = imread(example_file, as_grey=True)
plt.imshow(im, cmap=cm.gray)
plt.show()


blobs_log = blob_log(im, max_sigma=30, num_sigma=10, threshold=.1)
#compute radii in the 3rd column.
blobs_log[:,2] = blobs_log[:,2]* sqrt(2)
numrows = len(blobs_log)
print("Number of stars counted :", numrows)

fig, ax = plt.subplots(1,1)
plt.imshow(im, cmap=cm.gray)
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=False)
    ax.add_patch(c)
    

