import string
import csv
import requests
import os

# downloader.py
#
# Seung-Woo Choi 2019
#
# Scans memegenerator.csv, downloads each meme's image from URLs provided.
#
# Based off of Library of Congress's code to navigate the csv file
# https://github.com/LibraryOfCongress/data-exploration/blob/master/getting_started_with_memegenerator.ipynb
#

class Downloader:
    __memeDataList = []
    __imageURLList = []
    __urlIterator = 0

    def __init__(self):
        self.__populateMemeData()
        self.__populateImageURLList()
        self.__urlIterator = 0


    def __populateMemeData(self):
        memesContained = []
        with open('memegenerator.csv', 'r', encoding='utf-16') as memedata:
            reader = csv.DictReader(memedata,delimiter='\t')
            for row in reader:
                if row['Base Meme Name'] not in memesContained:
                    memesContained.append(row['Base Meme Name'])
                    self.__memeDataList.append(row)

    def __populateImageURLList(self):
        for row in self.__memeDataList:
            self.__imageURLList.append(row['Archived URL'])

    def isDone(self):
        print('Progress:', self.__urlIterator + 1, '/', len(self.__imageURLList))

        if self.__urlIterator >= len(self.__imageURLList):
            return True
        else:
            return False

    def downloadNextImage(self):
        count = self.__urlIterator

        imageFolderPath = os.path.dirname(os.getcwd()) + '/imagefolder'

        if not os.path.isdir(imageFolderPath):
            os.mkdir(imageFolderPath)

        url = self.__imageURLList[count]

        img_data = requests.get(url).content

        memefilename = imageFolderPath + '/' + self.__memeDataList[count]['Base Meme Name'] + '.jpg'
        with open(memefilename, 'wb') as handler:
            handler.write(img_data)
        self.__urlIterator += 1

        return imageFolderPath + '/' + self.__memeDataList[count]['Base Meme Name'] + '.jpg'
