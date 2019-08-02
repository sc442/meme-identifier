from colorclassifier import *
from downloader import *

# organizer.py
#
# Seung-Woo Choi 2019
#
# Downloads and Organizes images in imagefolder into color averages.
#

dl = Downloader()
clc = ColorClassifier()

def main():
    while not dl.isDone():
        img = dl.downloadNextImage()

        print(img)
        print(clc.classify(img))

    print("Finished downloading and organizing template images!")


main()
