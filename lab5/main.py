from ex_1_class import Exercise
from ex_2_class import Exercise2

if 1 == int(input("Lesson 6. Select exercise (1 or 2): ")):
    print(Exercise(int(input("Введите x: "))))
else:
    print(Exercise2(int(input("Введите возраст: "))))