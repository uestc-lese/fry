from collections import Counter
import re



with open('test1.txt', 'r') as test1,open('test2.txt', 'r') as test2:
    txt1 = test1.read()
    txt2 = test2.read()
a = Counter(re.split('\W+',txt1))  #取出每个单词出现的个数 \W匹配任何非单词字符 \w匹配包括下划线的任何单词字符
b = Counter(re.split('\W+',txt2))
ret1 = a.most_common(10)   #取出频率最高的前10个
ret2 = b.most_common(10)
print("test1单词前十:")
print(ret1)\n
print("test2单词前十:")
print(ret2)\n
