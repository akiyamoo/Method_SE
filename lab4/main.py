from zadaniya import lesson1_zadanie1, lesson1_zadanie2, lesson2_zadanie1, lesson2_zadanie2, lesson2_zadanie3, \
    lesson2_zadanie4, lesson2_zadanie5, lesson3_zadanie1, lesson3_zadanie2, lesson3_zadanie3, lesson3_zadanie4, \
    lesson4_zadanie1, lesson4_zadanie2, lesson4_zadanie3, lesson4_zadanie4

while True:
    lesson = int(input("Номер Lesson'a: "))
    if lesson == 1:
        print("В Lesson1 - 2 задания")
        zadanie = int(input("Введите номер задания: "))
        if zadanie == 1:
            lesson1_zadanie1()
        elif zadanie == 2:
            lesson1_zadanie2()
        else:
            print("Нет такого задания!")
    elif lesson == 2:
        print("В Lesson2 - 5 заданий")
        zadanie = int(input("Введите номер задания: "))
        if zadanie == 1:
            lesson2_zadanie1()
        elif zadanie == 2:
            lesson2_zadanie2()
        elif zadanie == 3:
            lesson2_zadanie3()
        elif zadanie == 4:
            lesson2_zadanie4()
        elif zadanie == 5:
            lesson2_zadanie5()
        else:
            print("Нет такого задания!")
    elif lesson == 3:
        print("В Lesson3 - 6 заданий")
        zadanie = int(input("Введите номер задания: "))
        if zadanie == 1:
            lesson3_zadanie1()
        elif zadanie == 2:
            lesson3_zadanie2()
        elif zadanie == 3:
            lesson3_zadanie3()
        elif zadanie == 4:
            lesson3_zadanie4()
        elif zadanie == 5:
            lesson2_zadanie5()
        elif zadanie == 6:
            lesson2_zadanie5()
        else:
            print("Нет такого задания!")
    elif lesson == 4:
        print("В Lesson4 - 4 заданий")
        zadanie = int(input("Введите номер задания: "))
        if zadanie == 1:
            lesson4_zadanie1()
        elif zadanie == 2:
            lesson4_zadanie2()
        elif zadanie == 3:
            lesson4_zadanie3()
        elif zadanie == 4:
            lesson4_zadanie4()
        else:
            print("Нет такого задания!")
    print("\n")