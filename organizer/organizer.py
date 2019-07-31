import cv2
import numpy as np
from skimage import io

from colorclassifier import *

# organizer.py
#
# Seung-Woo Choi 2019
#
# Organizes images in imagefolder into color averages.
#


###################################

img = io.imread('imagefolder/Alright Then Business Kid.jpg')

pixels = np.float32(img.reshape(-1, 3))

n_colors = 5
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
flags = cv2.KMEANS_RANDOM_CENTERS

_, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
_, counts = np.unique(labels, return_counts=True)

dominant = palette[np.argmax(counts)]

indices = np.argsort(counts)[::-1]

for i in range(3):                      # Print the 3 most common RGB Values
    print('Common rgb value', i, ':', palette[indices[i]])

clrcls = ColorClassifier()
print('Primary color is: ', clrcls.classify(palette[indices[0]]))
