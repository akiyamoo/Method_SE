from zadaniya import lesson1_ex1, lesson1_ex2, lesson2_ex1, lesson2_ex2, lesson2_ex3, lesson2_ex4, lesson2_ex5, lesson3_ex1, lesson3_ex2, lesson3_ex3, lesson3_ex4

lesson = int(input("Номер Lesson'a: "))
if lesson == 1:
    zadanie = int(input("Введите номер задания: "))
    if zadanie == 1:
        lesson1_ex1()
    elif zadanie == 2:
        lesson1_ex2()
    else:
        print("Нет такого задания!")
elif lesson == 2:
    zadanie = int(input("Введите номер задания: "))
    if zadanie == 1:
        lesson2_ex1()
    elif zadanie == 2:
        lesson2_ex2()
    elif zadanie == 3:
        lesson2_ex3()
    elif zadanie == 4:
        lesson2_ex4()
    elif zadanie == 5:
        lesson2_ex5()
    else:
        print("Нет такого задания!")
elif lesson == 3:
    zadanie = int(input("Введите номер задания: "))
    if zadanie == 1:
        lesson3_ex1()
    elif zadanie == 2:
        lesson3_ex2()
    elif zadanie == 3:
        lesson3_ex3()
    elif zadanie == 4:
        lesson3_ex4()
    else:
        print("Нет такого задания!")
