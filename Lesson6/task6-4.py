#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
# . А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car :
    def __init__(self,speed,color,name,is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self) :
        print(f"{self.name} start to go")
    def stop(self):
        print(f"{self.name} stop")
    def turn(self,direction):
        print(f"{self.name} change direction to {direction}")
    def showspeed(self):
        print(f"{self.name} speed is {self.speed}")
class TownCar(Car) :
    def showspeed(self):
        if self.speed >= 60 :
            print(f"{self.name} speed {self.speed} you over speed limit")
    pass
class SportCar(Car) :
    pass
class WorkCar(Car) :
    def showspeed(self):
        if self.speed >= 40:
            print(f"{self.name} speed {self.speed} you over speed limit")

class PoliceCar(Car) :
    pass

t1 = TownCar(70,"Green","Towncar",False)
s1 = SportCar(120,"Blue","Sportcar",False)
w1 = WorkCar(50,"Red","Workcar",False)
p1 = PoliceCar(0,"Black","Police",True)
print(f"Name {t1.name} your speed {t1.speed} and your color {t1.color} and Are you police? {t1.is_police}")
print(f"Name {s1.name} your speed {s1.speed} and your color {s1.color} and Are you police? {s1.is_police}")
print(f"Name {w1.name} your speed {w1.speed} and your color {w1.color} and Are you police? {w1.is_police}")
print(f"Name {p1.name} your speed {p1.speed} and your color {p1.color} and Are you police? {p1.is_police}")
t1.go()
t1.stop()
t1.turn("left")
t1.showspeed()

s1.go()
s1.stop()
s1.turn("left")
s1.showspeed()

w1.go()
w1.stop()
w1.turn("left")
w1.showspeed()

p1.go()
p1.stop()
p1.turn("left")
p1.showspeed()