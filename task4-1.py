#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv
script_name, counthours , salaryperhour, bonus = argv
def allsalary (arg1 , arg2, arg3) :
    return  int(arg1)*float(arg2) + int(arg3)
print(f"Ваша зарплата равна = {allsalary(counthours , salaryperhour, bonus)}")
