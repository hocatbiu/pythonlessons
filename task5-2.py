# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.
f = open("file_task5-2.txt", "r",encoding="utf-8")
i = 0
allstring = f.readlines()
print(f"Всего строк в файле {len(allstring)}")
for i in allstring :
    print(f" Строка {i} содержит  {len(i.split(' '))} слов")
f.close()