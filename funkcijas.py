def hello():
    print('Hello, World!')

x = int(input('Ввведите первое число: '))
y = int(input('Ввведите первое второе: '))

def sum(a,b):
    return a + b
z = (sum(x,y))

print(z)




##################################################

def f(a=2):
    return 2*a - 2

print(f(5))


##################################################


a=45
b=5

print(a)

def f():
    global a
    a = a+2
    print(a)

f()
