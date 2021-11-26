
my_dict = {"One": "Один", "Two":"Два", "Three":"Три", "Four": "Четыре", "Five": "Пять", "Six": "Шесть","Seven":"Семь","Eight":"Восемь", "Nine": "Девять"}

with open("numbers.txt", 'r') as f_obj_1, open("rus_numbers.txt", 'w') as f_obj_2:
    new_str = f_obj_1.readline()
    while new_str != "":
        words = new_str.split()
        f_obj_2.write(f"{my_dict.get(words[0])} {words[1]} {words[2]}\n")
        new_str = f_obj_1.readline()


