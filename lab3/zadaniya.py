import random


def lesson1_ex1():
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


def lesson1_ex2():
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


def lesson2_ex1():
    str = input("Введите строку: ")
    strs = str.split()
    print(max(strs, key=len))


def lesson2_ex2():
    str = input("Введите строку: ")
    strs = str.split(";")
    print(max(strs, key=len))


def lesson2_ex3():
    str = input("Введите строку: ")
    seperator = input("Введите символ для разделения: ")
    strs = str.split(seperator)
    print(min(strs, key=len))


def lesson2_ex4():
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


def lesson2_ex5():
    str_ = input("Введите строку: ")
    strs = str_.split()
    print("Количество слов в строке -", len(strs))


def lesson3_ex1():
    number = [i for i in range(1, 9)]
    stepeni = [i for i in range(1, 10)]

    txt = """ haaskfas askdajdg adfdajfa akfa afkaskfaf """
    strings = [i for i in txt.split()]

    x = random.choice(number)
    print("x =", x)
    if x >= 1 and x <= 3:
        s = random.choice(strings)
        print("s =", s)
        n = random.choice(number)
        print("n =", n)
        for i in range(0, n, 1):
            print(s)
    elif x >= 4 and x <= 6:
        m = random.choice(stepeni)
        print("m =", m)
        print(x, "^", m, " = ", pow(x, m))
    elif x >= 7 and x <= 9:
        for i in range(0, 10, 1):
            x = x + 1
            print(i + 1, "x =", x)
    else:
        print("Ошибка ввода!")


def lesson3_ex2():
    x = int(input("Введите число от 1 до 9: "))
    lesson3_ex2_check(x)


def lesson3_ex2_check(x):
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
            print(i + 1, "x =", x)
    else:
        print("Ошибка ввода!")


def lesson3_ex3():
    str = input("Введите строку: ")
    strs = str.split()
    for i in strs:
        print(i, "-", len(i))


def lesson3_ex4():
    arr = input()  # takes the whole line of n numbers
    nums = list(map(int, arr.split(' ')))

    print(nums)

    print(nums[0])
    for i in range(1, len(nums), 1):
        print(pow(nums[i], nums[i-1]))