from functools import reduce

my_list = [el for el in range(100, 1001)]
sum_all = reduce(lambda a, b: a * b, my_list)
print(my_list)
print(sum_all)
