revenue = int(input("Введите сумму выручки вашей компании за предыдущей год:"))
expenses = int(input("Введите сумму издержек вашей компании за предыдущей год:"))
delta = revenue - expenses
if delta > 0 :
    print ("У вас прибыль в размере:", delta)
    profitability = delta / revenue
    print("Рентабельность вашей выручки", profitability)
    cntemployee = int(input("Введите количество сотрубников вашей компании:"))
    print("Прибыль фирмы в расчете на одного сотрудника", delta/cntemployee)
else :
    print("У вас убыток в размере:", delta)

