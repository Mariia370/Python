numb_1 = 100
numb_2 = 256
print(numb_1 + numb_2)
print(numb_2 // numb_1)
print(numb_2 % numb_1)
print(numb_1 / numb_2)
print(str(numb_1) + str(numb_2))
numb_3 = float(input("Введите число "))
if (numb_3 % 1) == 0:
    if numb_3 > 0:
        print("Вы ввели натуральное число")
    else:
        print("Вы ввели целое число")
else:
    print("Введеное число не является ни целым, ни натуральным")
