def my_func(num_1, num_2):
    """
    Возведение числа num_1 в степень num_2
    :param num_1: int
    :param num_2: int
    :return: float
    """
    return num_1 ** num_2

def my_func2(num_1, num_2):
    """
       Возведение числа num_1 в степень num_2
       :param num_1: int
       :param num_2: int
       :return: float
       """
    res = num_1
    abs_num_2 = abs(num_2)
    while abs_num_2 > 1:
        res *= num_1
        abs_num_2 -= 1
    return 1 / res

x = float(input("Введите число, которое нужно возвести в степень "))
y = float(input("Введите степень числа "))
print(my_func(x, y))
print(my_func2(x, y))

