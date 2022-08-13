while True:
    try:
        a = int(input('Впиши число: '))
        b = int(input('Впиши число: '))
        print(a/b) 
    except ZeroDivisionError:
        print('На 0 делить нельзя')

# надо предупредить кента, чтобы не вводил 0 (try, except)