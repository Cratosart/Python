def my_fync(x, y):
    if y == 0:
        print("Делить на 0 не будем в этот раз бесконечност нам не нужна")
        return
    else:
        z = x / y
        print(f"Результат деления {z}")


my_fync(float(input("Введите х")), float(input("Введите у")))