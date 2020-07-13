# -*- coding: utf-8 -*-
f = open("hw_2.txt", 'r')
content = f.readlines()
z = len(content)
print(f"Строк в файле {z} \n ")
f.close()

f = open('hw_2.txt', 'r')
i=0
for line in range(len(content)):
    content =f.readline()
    z = content.split()
    i +=1
    a = len(z)
    print(f"{a} Слов в {i} строке ")

