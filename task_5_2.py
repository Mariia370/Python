with open("new_file.txt", 'r') as file_obj:
    list_of_str = file_obj.readlines()
    print("Количество строк в файле: ", len(list_of_str))
    numb_of_words = [((i+1), len(words.split())) for (i, words) in enumerate(list_of_str)]
    for i, numb in numb_of_words:
        print(f"Количество слов в строке {i}: {numb}")
