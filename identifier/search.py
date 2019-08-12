from colorclassifier import *

import cv2              # sift imports
import os
import numpy as np

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

def getDominantColor(img):
    cls = ColorClassifier()
    color = cls.classify(img)
    return color

def siftThroughColor(inputfile, color):
    KEYPOINT_COUNT = 10

    # Adding all templates to list
    input = cv2.imread(inputfile, cv2.IMREAD_GRAYSCALE)


    templates = {}

    dirname = os.path.dirname(os.getcwd())

    # Need to figure out parent directory, then color directory

    targetdir = dirname + '/imagefolder/' + color

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
    print("Matched with: " + min(distances, key=lambda k: distances[k]))
    print("")

    for d in distances:
        print(d + ": " + str(distances[d]))

def main():
    inp = getInputImage()
    color = getDominantColor(inp)
    print('color:', color)
    siftThroughColor(inp, color)

main()
