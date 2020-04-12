#3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
#Подсказка: использовать функцию range() и генератор.
#import random
#my_input_list = [random.randint(20,240) for el in range(1,10) ]
#print(f"Исходный список {my_input_list}")

my_output_list = [ i for i in range(20,241) if i % 20 == 0  or i % 21 == 0]
print(my_output_list)