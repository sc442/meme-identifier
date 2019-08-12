from colorclassifier import *

import cv2              # sift imports
import os
import numpy as np
import operator

#
# search.py
#
# Seung-Woo Choi 2019
#
# Searches through imagefolder and matches input picture with existing picture in database using
# keypoint matching algorithm (SIFT)
#

# First, identify the dominant colors of the picture. (Use organizer/colorclassifier.py)
# Identify folder to search through that may contain the meme templates
# Apply SIFT to compare input image to each image in the folder.

def getInputImage():
    print("Please enter the image name: ")
    inputfile = input()
    return inputfile

def getDominantColors(img):
    cls = ColorClassifier()
    color = cls.classify(img)
    return color

def siftThroughColor(inputfile, colors):
    KEYPOINT_COUNT = 10

    # Adding all templates to list
    input = cv2.imread(inputfile, cv2.IMREAD_GRAYSCALE)


    templates = {}

    dirname = os.path.dirname(os.getcwd())

    print('Searching through: ')
    for c in colors[:2]:
        print('\t',c)
        targetdir = dirname + '/imagefolder/' + c[0]

        for file in os.listdir(os.fsencode(targetdir)):
            templates[os.fsdecode(file)] = cv2.imread(targetdir + '/' + os.fsdecode(file), cv2.IMREAD_GRAYSCALE)

    alg = cv2.xfeatures2d.SIFT_create()

    ####################################################################
    # Detect and compute keypoints and descriptors for input and each template

    inputkp, inputdes = alg.detectAndCompute(input, None)

    templatekp = {}
    templatedes = {}

    for t in templates:
        kp,des = alg.detectAndCompute(templates[t], None)
        templatekp[t] = kp
        templatedes[t]= des

    #######################
    # Brute Force Matching
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck = True)

    matches = {}

    for td in templatedes:
        match = bf.match(inputdes,templatedes[td])
        match = sorted(match, key = lambda x: x.distance) # Sorted by best matches
        matches[td] = match

    distances = {}

    for m in matches:
        distance = 0
        for i in range(0, KEYPOINT_COUNT):
            distance += matches[m][i].distance
        distances[m] = distance
    print("Input: " + inputfile)

    sorted_dist = sorted(distances.items(), key=operator.itemgetter(1))


    print("Best matches: ")
    for d in sorted_dist[:3]:
        # print(d[0] + ": " + str(d[1]))
        print('\t',d[0])

def main():
    inp = getInputImage()
    colors = getDominantColors(inp)
    siftThroughColor(inp, colors)

main()
