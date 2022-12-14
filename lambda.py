# лямбда выражения или анонимные функции 
# лямба создает функцию, которая возвращает сам обьект функции, не присваивая ему имени
# появляется там, где синтаксис python не позволяет использовать функцию def
# не может содержать в себе больше 1 строки

print((lambda a,b: a*b)(13,14))

def max(a,b):
    if a>b:
        return(f'Число {a} больше, чем {b}')
    else:
        return(f'Число {b} больше, чем {a}')

print(max(5,2))

print((lambda a,b: a if a>b else b)(54,786)) # после : указывает, что вернуть if действие  потом что вернуть 2     потом аргументы

#1) Написать lambda-функцию, принимающую 1 аргумент — сторону квадрата, и возвращающую периметр квадрата.
print((lambda a: a*4) (3))
#2) Написать lambda-функцию, которая выводит среднее арифметическое 3 чисел.
print((lambda a,b,c: ((a+b+c)/3))(4,6,8))