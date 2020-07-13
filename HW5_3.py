# -*- coding: utf8 -*-
my_f = open("fio.txt", "r")
content = my_f.readlines()
b = len(content)
print(f"{content}")
sal = []
my_f = open("fio.txt", "r")
for i in range(len(content)):
    content = my_f.readline()
    z = content.split()
    sal.append(int(z[1]))
    if int(z[1]) > 20000:
        print(f"Оклад больше 20000 рублей: {z[0]}")

sred = sum(sal)/b
print(f"Средний оклад работников {sred}")
my_f.close()