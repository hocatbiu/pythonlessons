#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл
l1 = ""
with open("file_task5-4.txt", "r",encoding="utf-8") as f:
    for i in f :
        k = i
        l = k.replace('One','Один')
        if l != k :
            l1 = l1 + l
        l = k.replace('Two', 'Два')
        if l != k :
            l1 = l1 + l
        l = k.replace('Three', 'Три')
        if l != k :
            l1 = l1 + l
        l = k.replace('Four', 'Четыре')
        if l != k :
            l1 = l1 + l
        print(l1)
f = open("file_task5-4.txt", "w",encoding="utf-8")
f.writelines(l1)
f.close()