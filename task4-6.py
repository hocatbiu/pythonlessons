# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle

my_input_list = input("Введите целое число и любую строку через пробел").split()
print(my_input_list)
#my_output_list = (el + el1  for el in count(int(my_list.[1])) )

for el  in count(int(my_input_list[0])) :

    if el > int(my_input_list[0]) * 12:
        break
    else:
       print(el)
c = 0
for el in cycle(my_input_list[1]) :
    if c > 12 :
        break
    print (el)
    c += 1
