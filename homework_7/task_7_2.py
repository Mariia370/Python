from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def amount_of_fabric(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def amount_of_fabric(self):
        return float(self.size)/6.5 + 5

class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def amount_of_fabric(self):
        return float(self.height)*2 + 0.3


my_coat = Coat(42)
my_suit = Suit(170)

print(my_coat.amount_of_fabric)
print(my_suit.amount_of_fabric)

