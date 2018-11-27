#!user/bin/python
# coding: utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

#!/user/bin/python
#  -*-coding: utf-8-*-
from PIL import Image,ImageEnhance
import pytesseract
from selenium import webdriver
import time
# from array import *
import numpy as np
#  Numpy
import numpy
import cv2
from code.common import table

def isElementExistid(element):
    flag = True
    # driver = self.driver
    try:
        driver.find_element_by_id(element)
        return flag
    except:
        flag = False
        return flag

driver=webdriver.Chrome()
driver.get('https://testpay.hongnaga.com/merchant.html')
# driver.get("https://pay.hongnaga.com/merchant/login")
# driver.get('https://cpay.hypayde.com/merchant')
# driver.get('http://47.75.86.174:8092/posa/merlogin.jsp')
driver.maximize_window()
driver.find_element_by_id("mch_id").clear()
driver.find_element_by_id("mch_id").send_keys(12001)
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys(123456)
# driver.find_element_by_id("password").send_keys("chilong123456")
driver.find_element_by_id("captcha").send_keys(0)
driver.find_element_by_id("sub").click()
time.sleep(10)

# element="error"
#
# for i in range(10):
#     if isElementExistid(element):
#         tishi=driver.find_element_by_id(element).text
#         print driver.find_element_by_id(element).text
#         # link_text="验证码错误"
#         if tishi==u"验证码错误":
#             driver.find_element_by_id("captcha_img").click()
#             driver.save_screenshot('D:\\code\\code.png')
#             id = driver.find_element_by_id("captcha_img")
#             # id=driver.find_element_by_id("randImage")
#             size = id.size
#             location = id.location
#             rangle = (int(location['x']), \
#                       int(location['y']), \
#                       int(location['x'] + size['width']), \
#                       int(location['y'] + size['height']))
#             img = Image.open('D:\\code\\code.png')
#             img = img.crop(rangle)
#             img = img.save('D:\\code\\code2.png')  # 裁剪验证码
#             time.sleep(1)
#             img = Image.open('D:\\code\\code2.png').convert('L')  # 二ZZZ值化
#             img = ImageEnhance.Contrast(img)  # 增强对比度
#             img = img.enhance(2.0)  # 增加饱和度
#             img.save('D:\\code\\code3.png')
#             time.sleep(2)
#             code = pytesseract.image_to_string(img)  # 使用image_to_string识别验证码
#             a = code.strip()
#             print a
#             driver.find_element_by_id("captcha").clear()
#             driver.find_element_by_id("captcha").send_keys(a)
#             driver.find_element_by_id("sub").click()
#             time.sleep(2)
#             element2="password"
#     else:
#         break
# print "success"
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# #登录网页
# driver.get("http://jdshop.shopjian.cn/public/admin/index/login?url=/public/admin/dashboard?ref=addtabs")
time.sleep(2)
driver.find_element_by_link_text("账户管理").click()
driver.find_element_by_xpath("//*[contains(@data-index,'6')]").click()
#切换到账户管理页面
frame_xpath=driver.find_element_by_xpath("//*[contains(@name,'iframe6')]")
driver.switch_to.frame(frame_xpath)
time.sleep(1)
zhgl=table.get_table(driver)
zhgl_table=zhgl.get_table_content("list")
# print zhgl_table[3][3]
for i in range(len(zhgl_table)):
    if zhgl_table[i][2]==zhgl_table[i][3]+zhgl_table[i][10]:#总金额=可用余额+手续费
        if zhgl_table[i][3]==zhgl_table[i][4]+zhgl_table[i][6]:#可用余额=可提现金额+待结算金额
            print"%s入金账户对账信息准确"%zhgl_table[i][1]




# #切换到iframe
# frame_xpath=driver.find_element_by_xpath("//iframe[contains(@src,'category')]")
# driver.switch_to.frame(frame_xpath)
#
# time.sleep(3)
# driver.find_element_by_class_name('btn-add').click()
# time.sleep(3)
# # 切换到添加页面
# add_path=driver.find_element_by_xpath("//iframe[contains(@src,'add?dialog')]")
# driver.switch_to.frame(add_path)
# driver.find_element_by_class_name('pull-left').click()
# time.sleep(3)
# ajfl=driver.find_elements_by_tag_name('li')#选择分类
# ajfl[2].click()
# driver.implicitly_wait(3)
# time.sleep(3)
# driver.find_element_by_id('c-name').send_keys("123")
# driver.implicitly_wait(3)
# driver.switch_to.parent_frame()
# driver.find_element_by_class_name('btn-embossed').click()
# time.sleep(3)
# # 获得table中的list
# table=driver.find_element_by_id("table")
# trs=table.find_elements_by_tag_name('tr')
# tr=trs.pop(-1).click()
# driver.implicitly_wait(3)
# tds=driver.find_elements_by_class_name('btn-delone')
# print tds
# driver.implicitly_wait(3)
# tds.pop(-1).click()
# # driver.switch_to.alert().accept()
# time.sleep(1)
# driver.find_element_by_class_name("layui-layer-btn0").click()#确定删除
# time.sleep(3)
#
# driver.switch_to.default_content()
# driver.find_element_by_xpath("//*[@href='/public/admin/goods/goods']").click()
# time.sleep(3)
#
# driver.find_element_by_xpath("//*[@placeholder='搜索菜单']").send_keys(u"管理")#
# time.sleep(3)
#
# driver.find_element_by_xpath("//*[@data-url='/public/admin/company/shoptable']").click()#隐藏参数
# time.sleep(3)
#
# driver.find_element_by_id("search-btn").click()
# zt=driver.find_element_by_xpath("//*[contains(@src,'shoptable?addtabs=1')]")
# driver.switch_to.frame(zt)
# driver.find_element_by_id("b.name").send_keys(u"台桌")
# driver.find_element_by_class_name("btn-success").click()
# time.sleep(2)
# # tr2=driver.find_elements_by_tag_name("tr")
# # tr2[2].click()
# td2=driver.find_elements_by_class_name("fa-pencil")
# td2[2].click()
# time.sleep(5)
# driver.switch_to.default_content()
#
#
#



