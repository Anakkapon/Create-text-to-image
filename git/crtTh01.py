# -*- coding: utf-8 -*-

import sys
import numpy as np
# print sys.getdefaultencoding()

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import fncropimage
import cv2


txt = 'เชียงใหม่'
font = ImageFont.truetype("font/Sarun's ThangLuang.ttf",36)

img=Image.new("RGBA", (500,48),(255,255,255))
draw = ImageDraw.Draw(img)
draw.text((0, 0),unicode(txt,'UTF-8'),(0,0,0),font=font)
draw = ImageDraw.Draw(img)

# Auto Crop image

imInput = np.array(img)
imInput.save("tmp.png")
imInput = cv2.imread("tmp.png",0)

# cv2.imshow('res', imInput)
# cv2.waitKey(2000)

#fncropimage.cropImg(imInput,"testdata/a_test.png")

# img.save("testdata/a_test.png")
