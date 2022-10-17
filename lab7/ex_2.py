# import pandas as pd   #  pip install pandas
#
# columns=['x', 's', 'n', 'm']
#
# data = [
# ['1', 'Hello Eldar', '1', '4'],
# ['3', 'Hello Eldar', '2', '4'],
# ['5', 'Hello Eldar', '3', '4'],
# ['8', 'Hello Eldar', '4', '4']
# ]
#
# df = pd.DataFrame(data, columns=columns)
# df.to_csv('./cartridge_accounting.csv')

import pandas as pd

data = pd.read_csv('/cartridge_accounting.csv')

xList = []
sList = []
nList = []
mList = []

for i in data:
    if data[i].name == 'Unnamed: 0':
        continue
    for j in data[i]:
        if (data[i].name == 'x'):
            xList.append(int (j))
        elif (data[i].name == 's'):
            sList.append(j)
        elif (data[i].name == 'n'):
            nList.append(int (j))
        elif (data[i].name == 'm'):
            mList.append(int(j))

for i in range(len(xList)):
    x = xList[i]
    s = sList[i]
    n = nList[i]
    m = mList[i]
    if 1 <= x <= 3:
        for i in range(n):
            print("Строка = ", s)
            print("N = ", i)
    elif 4 <= x <= 6:
        print(pow(x, m))
    elif 7 <= x <= 9:
        for i in range(10):
            x += 1
            print("x = ", x)
    else:
        print("Ошибка ввода")

    print('\n')








