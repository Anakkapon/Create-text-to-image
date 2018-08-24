# -*- coding: utf-8 -*-

import sys
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

fname = 'listtext.txt'

with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

for  i in range(len(content)):
    print content[i]
