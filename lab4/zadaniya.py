import random

import os.path, time
import os

from lesson_4_ex_1.first_condition import first_condition
from lesson_4_ex_1.fourth_condition import fourth_condition
from lesson_4_ex_1.second_condition import second_condition
from lesson_4_ex_1.third_condition import third_condition


def lesson1_zadanie1():
    x = int(input("Введите число от 1 до 9: "))
    if x >= 1 and x <= 3:
        s = input("Введите строку: ")
        n = int(input("Введите число повторов: "))
        for i in range(0, n, 1):
            print(s)
    elif x >= 4 and x <= 6:
        m = int(input("Введите степень: "))
        print(x, "^", m, " = ", pow(x, m))
    elif x >= 7 and x <= 9:
        for i in range(0, 10, 1):
            x = x + 1
            print(i + 1, "итерация - x =", x)
    else:
        print("Ошибка ввода!")


def lesson1_zadanie2():
    print("<-- Общество в начале XXI века -->")
    age = int(input("Введите ваш возраст: "))
    if age >= 0 and age < 7:
        print("Вам в детский сад")
    elif age >= 7 and age < 18:
        print("Вам в школу")
    elif age >= 18 and age < 25:
        print("Вам в профессиональное учебное заведение")
    elif age >= 25 and age < 60:
        print("Вам на работу")
    elif age >= 60 and age < 120:
        print("Вам предоставляется выбор")
    elif age < 0 or age >= 120:
        for i in range(0, 5, 1):
            print("Ошибка! Это программа для людей!")


def lesson2_zadanie1():
    str = input("Введите строку: ")
    strs = str.split()
    print(max(strs, key=len))


def lesson2_zadanie2():
    str = input("Введите строку: ")
    strs = str.split(";")
    print(max(strs, key=len))


def lesson2_zadanie3():
    str = input("Введите строку: ")
    seperator = input("Введите символ для разделения: ")
    strs = str.split(seperator)
    print(min(strs, key=len))


def lesson2_zadanie4():
    str_ = input("Введите строку: ")
    word = input("Введите слово, которое надо найти: ")
    strs = str_.split()
    count = 0
    for i in strs:
        if i == word:
            count = count + 1
    if count > 0:
        print("В тексте таких слов -", count)
    else:
        print("В тексте нет такого слова!")


def lesson2_zadanie5():
    str_ = input("Введите строку: ")
    strs = str_.split()
    print("Количество слов в строке -", len(strs))


def lesson3_zadanie1():
    number = [i for i in range(1, 9)]
    stepeni = [i for i in range(1, 10)]

    txt = """ dfghjk dfghjk fghjk fghjkl dfghj ertyui rtyu dfgbhjk """
    strings = [i for i in txt.split()]

    x = random.choice(number)
    print("Сгенерированное число x =", x)
    if x >= 1 and x <= 3:
        s = random.choice(strings)
        print("Сгенерированная строка s =", s)
        n = random.choice(number)
        print("Сгенерированное число повторов n =", n)
        for i in range(0, n, 1):
            print(s)
    elif x >= 4 and x <= 6:
        m = random.choice(stepeni)
        print("Сгенерированная степень m =", m)
        print(x, "^", m, " = ", pow(x, m))
    elif x >= 7 and x <= 9:
        for i in range(0, 10, 1):
            x = x + 1
            print(i + 1, "итерация - x =", x)
    else:
        print("Ошибка ввода!")


def lesson3_zadanie2():
    x = int(input("Введите число от 1 до 9: "))
    lesson3_zadanie2_check(x)


def lesson3_zadanie2_check(x):
    if x >= 1 and x <= 3:
        s = input("Введите строку: ")
        n = int(input("Введите число повторов: "))
        for i in range(0, n, 1):
            print(s)
    elif x >= 4 and x <= 6:
        m = int(input("Введите степень: "))
        print(x, "^", m, " = ", pow(x, m))
    elif x >= 7 and x <= 9:
        for i in range(0, 10, 1):
            x = x + 1
            print(i + 1, "итерация - x =", x)
    else:
        print("Ошибка ввода!")


def lesson3_zadanie3():
    str = input("Введите строку: ")
    strs = str.split()
    for i in strs:
        print(i, "-", len(i))


def lesson3_zadanie4():
    numbers = [i for i in range(1, 10)]
    x = int(input("Введите кол-во значений: "))
    nums = []
    for i in range(0, x, 1):
        n = random.choice(numbers)
        nums.append(n)

    print(nums)

    print(nums[0])
    for i in range(1, len(nums), 1):
        print(pow(nums[i], nums[i-1]))


def lesson4_zadanie1():
    x = int(input("Введите число от 1 до 9: "))
    first_condition(x)
    second_condition(x)
    third_condition(x)
    fourth_condition(x)


def lesson4_zadanie2():
    filename = input("Введите путь к файлу: ")
    if os.path.exists(filename):
        file_path = os.path.abspath(filename)
        file_stats = os.stat(file_path)
        print(f'Путь: {file_path}\n'
              f'Размер: {file_stats.st_size / (1024 * 1024)}')
        print("Последнее изменение: %s" % time.ctime(os.path.getmtime(file_path)))
        print("Дата создания: %s" % time.ctime(os.path.getctime(file_path)))
    else:
        print("Файл не существует")


def lesson4_zadanie3():
    answers = ['Да', 'Нет', ' Я согласен', 'Пойдет!', 'Нет проблем!', 'Меня зовут Рашид!',
               'Хорошо', 'Замечательно', 'Привет!', 'Не понял!']
    question = input('Задайте вопрос: ')
    ans = random.choice(answers)
    print(question, "-", ans)


def lesson4_zadanie4():
    txt = """ hello eldar qwerty app python """
    strings = [i for i in txt.split()]
    s = input("Введите слово: ")
    x = 0
    for i in strings:
        if i == s:
            x = x + 1
            i = i[::-1]
        print(i, end=" ")

    if x == 0:
        print("Нет такого слова в тексте!")

