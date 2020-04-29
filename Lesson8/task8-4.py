# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В
# классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь

class Device():
    def __init__(self, id, title, model, color):
        self.id = id
        self.title = title
        self.model = model
        self.color = color

class CheckType(Exception) :
    def __init__(self,txt):
        self.txt = txt
class WareHouse():
    def __init__(self):

        self.wd = {}
        self.wd2 = {}

    def putin(self, title):
        if self.wd.get(title) is not None:
            self.wd.update({title: self.wd.get(title) + 1})
        else:
            self.wd.update({title: 1})
        print(f"На главном складе всего {self.wd}")

    def putout(self, title, wd):
        if wd.get(title) is not None and wd.get(title) > 0 and self.wd2.get(title) is not None:
            self.wd2.update({title: self.wd2.get(title) + 1})
            wd.update({title: wd.get(title) - 1})
            print(f"Осталось на главном складе {wd}")
            print(f"Поступило на склад подразделения {self.wd2}")
        else:
            if wd.get(title) is not None and wd.get(title) > 0 and self.wd2.get(title) is None:
                self.wd2.update({title: 1})
                wd.update({title: wd.get(title) - 1})
                print(f"Осталось на главном складе {wd}")
                print(f"Поступило на склад подразделения {self.wd2}")
            else:
                print(f"Оборудования нет на главном складе")


class Printer(Device):
    def __init__(self, id, title, model, color, speedprinting, typeofprint, supportformat):
        super().__init__(id, title, model, color)
        self.speedprinting = speedprinting
        self.typeofprint = typeofprint
        self.supportformat = supportformat
        self.my_dict = {
            self.id: [self.title, self.model, self.color, self.speedprinting, self.typeofprint, self.supportformat]}


class Xerox(Device):
    def __init__(self, id, title, model, color, speedcopy, supportformat):
        super().__init__(id, title, model, color)
        self.speedcopy = speedcopy
        self.supportformat = supportformat
        self.my_dict = {self.id: [self.title, self.model, self.color, self.speedcopy, self.supportformat]}


class Scanner(Device):
    def __init__(self, id, title, model, color, countryofproducing, supportformat):
        super().__init__(id, title, model, color)
        self.countryofproducing = countryofproducing
        self.supportformat = supportformat
        self.my_dict = {self.id: [self.title, self.model, self.color, self.countryofproducing, self.supportformat]}

    def printall(self):
        print(f"{self.my_dict}")



d = Scanner(1, "Scanner", "HP", "Gray", "Russia", ["A1", "A2"])
d1 = Scanner(2, "Scanner", "Xerox", "Gray", "Russia", ["A1", "A2"])
d2 = Scanner(3, "Scanner", "Huawie", "Green", "Russia", ["A2"])
w = WareHouse()
w2 = WareHouse()
m2 = WareHouse.putin(w, d.title)
m2 = WareHouse.putin(w, d1.title)
m2 = WareHouse.putin(w, d2.title)


my_list = []
v = input("Сколько сканнеров переместить на склад подразделения")
k = 0
for el in v :
    if ord(el) < 48 or ord(el) > 57 :
        k += 1
if k > 0 :
    try :
        raise CheckType("Вы ввели не число")
    except CheckType as err:
        print(f"{err}")
else :
    print ("Вы ввели число")
    my_list.append(int(v))

for i in range(0,int(v)) :
    m2 = WareHouse.putout(w2, d1.title, w.wd)
#print(d.my_dict)
