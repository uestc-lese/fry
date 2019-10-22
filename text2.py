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

for (url1,file_name) in zip(tu_pian_lian_jie_list_all,tu_pian_ming_zi_list):
    folder_path = "C:/pachong/" + file_name +"/"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    print("正在提取该网址",url1)#已提取网址
    open_driver = webdriver.Chrome(executable_path = 'C:\\Users\\34281\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')#不同的人电脑不一样请找到自己的那个chrome地址
    html = requests.get(url1)
    open_driver.get(url1)
    html = open_driver.page_source
    source =  etree.HTML(html)
    tu_pian_di_zhi_houduan_list = source.xpath('//*[@id="member"]/section/div/div/div[1]/ul/li/photo-thumbnail/div/a/@href')      
    open_driver.close()
#取出了一个角色的所有照片
    tu_pian_di_zhi_list = []
    for tu_pian_di_zhi_houduan in tu_pian_di_zhi_houduan_list:
        print(tu_pian_di_zhi_houduan)#已提取出的内容
        tu_pian_di_zhi = 'https://worldcosplay.net' +  str(tu_pian_di_zhi_houduan)
        tu_pian_di_zhi_list.append(tu_pian_di_zhi)
        #同理构造出一个角色的每个图片地址
#print(tu_pian_di_zhi_list)
        i = 0
    for url2 in tu_pian_di_zhi_list:
        html2 = requests.get(url2)
        selector2 = etree.HTML(html2.text)
        tupian_url = selector2.xpath('//*[@id="photoContainer"]/div/div/img/@src')
        #print(tupian_url)
        #构造出一个角色所有照片###下载###地址
        for xzurl in tupian_url:
            i = i + 1
            xz_tupian = requests.get(xzurl)
            print("正在下载图片",i)
            open( f'C:/pachong/{file_name}/' + str(i) + '.jpg','wb').write(xz_tupian.content)#二进制方式打开下载图片
            print("下载完成",i)