import time, itertools


class TrafficLight:
    __time_intervals = [7, 2, 4]
    __list_of_colours = ["red", "yellow", "green"]

    def __init__(self):
        self.__color = "red"

    def running(self):
        count = 0
        for i in itertools.cycle([1, 2, 0]):
            print(self.__color)
            count += 1
            time.sleep(self.__time_intervals[i])
            self.__color = TrafficLight.__list_of_colours[i]
            if count > 5:
                break


tr_ligth = TrafficLight()
tr_ligth.running()
