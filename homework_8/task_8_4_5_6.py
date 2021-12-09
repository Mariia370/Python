class MyException(Exception):
    def __init__(self):
        self.sms = "Incorrect type"


class Storage:
    __printers = []
    __scanners = []
    __copiers = []
    __printer_scanner_copier = []

    def __init__(self, equip):
        self.equip = equip

    @classmethod
    def sort_equipment(self, equipm):
        for i in equipm:
            if i.have_printer_funct:
                self.__printers.append(i)
            elif i.have_scanner_funct:
                self.__scanners.append(i)
            else:
                self.__copiers.append(i)

            for i in self.__printers:
                for j in self.__scanners:
                    for k in self.__copiers:
                        if i.name == j.name and i.name == k.name:
                            self.__printer_scanner_copier.append(Printer_Scaner_Copier(i, j, k))
                            self.__printers.remove(i)
                            self.__scanners.remove(j)
                            self.__copiers.remove(k)

        return f"Storage of printers: {self.__printers}\nStorage of scanners:{self.__scanners}\nStorage of copiers:{self.__copiers}\nStorage of multifunctional devices:{self.__printer_scanner_copier}"


class OfficeEquipment:
    def __init__(self, have_printer_funct, have_scanner_funct, have_copier_funct, name):
        self.have_printer_funct = have_printer_funct
        self.have_scanner_funct = have_scanner_funct
        self.have_copier_funct = have_copier_funct
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, name, speed_of_printing):
        super().__init__(True, False, False, name)
        try:
            if speed_of_printing.isdigit():
                self.speed_of_printing = speed_of_printing
            else:
                raise MyException
        except MyException as e:
            print(e.sms)

    def __repr__(self):
        return f"Printer {self.name}, speed {self.speed_of_printing}"

    @property
    def get_info(self):
        return self.speed_of_printing


class Scanner(OfficeEquipment):
    def __init__(self, name, format_of_paper):
        super().__init__(False, True, False, name)
        try:
            if format_of_paper[0] == 'a' and format_of_paper[1].isdigit():
                self.format_of_paper = format_of_paper
            else:
                raise MyException
        except MyException as e:
            print(e.sms)

    def __repr__(self):
        return f"Scanner {self.name}, format {self.format_of_paper}"

    @property
    def get_info(self):
        return self.format_of_paper


class Copier(OfficeEquipment):
    def __init__(self, name, colours):
        super().__init__(False, False, True, name)
        self.colours = colours

    def __repr__(self):
        return f"Copier {self.name}, colours: {self.colours}"

    @property
    def get_info(self):
        return self.colours


class Printer_Scaner_Copier(OfficeEquipment):
    def __init__(self, eq_1, eq_2, eq_3):
        list_pr = [eq_1.have_printer_funct, eq_2.have_printer_funct, eq_3.have_printer_funct]
        list_sc = [eq_1.have_scanner_funct, eq_2.have_scanner_funct, eq_3.have_scanner_funct]
        list_cop = [eq_1.have_copier_funct, eq_2.have_copier_funct, eq_3.have_copier_funct]
        super().__init__(max(list_pr), max(list_sc), max(list_cop), eq_1.name)
        self.info = [eq_1.get_info, eq_2.get_info, eq_3.get_info]

    def __repr__(self):
        return f"Printer-Scanner-Copier {self.name}, info: {self.info}"


pr_1 = Printer("Canon", "10")
sc_1 = Scanner("Canon", "a4")
cop_1 = Copier("Canon", "colourful")
pr_2 = Printer("Samsung", "15")
sc_2 = Scanner("HP", "a9")
cop_2 = Copier("Canon133", "colourful")
print(Storage.sort_equipment([pr_2, pr_1, sc_2, sc_1, cop_2, cop_1]))

