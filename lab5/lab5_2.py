"""
Напишите программу, которая выводит «ENG» при условии,
что пользователь вводит с клавиатуры пароль «qwerty»,
и выводит «РУС» при условии,что пользователь вводит с клавиатуры «йцукен».
"""

import re

def func(passw):
    return bool(re.search('[а-яА-Я]', passw))

def main():
    try:
        passw = input("Введите пароль: ")
        if passw == '':
            raise TypeError
        if passw.isdigit():
            raise Exception
        if func(passw):
            print("РУС")
        else:
            print("ENG")
    except (ValueError, TypeError):
        print("Некорректные данные!")
    except Exception:
        print("Пароль не должен содержать цифры!")

if __name__ == "__main__":
    main()
