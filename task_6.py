a = float(input("Введите результат пробежки спортсмена в первый день (км): "))
b = float(input("Введите цель спортсмена (км в день): "))
day = 1
if a >= b:
    print("Спортсмен уже достиг цели")
else:
    while a < b:
        day += 1
        add = 0.1 * a
        a += add
        #print(day, a)
    print(f"Спорсмен достигнет цели на {day} день")
