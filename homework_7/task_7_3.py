class Cell:
    def __init__(self, numb_of_cells):
        self.numb_of_cells = int(numb_of_cells)

    def __add__(self, other):
        self.numb_of_cells += other.numb_of_cells

    def __sub__(self, other):
        if self.numb_of_cells - other.numb_of_cells > 0:
            self.numb_of_cells = self.numb_of_cells - other.numb_of_cells
        else:
            print("Number of inner cells in the first cell is less that in the second")

    def __mul__(self, other):
        self.numb_of_cells *= other.numb_of_cells

    def __truediv__(self, other):
        self.numb_of_cells = self.numb_of_cells // other.numb_of_cells

    def make_order(self, numb_of_row):
        result = ""
        numb_of_full_str = self.numb_of_cells // numb_of_row
        numb_of_rest_cells = self.numb_of_cells % numb_of_row
        return ("*" * numb_of_row + '\n') * numb_of_full_str + "*" * numb_of_rest_cells

my_cell = Cell(16)
print(my_cell.make_order(5))

