class Exercises_function:
    age = None

    def condition_1(self):
        print("Введите строку")
        self.s = input()
        print("Введите число повторений строки")
        self.n = int(input())
        for i in range(self.n):
            print("Строка = ", self.s)
            print("N = ", i)

    def condition_2(self):
        print("Введите степень числа")
        self.m = int(input())
        print(pow(self.x, self.m))

    def condition_3(self):
        for i in range(10):
            self.x += 1
            print("x = ", self.x)

    def exercise2(self):
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
