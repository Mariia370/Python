def sum_of_numb(my_str):
    cur_str = ""
    cur_numb = 0
    i = 0
    if len(my_str) == 0:
        return 0
    else:
        while my_str[i].isdigit():
            cur_str += my_str[i]
            i += 1
        if cur_str != "":
            cur_numb = int(cur_str)
        return cur_numb + sum_of_numb(my_str[i+1:])


with open("subjects.txt", 'r', encoding='utf-8') as f_obj:
    new_str = f_obj.readline()
    result = dict()
    while new_str != "":
        subj, classes = new_str.split(':')
        #classes = ''.join(classes.split())
        result[subj] = sum_of_numb(classes)
        new_str = f_obj.readline()
print(result)
