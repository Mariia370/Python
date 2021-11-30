from sqlite3 import Row


class Road:

    def __init__(self, length_km, width_km):
        self._length_km = length_km
        self._width_km = width_km
    def weight(self, height_cm, weight_of_unit_kg_m2 = 25):
        return self._length_km * self._width_km * weight_of_unit_kg_m2 * height_cm

new_road = Road(5000, 20)
print(new_road.weight(5))
