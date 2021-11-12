the_end = "да"
goods_list = []
i = 0
while the_end == "да":
    i += 1
    name = input("Введите название товара ")
    price = input("Введите цену товара ")
    amount = input("Введите количество товара ")
    units = input("Введите единицы измерения товара ")
    goods = (i, dict(название=name, цена=price, количество=amount, ед=units))
    goods_list.append(goods)
    the_end = input("Если хотите продолжить, введите 'да', если хотите завершить ввод товара, введите 'нет' ")
print(goods_list)
keys = list((goods_list[0])[1].keys())
#print(keys)
key_0 = set()
key_1 = set()
key_2 = set()
key_3 = set()
for number, dict_of_goods in goods_list:
    key_0.add(dict_of_goods.get(keys[0]))
    key_1.add(dict_of_goods.get(keys[1]))
    key_2.add(dict_of_goods.get(keys[2]))
    key_3.add(dict_of_goods.get(keys[3]))
analytics = {keys[0]: list(key_0), keys[1]: list(key_1), keys[2]: list(key_2), keys[3]: list(key_3)}
print(analytics)
