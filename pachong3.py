from bs4 import BeautifulSoup as bs

import re

import requests

     # 获取网页信息
        url = 'https://worldcosplay.net/member/Itsuki-chan/characters'         # print(url)
        header = { 'Upgrade-Insecure-Requests: 1'
                    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.21 Safari/537.36'  }    # F12 设置请求头

             res = requests.get(url, headers=header)
             html = res.text         # 提取图片链接
             soup = bs(html, features='lxml')
             img_ = soup.img
             url_img = img_.find_all('img', {'src': re.compile('.*?\.jpg')}) # 字典对应class属性关键词和正则提取代码
             for i in url_img:
                  print(i['src'])

        # 获取图片信息

        url_img = img_['src']   # 图片链接

        header1 = {}



         html = requests.get(url_img, headers=header1) # 图片信息
         # 下载图片
         name_img += 1
         with open('{}.jpg'.format(name_img), 'wb') as f:
              f.write(html.content)
      name_img += 100
