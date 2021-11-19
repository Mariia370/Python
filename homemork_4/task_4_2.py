
my_list = list(map(int, (input("Введите список целых чисел ").split())))
new_list = [elem for (i, elem) in enumerate(my_list) if elem > my_list[i - 1] and i > 0]
print(new_list)
