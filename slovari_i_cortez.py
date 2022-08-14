#tuple = кортеж

spisok = [1,2,6,3,5,2,5]
print(type(spisok[1]))

print(tuple(['Hello', 46, 90]))

print(list((3,53,77,)))

dict = {'Яблоко': 'Красное', 'Банан': 'Желтый', 'Лимон': 'Желтый'}
for i in dict.keys():
    print(i)

del (dict['Лимон'])
print(dict)

print(dict['Банан'])