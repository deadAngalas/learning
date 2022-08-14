# Множества - структура данных, которая содержит неупорядочные элементы = (те, что непроиндексированны, не имеют свой порядковый номер и находятся в случайном порядке, уникальные=нет дубликантов, элекменты неизменяемы, но множества изменяемы)

numbers = {1, 2, 4, 67}
print(numbers)

numbers1 = {}
print(type(numbers1)) #просто пустые скобли это словарь, а не множество.

#надо использовать SET чтобы создать пустое множество

numbers2 = set()
print(type(numbers2))

numbers3 = set([1,2,3,4,2])
print(numbers3)

#методы к множествам

#доступ к элекментам множества

numbers4 = {1,2,3,4,5,6,7,8}
print(3 in numbers4) #пишет true or false находится ли она в множестве, благодаря IN


for i in numbers4: # позволяет вывести каждый элемент по очереди
   print(i)

numbers4.add(58)
numbers4.remove(2) # выдает ошибку, если нет данного элемента в списке
numbers4.discard(53) # не выдает ошибку, если нет элемента в списке или есть - не важно
numbers4.pop() #удаляет первые элемент множества
#numbers4.clear() удаляет все элементы
print(numbers4)

numbers5 = {2,4,6,8}

numbers6 = numbers4.union(numbers5) # обьеденяет 2 множества
print(numbers6)
numbers7 = numbers4 | numbers5 # также обьеденяет 2 множества
print(numbers7)

numbers8 = numbers4.intersection(numbers5)
print(numbers8) # вносит те элементы, которые есть и там и там (пересечение)
numbers9 = numbers4 & numbers5  # также пересечение
print(numbers9)

numbers10 = numbers4 - numbers5 # содержаться в 1, но не содержаться во 2
print(numbers10)

numbers11 = numbers4.copy() # копираует элементы из 1 множества в другое
print(numbers11) 

print(len(numbers4)) #возвращает длинну/количество элементов в множестве 

numbers12 = frozenset({4,8,4,3,6}) #создает множество, которые нельзя изменять вообще
print(numbers12)