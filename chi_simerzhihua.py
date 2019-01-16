#!/user/bin/python
#  -*-coding: utf-8-*-
from PIL import Image,ImageEnhance
import pytesseract
import time
import numpy as np
import cv2

#处理图片
img = Image.open('./easy_img/shang.png').convert('L')  # 二ZZZ值化
img = ImageEnhance.Contrast(img)  # 增强对比度
img = img.enhance(2.0)  # 增加饱和度
# w,h=img.size
x=0
y=0
img.save('./easy_img/shang2.png')
img = np.array(Image.open('./easy_img/shang2.png'))
h, w = img.shape[:2]
for y in range(1, w-1):
    for x in range(1, h-1 ):
        count = 0
        # cur_pixel = easy_img.getpixel((x, y+1))
        # print"当前像素：%s"%cur_pixel
        if img[x, y ] > 127:
            img[x, y] = 0
        else:
            img[x,y] =255
cv2.imwrite('./easy_img/shang3.png', img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
time.sleep(1)
img=Image.open('./easy_img/shang3.png')
text=pytesseract.image_to_string(img,lang='chi_sim').strip()
# code = pytesseract.image_to_string(img)  # 使用image_to_string识别验证码
# a = code.strip()
print text


