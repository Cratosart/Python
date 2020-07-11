my_mass = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
n_mass = [i for num, i in enumerate(my_mass) if my_mass[num] > my_mass[num-1]]

print(n_mass)

