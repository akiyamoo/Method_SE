x = int(input("Введите возраст: "))

if 4 < x < 21:
    print(str(x) + " лет")
elif x % 10 == 1:
    print(str(x) + " год")
elif 1 < x % 10 < 5:
    print(str(x) + " года")
else:
    print(str(x) + " лет")