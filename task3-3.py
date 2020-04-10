# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает
# сумму наибольших двух аргументов.

def sumtwoofmax(val1, val2, val3) :
    if val1 >= val2 :
        sum = val1
        if val2 >= val3 :
            sum = sum + val2
        else :
            sum = sum + val3
    else :
        sum = val2
        if val1 >= val3 :
            sum = sum + val1
        else :
            sum = sum + val3
    return sum

print(sumtwoofmax(int(input("Введите первое любое целое число")),
      int(input("Введите второе любое целое число")),
      int(input("Введите третье любое целое число"))))

