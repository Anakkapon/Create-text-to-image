import cv2
import numpy as np

def crop(file,savefile):

    im = cv2.imread(file)
    im = cv2.resize(im,(410,90))
    # img = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY,None,None)

    img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, im2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow('res', im2)

    kernel = np.ones((7, 7), np.uint8)
    dilation = cv2.dilate(im2, kernel, iterations=2)
    ret2, im3 = cv2.threshold(dilation, 127, 255, cv2.THRESH_BINARY)
    # cv2.imshow('res1', im3)

    contours, hierarchy,_ = cv2.findContours(im3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]

    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # cv2.imshow('res3', im)

    crop_img = im2[y:y+h,x:x+w]
    cv2.imwrite(savefile,crop_img)


def cropImg(img,savefile):

    imge = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, im2 = cv2.threshold(imge, 127, 255, cv2.THRESH_BINARY_INV)

    # cv2.imshow('invert',im2)
    # cv2.waitKey(2000)

    kernel = np.ones((5, 5), np.uint8)
    di = cv2.dilate(im2, kernel, iterations=1)
    ret2, im3 = cv2.threshold(di, 20, 255, cv2.THRESH_BINARY)
    # cv2.imshow('res', im2)
    im2,contours, hierarchy = cv2.findContours(im3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.imshow('invert',im3)
    # cv2.waitKey(2000)

    xMax2 = 0;
    yMax2 = 0;
    xMin2 = 10000;
    yMin2 = 10000;
    for r in range(len(contours)):
        cnt = contours[r]
        x, y, w, h = cv2.boundingRect(cnt)

        if x+w >= yMax2:
            yMax2 = x+w-22

        if y+h  >= xMax2:
            xMax2 = y+h

        if y<xMin2:
            xMin2 = y

        if x <yMin2:
            yMin2 = x


    # print xMax2
    # print yMax2
    crop_img = img[xMin2:xMax2 ,yMin2:yMax2]
    #cv2.imwrite(savefile,crop_img)
    cv2.imwrite(savefile,crop_img)
    #cv2.imwrite(savefile,img)




def preProcess(file):
    im = cv2.imread(file)

    ### Adaptive Resize image
    height, width, channels = im.shape
    print str(width)
    print str(height)

    PixelH = 60.0*8.0
    ratio = PixelH/height
    print str(ratio)

    new_h = int((height *ratio) +0.5)
    new_w = int((width * ratio) +0.5)
    im = cv2.resize(im, (new_w,new_h),interpolation=cv2.INTER_LINEAR)

    # ### Smooth filter
    # im = cv2.GaussianBlur(im,(3,3),0)
    # cv2.imshow('res', im)
    # cv2.waitKey(2000)
    # ret2, im3 = cv2.threshold(im, 100, 255, cv2.THRESH_BINARY)

    return im


def extectObj(im):

    img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, im2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow('res', im2)
    # cv2.waitKey(2000)

    kernel = np.ones((15, 15), np.uint8)
    dilation = cv2.dilate(im2, kernel, iterations=1)
    ret2, im3 = cv2.threshold(dilation, 127, 255, cv2.THRESH_BINARY)
    # cv2.imshow('res1', im3)
    # cv2.waitKey(2000)

    hierarchy,contours ,_ = cv2.findContours(im3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    imgArray = []
    inx = 0
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)

        crop_img = im2[y:y+h,x:x+w]
        imgArray.append(crop_img)
        inx = inx +1

    return inx,imgArray


#
# #### Sample code
#
# W = preProcess("t1.png")
# c,imgA =extectObj(W)
#
# print str(c)
#
# for r in imgA:
#     cv2.imshow("Image",r)
#     cv2.waitKey(2000)
