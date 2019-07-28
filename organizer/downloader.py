import string
import csv
import pandas as pd
import matplotlib.pyplot as plt
import requests


# downloader.py
#
# Seung-Woo Choi 2019
#
# Scans memegenerator.csv, downloads each meme's image from URLs provided.
#
# Based off of Library of Congress's code to navigate the csv file
# https://github.com/LibraryOfCongress/data-exploration/blob/master/getting_started_with_memegenerator.ipynb
#

memeDataList = []
imageURLList = []

def populateMemeData():
    global memeDataList
    memesContained = []
    with open('memegenerator.csv', 'r', encoding='utf-16') as memedata:
        reader = csv.DictReader(memedata,delimiter='\t')
        for row in reader:
            if row['Base Meme Name'] not in memesContained:
                memesContained.append(row['Base Meme Name'])
                memeDataList.append(row)

def populateImageURLList():
    global memeDataList, imageURLList

    for row in memeDataList:
        imageURLList.append(row['Archived URL'])

def downloadImages():
    count = 0
    for url in imageURLList:
        count += 1
        img_data = requests.get(url).content
        with open('imagefolder/' + str(count) + '.jpg', 'wb') as handler:
            handler.write(img_data)

def main():
    populateMemeData()
    populateImageURLList()
    downloadImages()

main()
