import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('koivu1.jpg',0)
img2 = cv2.imread('koivu2.jpg',0)

orb = cv2.ORB_create() 
keypoints = orb.detect(img,None)
keypoints, descriptions = orb.compute(img, keypoints)

keypoints2 = orb.detect(img2,None)
keypoints2, descriptions2 = orb.compute(img2, keypoints2)

img4 = cv2.drawKeypoints(img,keypoints,None,(255,0,0),4)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True) 
matches = bf.match(descriptions, descriptions2)
img3 = cv2.drawMatches(img,keypoints,img2,keypoints2,matches,None,flags=2)

plt.imsave('vertailu.png', img3)



