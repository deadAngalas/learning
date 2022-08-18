# область видемости переменных
# 1) встроенная область видемости build in 2) глобальные (те, что есть .py) 3) локальные (те, что внутри функции) 4) enclosing (обьемлющая)

import builtins
print(dir(builtins)) #встроенные

y = 2
def degree(x):
    return y**x  # используем глобальную переменнуую

print(degree(3))



def degree(x):
    y = 4
    return y**x  

print(degree(3))


def degree(x): #обьемлющая
    y = 3
    def degree_two(): #вложенная функция
        return y**x
    return degree_two

print(degree(5))

# инкапсуляция - прием, когда надо защитить или скрыть функцию от всего, что происходил за ее пределами

def message(number):
    def print_message():
        return 'Число' + str(number)
    return print_message

print(message(78))

# замыкания - динамически созданные функции, которые возвращаеются другими функциями

def message(x):
    def print_message(y):
        return x,y
    return print_message

d = message(7) # запоминает 7, так как есть живая ссылка
print(d(5))