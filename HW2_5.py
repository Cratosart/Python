my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
while True:
        digit = int(input("Введите баллы рейтинга"))
        my_list.append(digit)
        my_list.sort(reverse=True)
        print(my_list)

