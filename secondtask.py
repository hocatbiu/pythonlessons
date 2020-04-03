seconds = int(input("Введите время в секундах: "))
hours = seconds // 3600
if hours < 10:
    hoursstr = '0' + str(hours)
else:
    hoursstr = str(hours)
minutes = (seconds - hours*3600)//60
if minutes < 10:
    minutesstr = '0' + str(minutes)
else:
    minutesstr = str(minutes)
seconds2 = seconds - hours*3600 - minutes*60
if seconds2 < 10:
    secondsstr = '0' + str(seconds2)
else:
    secondsstr = str(seconds2)
print(f"{hoursstr}:{minutesstr}:{secondsstr}")