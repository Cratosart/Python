f_1 = open("my_file.txt", "w")
while True:
    x = input("Введите текст")
    if x != "":
        f_1.write(f"{x} \n")
    else:
        f_1.close()
        break
