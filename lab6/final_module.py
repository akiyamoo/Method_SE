from abstract_module import AbstractExercise
from def_module import Exercises_function


class FinalExercise(AbstractExercise, Exercises_function):
    age = None

    def __init__(self, x):
        self.x = x
        self.__condition()

    def __condition(self):
        if self.x == 1:
            n = int(input("Введите x: "))
            if 1 <= n <= 3:
                self.condition_1()
            elif 4 <= n <= 6:
                self.condition_2()
            elif 7 <= n <= 9:
                self.condition_3()
            else:
                print("Ошибка ввода")
        elif self.x == 2:
            self.age = int(input("Введите возраст: "))
            self.exercise2()
        else:
            print("Ошибка ввода")
