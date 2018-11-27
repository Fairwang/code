#!/user/bin/python
#  -*-coding: utf-8-*-
from PIL import Image,ImageEnhance
import pytesseract
from selenium import webdriver
import time
# from array import *

#支付demo界面
driver=webdriver.Chrome()
# driver.get('https://testpay.hongnaga.com/merchant.html')
driver.get("https://pay.hongnaga.com/merchant/login")
# driver.get('https://cpay.hypayde.com/merchant')
# driver.get('http://47.75.86.174:8092/posa/merlogin.jsp')
# driver.maximize_window()
driver.add_cookie({'name':'mch_id','value':'12001'})
driver.add_cookie({'name':'password','value':'chilong123456'})
driver.get("https://pay.hongnaga.com/merchant/login")

