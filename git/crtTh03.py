# -*- coding: utf-8 -*-

import sys
# print sys.getdefaultencoding()
import numpy as np
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import fncropimage
import cv2

numPic = 100000
nFile = str(numPic)
fileSavePic = nFile+'.bin.png'
fileSaveText = nFile+'.gt.txt'
path  =  'testdata/'

pSaveNamePic = path+fileSavePic
pSaveNameTxt = path+fileSaveText

txt = 'เขตป้อมปราบศัตรูพ่าย'
font = ImageFont.truetype("font/THSarabunNew.ttf",36)
img=Image.new("RGBA", (500,48),(255,255,255))

draw = ImageDraw.Draw(img)
draw.text((0, 0),unicode(txt,'UTF-8'),(0,0,0),font=font)
draw = ImageDraw.Draw(img)


# Convert Image(PIL) to OPENCV
imInput = np.array(img)
# cv2.imshow('res', img)
# cv2.waitKey(2000)

# Auto Crop image
fncropimage.cropImg(imInput,pSaveNamePic)

file = open(pSaveNameTxt,'w')
file.write(txt)
file.close()

# img.save("testdata/a_test.png")
