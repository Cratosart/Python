def my_func(arg_1, arg_2):
    return arg_1 ** arg_2


print(my_func(2, -3))


def cirk(x, y):
    i = -1
    z = x
    while i != y:
        x = z * x
        i -= 1
    x = 1/x
    print(f"{x}")

print(cirk(2, -3))
