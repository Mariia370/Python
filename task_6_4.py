class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, new_speed):
        self.speed = new_speed
        return f"The car went with the speed {self.speed} km/h"

    def stop(self):
        return "The car stoped"

    def turn(self, direction):
        return f"The car turn to the {direction}"

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Speed exceeding: {(float(self.speed)) - 60} km/h"
        else:
            return  f"Speed: {self.speed} km/h"

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)



class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Speed exceeding: {(float(self.speed)) - 40} km/h"
        else:
            return f"Speed: {self.speed} km/h"


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


first_car = PoliceCar(60, "white", "lada")
print(first_car.speed)
print(first_car.is_police)
print(first_car.name)
print(first_car.turn("left"))
print(first_car.go(45))

second_car = Car(100, "black", "bmw", False)
print(second_car.show_speed())

third_car = TownCar(80, "green", "nissan", False)
print(third_car.color)
print(third_car.is_police)
print(third_car.show_speed())
print(third_car.go(40))
print(third_car.show_speed())


fouth_car = SportCar(80, "red", "audi")
print(fouth_car.show_speed())

fifth_car = WorkCar(60, "yellow", "volkswagen", False)
print(fifth_car.show_speed())
fifth_car.speed = 40
print(fifth_car.show_speed())

