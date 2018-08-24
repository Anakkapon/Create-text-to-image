import cv2
import numpy as np
import fncropimage


a = '0.jpg'
b = 'aaa'+a
fncropimage.crop(a,b)

# im = cv2.imread('0.jpg')
# # img = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY,None,None)
# img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# ret, im2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('res', im2)
#
# kernel = np.ones((5, 5), np.uint8)
# dilation = cv2.dilate(im2, kernel, iterations=1)
# ret2, im3 = cv2.threshold(dilation, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow('res1', im3)
#
# contours, hierarchy = cv2.findContours(im3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnt = contours[0]
#
# x, y, w, h = cv2.boundingRect(cnt)
# cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imshow('res3', im)
#
# crop_img = im2[y:y+h,x:x+w]
# cv2.imwrite('aaaa.jpg',crop_img)

while True:
    ch = cv2.waitKey()

    if ch == 27:  # Escape
        cv2.destroyAllWindows()
        break
