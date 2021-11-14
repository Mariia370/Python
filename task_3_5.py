def summ_of_list(list_of_numb):
    """
    Приведение типов элементов списка к числовому и суммирование элементов
    :param list_of_numb: list
    :return: float
    """
    return sum(list(map(float, list_of_numb)))

numbers = (input("Введите строку чисел, разделенных пробелом ")).split()
res_sum = summ_of_list(numbers)
print(res_sum)
flag = True


while flag:
    numbers = input("Продолжайте вводить числа. Закончить ввод чисел можно введением точки через пробел ").split()
    index = len(numbers)

    for i, elem in enumerate(numbers):
        if elem == '.':
            flag = False
            index = i
            break
    res_sum += summ_of_list(numbers[:index])
print(res_sum)



