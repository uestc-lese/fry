# coding = utf -8

import re

with open("test1.txt", "r") as test1:
    word_list = []     # 存放所有单词，全部小写，并去除,.!等后缀，并去除空格字符串
    word_dict = {}     # 保留{word: count}键值对

    for line in test1.readlines():
        for word in line.strip().split(" "):
            word_list.append(re.sub(r"[.|!|,]", "", word.lower()))
            word_sets = list(set(word_list))   # 确保唯一

    word_dict = {word: word_list.count(word) for word in word_sets if word}
result = sorted(word_dict.items(), key=lambda d: d[1], reverse=True)[:10]
print(result)
