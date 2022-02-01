from collections import defaultdict, namedtuple
Data_of_Factory = namedtuple('Data_of_Factory', 'profit, sum_pr')
factories = defaultdict(Data_of_Factory)
i = int(input("Введите количество предприятий: "))
while i > 0:
    name = input(f"Введите название предприятия: ")
    profits = list(map(int, input("Введите через пробел прибыль предприятий за каждый квартал года: ").split()))
    factories[name] = Data_of_Factory(profits, sum(profits) )
    i -= 1

print(factories)
s = 0
for k in factories:
    s += sum(factories[k].profit)
s /= len(factories)
print(f"Средняя прибыль за год среди предприятий: {s}")
for k in factories:
    if factories[k].sum_pr > s:
        print(f"Предприятие, прибыль которого выше среднего: {k}")
    elif factories[k].sum_pr < s:
        print(f"Предприятие, прибыль которого ниже среднего: {k}")




