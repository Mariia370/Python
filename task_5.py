earnings = float(input("Введите значение выручки: "))
costs = float(input("Введите значение издержек: "))
if earnings > costs:
    print("Выручка больше издержек")
    print(f"Рентабельность выручки: {(earnings-costs) / earnings}")
    staff = int(input("Введите количество сотрудников: "))
    print(f"Величина прибыли в расчете на одного сотрудника: {(earnings-costs) / staff}")
elif earnings < costs:
    print("Выручка меньше издержек")
else:
    print("Выручка и издержки равны")
