class MyDivZeroException(Exception):
    def __init__(self):
        self.str = "Division by zero is not possible"



def my_division(a, b):
    try:
        if(b != 0):
            return a/b
        else:
            raise MyDivZeroException()
    except MyDivZeroException as e:
        print(e.str)

print(my_division(25,4))
print(my_division(25,0))

