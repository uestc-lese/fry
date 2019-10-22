from lxml import etree
import requests
import os

if __name__ == '__main__':

    #headers = {
    #'accept-ranges: bytes'
    #'cache-control: max-age=315360000'
    #'content-length: 7550'
    #'content-type: image/png'
    #'date: Fri, 18 Oct 2019 01:11:10 GMT'
    #'etag: "58f9d65f-1d7e"'
    #'expires: Thu, 31 Dec 2037 23:55:55 GMT'
    #'last-modified: Fri, 21 Apr 2017 09:52:31 GMT'
    #'server: nginx'
    #'status: 200'
    #             }
    url = 'https://worldcosplay.net/member/Itsuki-chan/characters'
    html = requests.get(url)
    selecter = etree.HTML(html.text)
    str = ""
    tu_pian_lian_jie_list_all = []
    tu_pian_ming_zi_list_all = []
    for x in range(1,42):
        tu_pian_lian_jie_list_houduan = selecter.xpath(f'//*[@id="member"]/section/div/ul/li[{x}]/div/div/a/@href')
        tu_pian_lian_jie_list = 'https://worldcosplay.net' + str.join(tu_pian_lian_jie_list_houduan)#为了保证网址完整（即去掉括号，去掉引号）
        tu_pian_lian_jie_list_all.append(tu_pian_lian_jie_list)#网址放入这个列表里
        tu_pian_ming_zi_list = selecter.xpath(f'//*[@id="member"]/section/div/ul/li[{x}]/div/div/a/div/text()')
        tu_pian_ming_zi_list_all.append(tu_pian_ming_zi_list)#同理将名字取爬下来
print(tu_pian_lian_jie_list_all)
print(tu_pian_ming_zi_list_all)
for (url1,file_name) in zip(tu_pian_lian_jie_list_all,tu_pian_ming_zi_list_all):

        html1 = requests.get(url1)
        selecter1 = etree.HTML(html1.text)#同理构造
        def mkdir(path):
            folder = os.path.exists(file_name)
            if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹，用爬下来的名字命名
                    os.makedirs(file_name)            #makedirs 创建文件时如果路径不存在会创建这个路径
                    print("---  new folder...  ---")
                    print( "---  OK  ---")

            else:
                    print ("---  There is this folder!  ---")

        tu_pian_di_zhi_houduan_list = []
        for m in range(1,30):
            tu_pian_di_zhi_houduan = selecter1.xpath(f'//*[@id="member"]/section/div/div/div[1]/ul/li[{m}]/photo-thumbnail/div/a/@herf')
            tu_pian_di_zhi_houduan_list.append(tu_pian_di_zhi_houduan)#同理构造出每个图片地址尾部

            for tupian in tu_pian_di_zhi_houduan_list:
                rul2 = 'https://worldcosplay.net'+ str.join(tupian)#构造出图片地址
                html2 = requests.get(rul2)
                selector2 = etree.HTML(html2.text)
                tupian_url = selector2.xpath('//*[@id="photoContainer"]/div[2]/div/img/@src')#得到图片地址
                print(tupian_url)
                #xz_tupian = requests.get(tupian_url,headers = headers)
                #with open(f'./{file_name}/' + tupian + '.jpg','wb') as tp:#二进制方式打开下载图片
                    #tp.write(xz_tupian.content)
                    #print("正在下载图片",tupian)
