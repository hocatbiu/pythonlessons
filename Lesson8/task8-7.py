#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав
# экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте
# корректность полученного результата.


class ComplexDigit():
    def __init__(self,complexdigit1,complexdigit2):
        self.complexdigit1 = complexdigit1
        self.complexdigit2 = complexdigit2
    def __add__(self, other):
        return ComplexDigit(self.complexdigit1 + other.complexdigit1
                            , self.complexdigit2  +  other.complexdigit2)

    def __mul__(self, other):
        return ComplexDigit(self.complexdigit1 * other.complexdigit1 - self.complexdigit2 * other.complexdigit2
                            ,self.complexdigit1 * other.complexdigit2 + self.complexdigit2 * other.complexdigit1)
    def __str__(self):
        return f"{self.complexdigit1} + {self.complexdigit2}i "


v = input("Введите комплексное число")
v = v.replace(" ","")
a1 = int(v[0:v.index("+")])
a2 = int(v[v.index("+")+1:v.index("i")])
cd1 = ComplexDigit(a1,a2)
v = input("Введите 2 комплексное число")
v = v.replace(" ","")
a1 = int(v[0:v.index("+")])
a2 = int(v[v.index("+")+1:v.index("i")])
cd2 = ComplexDigit(a1,a2)
cd3 = cd1+cd2
print(cd3)
print(cd1*cd2)
