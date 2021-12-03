with open("new_file.txt",'w') as file_obj:
    next_str = input("Вводите строки для записи в файл ")
    while next_str != '':
        file_obj.write(next_str + '\n')
        next_str = input()
