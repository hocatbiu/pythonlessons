# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def useroutput(phonenumber, birthday, city, email, name, secondname):
    return print(f"Ваше имя {name}, Ваша фамилия {secondname}, "
                 f"Вы проживаете {city}, Вы родились {birthday}, Ваш телефон {phonenumber},Ваш email {email}")


useroutput(name=input("Введите Ваше имя"),
           secondname=input("Введите Вашу фамилию"),
           city=input("Введите Ваш город проживания"),
           birthday=input("Введите Вашу дату рождения"),
           email=input("Введите Ваш email"),
           phonenumber=input("Введите Ваш номер телефона"))
