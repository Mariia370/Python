def letter_to_upper(word):
    """
Превращение первой буквы слова в заглавную
    :param word: string
    :return: string
    """
    return word.capitalize()
res_string = ""
my_words = input("Введите слова через пробел ").split()
for elem in my_words:
    res_string += letter_to_upper(elem) + " "
print(res_string)
