firstrun = float(input("Введите сколько километров вы планируете пробежать в первый день"))
totalkm = float(input("Введите общий результат в км , чтобы узнать на какой номер дня вы его достигнете"))
numberday = 1
while firstrun < totalkm:
    firstrun = firstrun + firstrun*0.1
    numberday = numberday +1
print(f"На {numberday} день вы пробежите {firstrun}")
