def summa(a,b,c):  # позиционные аргументы
    print(a+b+c)
summa(5,6,7)

def summa1(a,b=6,c=8):
    print(a+b+c)
summa1(3)

def summa2(a,b=7,c=8):  # именованые аргументы
    print(a,b,c)
summa2(c=1,b=80,a=70)


# оператор * способен вытаскивать из обьектов состовляющие их элементов
# *args к позиционным (кортеж)  *kwargs к именованным (сл)
# используется для вызова списка неопределенный длинны
def summa3(*numbers): #не важно как назовем, например, args, главное чтобы было звезда
    print(sum(numbers))
summa3(7,8,3,7,2)

def brand(**brands):
    for x,y in brands.items(): # x,y - перебирает пары ключ-значение и items вернер пары ключ/значение в виде кортежей
        print(x, ':', y)
brand(a='Apple', b = 'Samsung')

# a b c d
# *
# c d b a
# **