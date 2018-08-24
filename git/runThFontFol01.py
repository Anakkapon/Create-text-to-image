# -*- coding: utf-8 -*-

import sys
# print sys.getdefaultencoding()
import numpy as np
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import cv2

import fncropimage
import fnCreateTextimage
import GetFileNameinFolder



numPic = 200000
fname = 'l1.txt'
path  =  'ocrtrain2/'

with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

www = GetFileNameinFolder.GetFontNameArray()
for e,nFont  in  enumerate(www):
    print nFont

    for  i in range(len(content)):
        # print content[i]

        nFile = str(numPic)
        fileSavePic = content[i]+'.jpg'
        fileSaveText = nFile+'.gt.txt'
        # path  =  'testdata/'


        pSaveNamePic = path+fileSavePic
        pSaveNameTxt = path+fileSaveText

        imInputs = fnCreateTextimage.CreateImageText(nFont,content[i]+"\r\n")
        # cv2.imshow('res', imInputs)
        # cv2.waitKey(2000)

        # Auto Crop image
        fncropimage.cropImg(imInputs,pSaveNamePic)

        file = open(pSaveNameTxt,'w')
        file.write(str(content[i]))
        file.close()
        numPic = numPic+1

# img.save("testdata/a_test.png")
