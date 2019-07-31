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

    def classify(self,color):
        DistanceDict = {}
        RGBdict = self.__RGBdict
        for c in RGBdict:
            distance = self.__calculateDistance(color, RGBdict[c])
            DistanceDict[c] = distance

        return min(DistanceDict, key=DistanceDict.get)

    def __calculateDistance(self,a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
