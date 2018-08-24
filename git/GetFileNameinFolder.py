import cv2
import fncropimage
import glob, os
dirList = os.listdir("font/")
# os.chdir('/home/mungking/opus/Ladgrabang/')

def GetFontNameArray():
    arrayLs =[]
    a = 0
    for root, dirs, files in os.walk('./'):
        for dir in dirs:
            for root, dirs, files in os.walk(dir):
                if dir == 'font':
                    for name in files:
                        ff = dir + '/'+ name
                        # print(ff)
                        arrayLs.append(ff)
    return arrayLs
