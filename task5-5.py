#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


f = open("file_task5-5.txt", "w",encoding="utf-8")
f.write("1 2 3 4 5 6 7")
f.close()
f = open("file_task5-5.txt", "r",encoding="utf-8")
k = f.readline().split(" ")
sum = 0
for i in k :
    sum = sum + int(i)
print(sum)
f.close()