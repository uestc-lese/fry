from collections import Counter#相当于一种计数器
import re #re模块,正则表达式。。。
print("请输入要统计文本1")
wtf1=input("> ")
print("请输入要统计文本2")
wtf2=input("> ")

with open(wtf1, 'r') as test1,open(wtf2, 'r') as test2:#从文件中读取数据，然后关闭文件句柄,说白了就是包括打开文件和关闭文件，方便一点
    txt1 = test1.read()
    txt2 = test2.read()
a = Counter(re.split('\W+',txt1)) #取出每个单词出现的个数 \W匹配任何非单词字符 \w匹配包括下划线的任何单词字符 ps:"+" 用于取消空格，否则会统计空格
b = Counter(re.split('\W+',txt2))
ret1 = a.most_common(10)   #取出频率最高的前10个
ret2 = b.most_common(10)
print(f'{wtf1}出现次数:')
for i,m in zip(ret1,range(1,11)):#必须用zip将后面两个打包不然运行不了,要报错
    print(f"序号{m}:")
    print(i)
print("----------------\n")
print(f"{wtf2}出现次数：")
for f,m in zip(ret2,range(1,11)):
    print(f"序号{m}:")
    print(f)
