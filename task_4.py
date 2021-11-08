number = input("Введите натуральное число: ")
i=1
digit = int(number[0])
while i < len(number):
        if (int(number[i])) > digit:
            digit = int(number[i])
        i += 1
print(f"Самая большая цифра - {digit}")
