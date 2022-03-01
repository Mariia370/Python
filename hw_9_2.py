# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, namedtuple
import queue,time
def get_codes(the_head, my_dict, new_code):
    if the_head.value is not None:
        my_dict[the_head.value] = new_code
    else:
        get_codes(the_head.left, my_dict, new_code + "0")
        get_codes(the_head.right, my_dict, new_code + "1")
    return my_dict


def Huffman(s):
    frequencies = Counter(s)
    MyNode = namedtuple('MyNode', 'left, right, value')
    my_queue = queue.PriorityQueue(len(s))
    for i in frequencies:
        my_queue.put((frequencies[i], time.time(),  MyNode(None, None, i)))
        time.sleep(0.1)


    while not my_queue.empty():
        (index_1, t, left_node) = my_queue.get()
        print(index_1)
        print(left_node)
        if my_queue.empty():
            print("empty")
            break
        else:
            (index_2, t, right_node) = my_queue.get()
            print(index_2)
            print(right_node)
            my_queue.put((index_1 + index_2, time.time(), MyNode(left_node, right_node, None)))
            time.sleep(0.1)
    return get_codes(left_node, dict(), "")


s = input("Введите строку для кодирования: ")
print(Huffman(s))
