p = int(input("Введите любое целое положительное число: "))
max = p % 10
while p !=0:
    p = p // 10
    d2 = p % 10
    if max > d2:
        max = max
    else:
        max = d2
print ("Максимальное цифра в числе:",max)