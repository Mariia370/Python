class MyException(Exception):
    def __init__(self):
        self.sms = "It is not a number"


a = input("Print a number. If you want to stop, print 'stop'.\n")
my_list = []
while a != "stop":
    try:
        if a.isdigit():
            my_list.append(int(a))
        else:
            raise MyException
    except MyException as e:
        print(e.sms)
    a = input("Print a number. If you want to stop, print 'stop'.\n")

print(my_list)
