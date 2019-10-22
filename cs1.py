# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:40:31 2019

@author: 34281
"""

from lxml import etree
import requests
from selenium import webdriver#运行该程序需要用到chrome，chromedriver，selenium
import os


headers = {        
          'Sec-Fetch-User': '?1',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.21 Safari/537.36'}
url = 'https://worldcosplay.net/member/Itsuki-chan/characters'
html = requests.get(url)
selecter = etree.HTML(html.text)
tu_pian_lian_jie_list_all = []
tu_pian_lian_jie_list_houduan_list = selecter.xpath('//*[@id="member"]/section/div/ul/li/div/div/a/@href')
for tu_pian_lian_jie_list_houduan in tu_pian_lian_jie_list_houduan_list:
    tu_pian_lian_jie_list = 'https://worldcosplay.net' + tu_pian_lian_jie_list_houduan
    tu_pian_lian_jie_list_all.append(tu_pian_lian_jie_list)#网址放入这个列表里
    
    
tu_pian_ming_zi_list = selecter.xpath('//*[@id="member"]/section/div/ul/li/div/div/a/div/text()')
#同理将名字取爬下来
#print(tu_pian_lian_jie_list_all)
#print(tu_pian_ming_zi_list)

for file_name in tu_pian_ming_zi_list:
    
    folder_path = "C:/pachong/" + str(file_name) +"/"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)