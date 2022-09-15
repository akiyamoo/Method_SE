s = str(input("Введите строку: "))
symbol = input("Введите слово для поиска: ")

arr = s.split(" ")

index = -1
indexSize = 1000

for i in range(len(arr)):
    if arr[i].find(symbol) >= 0:
        if indexSize > len(arr[i]):
            indexSize = len(arr[i])
            index = i
            break

if index != -1:
    print("Слово №" + str(index + 1))
else:
    print("Нет слова под этот критерий!")