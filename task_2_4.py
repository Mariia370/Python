my_str = input("Введите слова через пробел ")
words = my_str.split()
for elem in words:
    print(f"{words.index(elem) + 1}. {elem[:10]}")
