print("Введите строку")
str = input()

b=str.split(" ")
index = -1
indexSize = 0
for i in range(len(b)):
    size = len(b[i])
    if indexSize < size:
        indexSize = size
        index = i
    print(i)

print("Самое длинное слово: ", b[index])