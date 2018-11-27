#!/user/bin/python
#  -*-coding: utf-8-*-
from PIL import Image,ImageEnhance
import pytesseract
from selenium import webdriver
import time
from array import *
import numpy as np
# import Numpy
import cv2
import numpy
import segmentation
import point_noise,line_noise

#支付demo界面
driver=webdriver.Chrome()
driver.get('https://pay.hongnaga.com/merchant/login')
# driver.get('https://cpay.hypayde.com/merchant/login.html')

driver.maximize_window()
driver.save_screenshot('D:\\code\\code.png')
id=driver.find_element_by_id("captcha_img")
size=id.size
location=id.location
rangle=(int(location['x']),\
        int(location['y']), \
        int(location['x']+size['width']), \
        int(location['y']+size['height']))
png=Image.open('D:\\code\\code.png')
png2=png.crop(rangle)
pic=png2.save('D:\\code\\code2.png')#裁剪验证码
time.sleep(5)
img0=Image.open('D:\\code\\code2.png').convert('L')#二值化
img1=img0.save('D:\\code\\code3.png')
img=np.array(Image.open('D:\\code\\code3.png'))
line_noise.line_noise()
point_noise.point_noise()

im_res='D:\\code\\code5.png'
im2, contours, hierarchy = cv2.findContours(im_res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
result = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w == w_max: # w_max是所有contonur的宽度中最宽的值
        box_left = np.int0([[x,y], [x+w/2,y], [x+w/2,y+h], [x,y+h]])
        box_right = np.int0([[x+w/2,y], [x+w,y], [x+w,y+h], [x+w/2,y+h]])
        result.append(box_left)
        result.append(box_right)
    else:
        box = np.int0([[x,y], [x+w,y], [x+w,y+h], [x,y+h]])
        result.append(box)




# png8=img.save('D:\\code\\code3.png')
cv2.imwrite('D:\\code\\code5.png',img, [int(cv2.IMWRITE_PNG_COMPRESSION),0])
# cv2.imshow("code5.png",img)
img111=pytesseract.image_to_string(img)#使用image_to_string识别验证码
print "png999 %s"%img111
