from statistics import mean

with open("salary.txt", 'r') as f_obj:
    list_of_data = f_obj.readlines()
if len(list_of_data) > 0:

    str_data_of_file = [pers_data.split() for pers_data in list_of_data]
    names_with_salary = [(data[0], float(data[1])) for data in str_data_of_file]
    names_with_min_salary = [name for (name, salary) in names_with_salary if salary < 20000]
    print("Сотрудники с зарплатой, меньшей 20000: ")
    for name in names_with_min_salary:
        print(name)
    mean_salary = mean([salary for (name, salary) in names_with_salary])
    print("Средняя зароботная плата сотрудников:", mean_salary)
else:
    print("Пустой файл")
