my_list = list(input("Введите любую фразу "))
print(my_list)
i = 0
while i + 1 < len(my_list):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    i += 2
print(my_list)
