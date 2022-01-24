import random as rm

numbers = [rm.randint(0, 100) for _ in range(0, 20)]
print(numbers)
counter = [i for i, elem in enumerate(numbers) if elem % 2 == 0]
print(counter)
