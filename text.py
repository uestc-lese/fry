from lxml import etree
import requests

headers = {
          'Referer: https://worldcosplay.net/member/Itsuki-chan/characters/73943'
          'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.21 Safari/537.36'
          }

url = 'https://worldcosplay.net/member/Itsuki-chan/characters/73943'
html = requests.get(url，headers = headers)
selecter = etree.HTML(html.text)#同理构造
#tu_pian_di_zhi_list = []
tu_pian_di_zhi_houduan_list = selecter.xpath('//photo-thumbnail/div/a/@href')
#tu_pian_di_zhi_list.append(tu_pian_di_zhi)#同理构造出每个图片地址
print(tu_pian_di_zhi_houduan_list)
#print(tu_pian_di_zhi_list)

#url = 'https://worldcosplay.net/member/Itsuki-chan/characters'
#html = requests.get(url)
#selecter = etree.HTML(html.text)
#tu_pian_lian_jie_list_all = []
#tu_pian_lian_jie_list_houduan_list = selecter.xpath('//*[@id="member"]/section/div/ul/li/div/div/a/@href')
#for tu_pian_lian_jie_list_houduan in tu_pian_lian_jie_list_houduan_list:
    #tu_pian_lian_jie_list = 'https://worldcosplay.net/' + tu_pian_lian_jie_list_houduan
    #tu_pian_lian_jie_list_all.append(tu_pian_lian_jie_list)
