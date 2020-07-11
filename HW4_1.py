from sys import argv

def zp():
    num_1, num_2, num_3 = argv[1:]
    print(argv)
    return (int(num_1) * int(num_2) + int(num_3))

print(zp())
