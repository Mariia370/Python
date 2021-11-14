def division(num_1, num_2):
    """
    Деление числа num_1 на num_2
    :param num_1: float
    :param num_2: float
    :return: float
    """
    return num_1 / num_2


a = float(input("Введите делимое число "))
b = float(input("Введите делитель "))
if b == 0:
    print("На ноль делить нельзя!")
else:
    print(division(a, b))
