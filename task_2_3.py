month = int(input("Введите номер месяца (целое число от 1 до 12) "))
seasons_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
print(seasons_list[month - 1])

seasons_dict = {i: seasons_list[i] for i in range(12)}
print(seasons_dict.get(month - 1))
