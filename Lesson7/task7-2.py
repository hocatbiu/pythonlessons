#2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC , abstractmethod
class Clothes(ABC) :

    def __init__(self,title):
        self.title = title

    @abstractmethod

    def clothspend(self):
        pass

class Coat(Clothes) :
    def __init__(self,title,size):
        super().__init__(title)
        self.v = int(size)

    @property
    def clothspend(self):
        return f"Размер {self.title} {self.v / 6.5 + 0.5}"

class Suit(Clothes) :
    def __init__(self, title,height):
        super().__init__(title)
        self.h = height

    @property
    def clothspend(self):
        return f"Размер {self.title} {2 * self.h + 0.3}"

a1 = Coat("Coat",10)
print(a1.clothspend)


a2 = Suit("Suit",10)
print(a2.clothspend)
