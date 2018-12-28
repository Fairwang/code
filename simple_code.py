#!/user/bin/python
#  -*-coding: utf-8-*-
from PIL import Image,ImageEnhance
import pytesseract
from selenium import webdriver
import time


# from array import *
# import numpy as np
#  Numpy
import numpy
def isElementExistid(element):
    flag = True
    # driver = self.driver
    try:
        driver.find_element_by_id(element)
        return flag
    except:
        flag = False
        return flag
#支付demo界面
driver=webdriver.Chrome()
# driver.get('https://testpay.hongnaga.com/merchant.html')
driver.get("https://pay.hongnaga.com/merchant/login")
# driver.get('https://cpay.hypayde.com/merchant')
# driver.get('http://47.75.86.174:8092/posa/merlogin.jsp')
driver.maximize_window()
driver.find_element_by_id("mch_id").clear()
driver.find_element_by_id("mch_id").send_keys(12001)
driver.find_element_by_id("password").clear()
# driver.find_element_by_id("password").send_keys(123456)
driver.find_element_by_id("password").send_keys("chilong123456")
driver.find_element_by_id("captcha").send_keys(0)
driver.find_element_by_id("sub").click()
time.sleep(2)
element="error"

for i in range(10):
    if isElementExistid(element):
        tishi=driver.find_element_by_id(element).text
        print driver.find_element_by_id(element).text
        # link_text="验证码错误"
        if tishi==u"验证码错误":
            driver.find_element_by_id("captcha_img").click()
            driver.save_screenshot('./easy_img/origin.png')
            id = driver.find_element_by_id("captcha_img")
            # id=driver.find_element_by_id("randImage")
            size = id.size
            location = id.location
            rangle = (int(location['x']), \
                      int(location['y']), \
                      int(location['x'] + size['width']), \
                      int(location['y'] + size['height']))
            img = Image.open('./easy_img/origin.png')
            img = img.crop(rangle)
            img = img.save('./easy_img/caijian.png')  # 裁剪验证码
            time.sleep(1)
            img = Image.open('./easy_img/caijian.png').convert('L')  # 二ZZZ值化
            img = ImageEnhance.Contrast(img)  # 增强对比度
            img = img.enhance(2.0)  # 增加饱和度
            img.save('./easy_img/duibi.png')
            code = pytesseract.image_to_string(img)  # 使用image_to_string识别验证码
            a = code.strip()
            print a


            driver.find_element_by_id("captcha").clear()
            driver.find_element_by_id("captcha").send_keys(a)
            driver.find_element_by_id("sub").click()
            time.sleep(2)
            element2="password"
    else:
        break

print "success"