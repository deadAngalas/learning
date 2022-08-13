age = int(input('Введи свой возраст: '))

if (age >= 18) and (age <25):
    print('Разрешено только с родителями!')
elif (age >= 25):
    print('Разрешено!')
else:
    print('Запрещено!')