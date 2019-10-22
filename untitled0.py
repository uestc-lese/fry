# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:09:54 2019

@author: 34281
"""
import os


file_name = input("> ")
folder_path = "C:\pachong" + file_name +"/"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)