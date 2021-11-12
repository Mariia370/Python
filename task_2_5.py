rating = [19, 12, 9, 5, 2]
the_end = "да"
while the_end == "да":
    new_digit = int(input("Введите натуральное число "))
    for i in range(len(rating)):
        if new_digit > rating[i]:
            rating.insert(i, new_digit)
#            print(rating)
            break
        if i == len(rating) - 1:
            rating.append(new_digit)
 #           print(rating)
    the_end = input("Если хотите продолжить, введите 'да', если хотите завершить ввод чисел, введите 'нет' ")
print(rating)
