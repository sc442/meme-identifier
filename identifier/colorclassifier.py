import cv2
import numpy as np
from skimage import io

import os

#
# colorclassifier.py
#
# Seung-Woo Choi 2019
#
# Assigns a given color to a known color by comparing how close its rgb values
# are to known values
#

class ColorClassifier:
    __RGBdict = {}

    def __init__(self):
        self.__RGBdict = {
            'Black': (0,0,0),
            'White': (255,255,255),
            'Red' : (255,0,0),
            'Orange' : (255,165,0),
            'Lime': (0,255,0),
            'Blue' : (0,0,255),
            'Yellow' : (255,255,0),
            'Cyan' : (0,255,255),
            'Magenta' : (255,0,255),
            'Silver' : (192,192,192),
            'Gray' : (128,128,128),
            'Maroon' : (128,0,0),
            'Olive' : (128,128,0),
            'Green' : (0,128,0),
            'Purple' : (128,0,128),
            'Teal' : (0,128,128),
            'Navy' : (0,0,128)
        }

    def __calculateRGB(self, img):
        try:
            img = io.imread(img)
        except:
            return (-1,-1,-1)

        pixels = np.float32(img.reshape(-1, 3))

        n_colors = 5
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
        flags = cv2.KMEANS_RANDOM_CENTERS

        _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
        _, counts = np.unique(labels, return_counts=True)

        dominant = palette[np.argmax(counts)]

        return dominant

    def classify(self,img):

        color = self.__calculateRGB(img)

        if color[0] == -1:
            return '!Woops!'

        DistanceDict = {}
        RGBdict = self.__RGBdict
        for c in RGBdict:
            distance = self.__calculateDistance(color, RGBdict[c])
            DistanceDict[c] = distance

        return min(DistanceDict, key=DistanceDict.get)

    def __calculateDistance(self,a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
