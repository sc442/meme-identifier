from colorclassifier import *
from downloader import *

import os

# organizer.py
#
# Seung-Woo Choi 2019
#
# Downloads and Organizes images in imagefolder into color averages.
# Library of Congress Meme Generator Dataset
# https://labs.loc.gov/experiments/webarchive-datasets/
#

dl = Downloader()
clc = ColorClassifier()

def moveIntoFolder(img, color):
    split = img.split('/')
    imgname = split[len(split) -1]
    print(imgname)
    print(color)
    print()

    imgdir = os.path.dirname(img)
    colordir = imgdir + '/' + color

    if not os.path.isdir(colordir):
        os.mkdir(colordir)

    os.rename(img, colordir+'/'+imgname)


def main():
    while not dl.isDone():
        img = dl.downloadNextImage()

        color = clc.classify(img)

        moveIntoFolder(img,color)

    print("Finished downloading and organizing template images!")


main()
