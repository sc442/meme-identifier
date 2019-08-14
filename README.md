# meme-identifier

![image](coolmeme.png)

Meme Identifier matches input images with memes recorded in the Library of Congress Meme Generator Dataset. In its current implementation, search.py works best with "macro image" style memes where text is superimposed upon a base image.

## Introduction

There are two parts to Meme Identifier:

Organizer: organizer.py downloads unique memes from the Library of Congress Meme Generator Dataset, then organizes them by color using k-means clustering and identifying the dominant colors in a meme. Unique instances of a meme are stored in the directory 'meme-identifier/imagefolder'.

Identifier: search.py takes an input image and identifies its dominant colors. It will then look through meme-identifier/imagefolder/[dominant color], where [dominant color] being the image's dominant color. It will also look through the second most dominant color in case of close dominance between two colors. When comparing the input image with each image in the folder, search.py uses SIFT ([Scale Invariant Feature Transform, credit to Dr David Lowe of the UBC](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform)), and prints the images with the least amount of difference with the input according to SIFT. 

## Running

Required packages: cv2, numpy, skimage, 

### Organizer

The main file, organizer.py, requires memegenerator.csv, downloader.py, colorclassifier.py:

memegenerator.csv - [Library of Congress Meme Generator dataset](https://labs.loc.gov/experiments/webarchive-datasets/)

downloader.py - Goes through memegenerator.csv and downloads images from the URLs provided by the dataset

colorclassifier.py - Provides the most dominant colors in an image using k-means clustering

To run organizer.py: `python3 organizer.py`

### Identifier

The main file, search.py, requires the version of colorclassifier.py in the identifier folder. Make sure the imagefolder is already populated with color-sorted memes/images using organizer.py.

To run search.py: `python3 search.py`

The program will prompt the user for an image. You may copy-paste an image into the same directory, then directly type the image name ('example.jpg') to search for the type of meme.

## Recognition

[User Tonechas on stackoverflow explaining average vs dominant colors in an image](https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv)

[OpenCV post on using SIFT, created by Dr David Lowe of the UBC](https://docs.opencv.org/3.3.0/da/df5/tutorial_py_sift_intro.html)

[YouTuber pysource's tutorial on feature detection using OpenCV](https://www.youtube.com/watch?v=USl5BHFq2H4&list=PL4dFf_BXheCGaVr6LOWU9xgnWtIjAtzwm)
