#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
#относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

numofmonth = int(input("Введите номер месяца"))
seasons = [ "winter" for i in range(2)]
seasons.extend("spring" for b in range(3))
seasons.extend("summer" for b in range(3))
seasons.extend("autumn" for b in range(3))
seasons.append("winter")
print(seasons[numofmonth-1])

seasonsdict = {"winter":[12,1,2],"spring":[3,4,5],"summer":[6,7,8],"autumn":[9,10,11]}
for key, value in seasonsdict.items():
    for p in  seasonsdict.get(key):
        if  numofmonth == p:
            print (key)
            break
