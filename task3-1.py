# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def zerodiv(numerator1, denumerator1):
    try:
        itogo = numerator1 / denumerator1
    except ZeroDivisionError:
        return "На 0 делить нельзя"
    return itogo


print(zerodiv(int(input("Числитель")), int(input("Знаменатель"))))
