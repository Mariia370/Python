class Matrix:

    def __init__(self, my_list):
        eq_of_dim = True
        try:
            self.number_of_str = len(my_list)
            self.number_of_cul = len(my_list[0])
            for str in my_list:
                if len(str) != self.number_of_cul:
                    eq_of_dim = False
                    break
            if eq_of_dim:
                self.my_list = my_list
            else:
                raise TypeError

        except TypeError:
            print("Разное количетво элементов в строках")
        except Exception:
            print("Неверные входные данные")


    def __str__(self):
        result = ""
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                result += str(self.my_list[i][j])+" "
            result += '\n'
        return result


    def __add__(self, other):
        try:
            for i in range(len(self.my_list)):
                for j in range(len(self.my_list[i])):
                    self.my_list[i][j] = float(self.my_list[i][j]) + float(other.my_list[i][j])
            return self
        except Exception:
            print("Неверные входные данные")





new_matr_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(new_matr_1)

uncorrect_matr_1 = Matrix([[1, 2], [4, 5, 6], [7, 8, 9]])
#print(uncorrect_matr_1)
#uncorrect_matr_2 = Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9])

new_matr_2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(new_matr_1+new_matr_2)
