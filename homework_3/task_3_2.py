def personal_data(f_name, l_name, year, city, email, phone):
    """
    Вывод данных о пользователе в одну строку
    :param f_name: string
    :param l_name: string
    :param year: string
    :param city: string
    :param email: string
    :param phone: string
    :return: string
    """
    return f"Имя: {f_name}, Фамилия: {l_name}, Год рождения: {year}, Город проживания: {city}, e-mail: {email}, Номер телефона: {phone}"

first_name = input("Введите имя ")
last_name = input("Введите фамилию ")
year_of_birth= input("Введите год рождения ")
city_of_residence = input("Введите город проживания ")
email_address = input("Введите e-mail ")
phone_number = input("Введите номер телефона ")
print(personal_data(email=email_address, year=year_of_birth, city=city_of_residence, l_name=last_name, phone=phone_number, f_name=first_name))
