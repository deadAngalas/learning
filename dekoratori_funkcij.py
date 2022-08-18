# Декоратор - это функция, которая позволяет обернуть другую функцию для разширения ее функциональности без непосредственного изменения ее кода

def my_decor(func):  # аргумент - это наша функция, которую она будет оборачивать
    def wrapper(n):
        print('start')
        func(n)
        print('end')
    return wrapper

@my_decor
def my_func(number):   # декорируем функцию my_func
    print(number ** 2) 

my_func(4)

import time

def decorator(funkcija):
    def wr():
        start_time = time.time() # замерит время до выполнения функции
        funkcija()
        print(time.time() - start_time)
    return wr

@decorator
def sp():
    spisok = [i**2 for i in range(0, 100000) if i%2==0]
    print(spisok)

sp()