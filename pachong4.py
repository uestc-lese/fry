from lxml import etree
import requests
import os

if __name__ == '__main__':


    url = 'https://worldcosplay.net/member/Itsuki-chan/characters'
    html = requests.get(url)
    selecter = etree.HTML(html.text)
    tupian = []
    tu_pian_lian_jie_list_houduan = selecter.xpath('//*@herf')

for w in tu_pian_lian_jie_list_houduan:
    tu_pian_lian_jie_list = 'https://worldcosplay.net' + w
    tupian.append(tu_pian_lian_jie_list)
print(f">>>>>>{tupian}")
input(">>> ")


for url1 in tu_pian_lian_jie_list:#之后将每一个图片地址后的图片全部下载下来
    html1 = requests.get(url1)
    selecter1 = etree.HTML(html1.text)


    tu_pian_di_zhi_houduan = selector1.xpath('//*[@id="member"]/section/div/div/div[1]/ul/li/photo-thumbnail/div/a/@herf')


for tupian in tu_pian_di_zhi_houduan:
    url2 = 'https://worldcosplay.net' + str.join(tupian)
    html2 = requests.get(rul2)
    selector2 = etree.HTML(html2.text)
    tupian_url = selector2.xpath('//*[@id="photoContainer"]/div/div/img/@src')
    xz_tupian = request.get(tupian_url)
    with open(f'./{file_name}/' + tupian + '.jpg','wb') as tp:
         tp.write(xz_tupian.content)
