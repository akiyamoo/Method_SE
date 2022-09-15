s = str(input("Введите строку: "))
symbol = input("Введите знак для поиска слов: ")

arr = s.split(" ")

index = -1
indexSize = 1000

for i in range(len(arr)):
    if arr[i].find(symbol) >= 0:
        if indexSize > len(arr[i]):
            indexSize = len(arr[i])
            index = i

if index != -1:
    print(arr[index])
else:
    print("Нет слова под этот критерий!")