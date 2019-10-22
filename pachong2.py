import requests

import os

from lxml import etree

from threading import *

from time import sleep

nMaxThread = 2  #这里设置需要开启几条线程，我笔记本不太行只能2核

ThreadLock = BoundedSemaphore(nMaxThread)

 gHeads = {    "",}
 class Meizitu(Thread):
     def __init__(self,mainReferer,url,title):
         Thread.__init__(self)
         self.MainReferer = mainReferer
         self.url = url
         self.title = title[3:-4]  #这里是为了把<b></b>给删除

     def run(self):
         try:
             urlList = self.GetPhotoUrl()
             if len(urlList) > 0 and urlList != None:
                 self.SavePath(urlList)

         finally:
             ThreadLock.release()
             def GetPhotoUrl(self):
                 heads={
                   "Referer":self.MainReferer
                        }
                 heads.update(gHeads)
                 html = requests.get(self.url,headers=heads)
                 if html.status_code == 200:
                      xmlContent = etree.HTML(html.text)
                      urlList = xmlContent.xpath("//div[@id='picture']/p/img/@src")
                      return urlList
                      else:
                          return None

def main():
    while True:
        try:
             nNum = int(raw_input("请输入要下载几页: "))
             if nNum>0:
                 break
            except ValueError:
                     print("请输入数字。")
                     continue
    for i in range(nNum):
        url = "http://www.meizitu.com/a/more_%d.html"%(i+1)
        html = requests.get(url,headers=gHeads)
        if html.status_code == 200:
            xmlContent = etree.HTML(html.content)
            hrefList = xmlContent.xpath("//div[@class='pic']/a/@href")
            titleList = xmlContent.xpath("//div[@class='pic']/a/img/@alt")
            for i in range(len(hrefList)):
                ThreadLock.acquire()
                t = Meizitu(url,hrefList[i],titleList[i])
                t.start()

if __name__ == '__main__':
     main()
