my_list = ["HI!", [1, 2], 5, 1.3, (1, 2, 3), None, True, 0, False]

def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)
