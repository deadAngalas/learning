print('Privet\tPrivet\nPri\"Hello\"vet\n"текст в кавычках"') # \n делает новый абзац    \t делает 4 проблема либо 1 табуляцию

text = "privet mir kyda idew"
text1 = "Mir"
print(text + ' ' + text1) # склаывает две строки

print(text1*3) # повторит строку 3 раза

print(text.upper()) # все большие буквы
print(text.lower()) # все маленькие буквы
print(text.capitalize()) #с  большой буквы

print(text.split(" ")) # разбивает строчку на обьекты в список - надо указать при каком элементе разбивать

spisok = ['a', 'b', 'c']

print(','.join(spisok)) # соединяет обьекты в строку - надо указать как соединять

text2 = '   Biba i Boba   '
print(text2.strip()) # удаляет все пробелы в начале и конце строки

print(text2.lstrip()) # удаляет пробелы в начале строки
print(text2.rstrip()) # удаляет пробелы в конце строки

text4 = 'lolololololo'
print(text4.replace('l', 'o')) # заменяет элемент на другой - надо указать что заменяем на что.