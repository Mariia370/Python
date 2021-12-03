with open("numbers_for_sum.txt", 'w+') as f_obj:
    f_obj.writelines([str(i*3)+" " for i in range(1, 100) if (i % 5) == 2])
    f_obj.seek(0)
    print(sum([int(n) for n in (f_obj.readline()).split()]))
