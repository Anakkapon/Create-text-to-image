#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
print sys.getdefaultencoding()

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps


txt =u"เชียงใหม้ดด" +u"\u0E48"
font = ImageFont.truetype("font/Sarun's ThangLuang.ttf",36)

box = font.getsize(txt)  
img=Image.new("RGB", (500,250),(255,255,255))
draw = ImageDraw.Draw(img)
#draw.text((0, 50),unicode(txt,'UTF-8'),(0,0,0),font=font)

draw.text ( (10,10), txt, font=font, fill=(0,0,0) )

#draw.text((0, 50),txt,font=font)
#draw = ImageDraw.Draw(img)
img.save("a_test.png")
