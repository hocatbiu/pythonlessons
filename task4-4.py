# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив
# чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения
# задания обязательно использовать генератор.

import random

my_input_list = [random.randint(0, 100) for el in range(1, 30)]
print(f"Исходный список {my_input_list}")

my_output_list = [my_input_list[i]
                  for i in range(0, len(my_input_list)) if my_input_list.count(my_input_list[i]) == 1
                  ]

print(f"Итоговый список {my_output_list}")
