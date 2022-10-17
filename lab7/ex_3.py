import json
from collections import namedtuple

def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())

with open('ex_3.json') as f:
    templates = f.read()

#print(templates)
studObj = json.loads(templates, object_hook=customStudentDecoder)

print(studObj)
print('\n')

x = int(studObj.x)
s = studObj.s
n = int(studObj.n)
m = int(studObj.m)


to_json = ''
if 1 <= x <= 3:
    for i in range(n):
        to_json += "Строка = " + str(s) + '\n'
        to_json += "N = " + str(i) + '\n'
elif 4 <= x <= 6:
    to_json += str(pow(x, m))
elif 7 <= x <= 9:
    for i in range(10):
        x += 1
        to_json += str("x = " + str(x))
else:
    to_json += str("Ошибка ввода")

with open('answer_ex_3.json', 'w') as f:
    f.write(json.dumps(to_json))