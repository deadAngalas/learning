# генератор коллекций (списка, множеств, словарей) называются включения
# инструкция создания 1)  ставим [] скобки так как создаем список
# 2) идет финальное выражение- то чем будет заполнятся список [x**3]
# 3) идет коллекция - может быть любой итерируемый обьект (то откуда берем финальные выражние)[x**3 for x in range(10)]
# 4) идет условие [x**3 for x in range(10) if x%2 == 0]

s1 = [i for i in range(1,21) if i%5 == 0]
print(s1)

s = []
[s.append(x) for x in range(1,21) if x%5 == 0]
print(s)

print(sum([i**3 for i in range(1,21) if i%5 == 0]))

s2 = []
for k in range(1,21):
    for i in range(1,51):
        s2.append((k, i))
print(s2)

s3 = [(k,i) for k in range(1,21) for i in range(1,51)]
print(s3)

s4 = [i**2 
    if i>0 
    else i**3 
    for i in range(-10,11) 
    if i%2 == 0]
print(s4)

s5 = [7,7,3,3,1,1,1,1]
set_set = {i for i in s5}
print(set_set) #кортеж

dict = {i: i**2 for i in s5}
print(dict) # словарь