#!/user/bin/python
#  -*-coding: utf-8-*-
from PIL import Image,ImageEnhance
import pytesseract
import time
from array import *
import numpy as np
# import Numpy
import cv2
import numpy
def line_noise(file_path):
    img=np.array(Image.open(file_path))
    h, w = img.shape[:2]
    for y in range(1, w - 1):
        for x in range(1, h - 1):
            count = 0
            print "33"
            # cur_pixel = easy_img.getpixel((x, y+1))
            # print"当前像素：%s"%cur_pixel
            if img[x, y + 1] >127:
                count = count + 1
            if img[x, y + 1] > 127:
                count = count + 1
            if img[x - 1, y] > 127:
                count = count + 1
            if img[x + 1, y] > 127:
                count = count + 1
            if count > 2:
                img[x, y] = 255
    cv2.imwrite('D:\\code\\code_line.png', img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    return img

