#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также
# словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджеры контекста.
import json
with open("file_task5-7.txt","r",encoding="utf-8") as f:
    avgprofit = 0
    i = 0
    company_dict = {None:None}
    for line in f :
        k = line.split(" ")
        profit = int(k[2]) - int(k[3])
        if profit > 0  :
            avgprofit = avgprofit + profit
            i = i + 1
        company = k[1] + " " +k[0]
        company_dict.update({company:profit})
    my_list = [company_dict,{"avgprofit" : avgprofit/i}]
    print(my_list)
with open ("file_task5-7j.json","w",encoding = "utf-8") as w:
    json.dump(my_list,w,ensure_ascii=False, indent = 4)
