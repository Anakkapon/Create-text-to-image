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


def CreateImageText(fontPath,txt):
    # txt = 'เขตป้อมปราบศัตรูพ่าย'
    # fontPaths = "font/THSarabunNew.ttf"
    font = ImageFont.truetype(fontPath,36)
    img=Image.new("RGBA", (500,200),(255,255,255))

    draw = ImageDraw.Draw(img)
    draw.text((0, 60),unicode(txt,'UTF-8'),(0,0,0),font=font)
    draw = ImageDraw.Draw(img)

    imInput = np.array(img)
    return imInput
