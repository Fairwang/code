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
import Queue
def cfs(im,x_fd,y_fd):
  # '''用队列和集合记录遍历过的像素坐标代替单纯递归以解决cfs访问过深问题
  # '''
  # print('**********')
  xaxis=[]
  yaxis=[]
  visited =set()
  q = Queue.Queue()
  q.put((x_fd, y_fd))
  visited.add((x_fd, y_fd))
  offsets=[(1, 0), (0, 1), (-1, 0), (0, -1)]#四邻域
  while not q.empty():
      x,y=q.get()
      for xoffset,yoffset in offsets:
          x_neighbor,y_neighbor = x+xoffset,y+yoffset
          if (x_neighbor,y_neighbor) in (visited):
              continue  # 已经访问过了
          visited.add((x_neighbor, y_neighbor))
          try:
              if im[x_neighbor, y_neighbor] == 0:
                  xaxis.append(x_neighbor)
                  yaxis.append(y_neighbor)
                  q.put((x_neighbor,y_neighbor))
          except IndexError:
              pass
  # print(xaxis)
  if (len(xaxis) == 0 | len(yaxis) == 0):
    xmax = x_fd + 1
    xmin = x_fd
    ymax = y_fd + 1
    ymin = y_fd
  else:
    xmax = max(xaxis)
    xmin = min(xaxis)
    ymax = max(yaxis)
    ymin = min(yaxis)
    #ymin,ymax=sort(yaxis)
  return ymax,ymin,xmax,xmin
def detectFgPix(im,xmax):
  # '''搜索区块起点
  # '''
  im = np.array(Image.open(im))

  h,w = im.shape[:2]
  for y_fd in range(xmax+1,w):
      for x_fd in range(h):
          if im[x_fd,y_fd] == 0:
              return x_fd,y_fd
def CFS(im):
  # '''切割字符位置
  # '''
  zoneL=[]#各区块长度L列表
  zoneWB=[]#各区块的X轴[起始，终点]列表
  zoneHB=[]#各区块的Y轴[起始，终点]列表
  xmax=0#上一区块结束黑点横坐标,这里是初始化
  for i in range(10):
      try:
          x_fd,y_fd = detectFgPix(im,xmax)
          # print(y_fd,x_fd)
          xmax,xmin,ymax,ymin=cfs(im,x_fd,y_fd)
          L = xmax - xmin
          H = ymax - ymin
          zoneL.append(L)
          zoneWB.append([xmin,xmax])
          zoneHB.append([ymin,ymax])
      except TypeError:
          return zoneL,zoneWB,zoneHB
  return zoneL,zoneWB,zoneHB
#####切割粘连字符代码：
def cutting_img(im,im_position,img,xoffset = 1,yoffset = 1):
  filename =  './out_img/'
  # 识别出的字符个数
  im_number = len(im_position[1])
  # 切割字符
  for i in range(im_number):
    im_start_X = im_position[1][i][0] - xoffset
    im_end_X = im_position[1][i][1] + xoffset
    im_start_Y = im_position[2][i][0] - yoffset
    im_end_Y = im_position[2][i][1] + yoffset
    cropped = im[im_start_Y:im_end_Y, im_start_X:im_end_X]
    cv2.imwrite(filename + '-cutting-' + str(i) + '.jpg',cropped)


#分割粘连字符代码：
# 切割的位置
ima="D:\\code\\code_fenge.png"
im_position = CFS(ima)
maxL = max(im_position[0])
minL = min(im_position[0])
# 如果有粘连字符，如果一个字符的长度过长就认为是粘连字符，并从中间进行切割
if(maxL > minL + minL * 0.7):
    maxL_index = im_position[0].index(maxL)
    minL_index = im_position[0].index(minL)
    # 设置字符的宽度
    im_position[0][maxL_index] = maxL // 2
    im_position[0].insert(maxL_index + 1, maxL // 2)
    # 设置字符X轴[起始，终点]位置
    im_position[1][maxL_index][1] = im_position[1][maxL_index][0] + maxL // 2
    im_position[1].insert(maxL_index + 1, [im_position[1][maxL_index][1] + 1, im_position[1][maxL_index][1] + 1 + maxL // 2])
    # 设置字符的Y轴[起始，终点]位置
    im_position[2].insert(maxL_index + 1, im_position[2][maxL_index])
# 切割字符，要想切得好就得配置参数，通常 1 or 2 就可以
cutting_img(ima,im_position,"111",1,1)



