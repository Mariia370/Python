class MyComplex:
    def __init__(self, re, im):
        self.re = float(re)
        self.im = float(im)

    def __add__(self, other):
        return MyComplex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return MyComplex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __str__(self):
        if self.im != 0:
            if self.re != 0:
                if self.im > 0:
                    return f"{self.re}+{self.im}i"
                else:
                    return f"{self.re}{self.im}i"
            else:
                return f"{self.im}i"
        else:
            return f"{self.re}"


a_1 = MyComplex(0, 1)
a_2 = MyComplex(0, -1)
print(a_1 + a_2)
print(a_1 * a_2)
a_3 = MyComplex(2, 3)
a_4 = MyComplex(2, -3)
print(a_3 + a_2)
print(a_3 * a_4)
print(a_1 * a_4)
