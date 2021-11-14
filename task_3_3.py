def my_func(a, b, c):
    """
    Вывод суммы двух максимальных чисел
    :param a: float
    :param b: float
    :param c: float
    :return: float
    """
    return max(a + b, a + c, b + c)

my_str = input("Введите три числа через пробел ")
my_list = my_str.split()
print(my_func(float(my_list[0]), float(my_list[1]), float(my_list[2])))
