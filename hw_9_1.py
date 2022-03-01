#1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
#Примечания:
#* в сумму не включаем пустую строку и строку целиком;
#* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.


import hashlib


def search_substr(s: str, sub: str) -> int:
    len_s = len(s)
    len_sub = len(sub)
    assert len_s > len_sub, "Подстрока должна быть строго меньше строки"
    assert len_s > 0 and len_sub > 0, "Строки не могут быть пустыми"
    count = 0

    hash_sub = hashlib.sha1(sub.encode('utf-8')).hexdigest()
    for i in range(len_s - len_sub + 1):
        if hash_sub == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            count += 1
    return count


s1 = input("Введите строку: ")
s2 = input("Введите подстроку для поиска: ")
print(f"Количестов строк {s2} в строке {s1}: {search_substr(s1, s2)}")
