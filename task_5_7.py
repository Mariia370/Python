import json

with open("firms.txt", 'r') as f_obj:
    new_str = f_obj.readline()
    profits = dict()
    total_profit = 0
    number = 0
    while new_str != "":
        my_list = new_str.split()
        firm = my_list[0]
        proceeds = my_list[2]
        costs = my_list[3]
        profit = float(proceeds) - float(costs)
        profits[firm] = profit
        new_str = f_obj.readline()
        if profit >= 0:
            total_profit += float(profit)
            number += 1
    result = [profits, {'average_profit': total_profit / number}]
print(result)
with open('firms_output.json', 'w') as f_obj_2:
    json.dump(result, f_obj_2)
