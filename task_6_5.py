class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationary):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationary):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки карандашом")

class Handle(Stationary):

    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки маркером")

my_pen = Pen("Черная ручка")
my_pen.draw()

my_pencil = Pencil("Простой карандаш")
my_pencil.draw()

my_handle = Handle("Красный маркер")
my_handle.draw()

