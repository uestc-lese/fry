# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:40:31 2019

@author: 34281
"""

   from selenium import webdriver
    import time
    open_driver = webdriver.Chrome()
    # open_driver = webdriver.Firefox()
    # open_driver = webdriver.PhantomJS()
    open_driver.get('https://www.baidu.com')
    time.sleep(5)
    open_driver.close()
