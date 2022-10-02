class Exercise2:
    age = None

    def __init__(self, age):
        self.age = age
        self.exercise()

    def exercise(self):
        if 0 <= self.age <= 7:
            print("Вам в детский сад")
        elif 7 <= self.age <= 18:
            print("Вам в школу")
        elif 18 <= self.age <= 25:
            print("Вам в профессиональное учебное заведение")
        elif 25 <= self.age <= 60:
            print("Вам на работу")
        elif 60 <= self.age <= 120:
            print("Вам предоставляется выбор")
        else:
            print("Ошибка! Это программа для людей!")
