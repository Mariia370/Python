from builtins import super


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_total_income(self):
        total_income = float(self._income.get("wage"))+float(self._income.get("bonus"))
        return f"Total income of {self.name} {self.surname} is {total_income}"

new_position = Position("Ivan", "Petrov", "engineer", 20000, 5000)
print(new_position.get_full_name())
print(new_position.get_total_income())
