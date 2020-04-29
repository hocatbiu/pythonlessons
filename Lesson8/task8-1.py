#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.
class Anydate() :
    age = 25
    def __init__(self,dateinput):
        self.dateinput = dateinput
    @classmethod
    def changetoint(cls, dateinput):
        a = cls([int(el) for el in dateinput.split("-")])
        return a
    @staticmethod
    def validatedate(dateinput):

        if dateinput[0] >= 31 :
            a = "Указан невалидный день месяца"
        else:
            a = "День валидный"
        if dateinput[1] >= 12 :
            a = a + "\nУказан невалидный номер месяц"
        else:
            a = a + "\nМесяц валидный"
        if dateinput[2] < 0 or dateinput[2] >= 2020 :
            a = a + "\nУказан невалидный год"
        else:
            a = a + "\nГод валидный"
        return a
    def display(self):
        return self.dateinput
#v = input("Введите дату")
v = "30-14-2001"
date1 = Anydate.changetoint(v)
p = date1.display()
print(p)
print(date1.validatedate(p))
