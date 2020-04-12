#2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента. Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка
# использовать генератор.
import random
my_input_list = [random.randint(0,100) for el in range(1,10) ]
print(f"Исходный список {my_input_list}")
my_output_list = [my_input_list[i+1] for i in  range(0,len(my_input_list)-1) if my_input_list[i+1]>my_input_list[i] ]
print(f"Итоговый список {my_output_list}")


