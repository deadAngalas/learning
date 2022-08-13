# вызвать функцию open() - которая возвращает обьекты file (указать путь и имя файла и в каком режиме должен открыть)
#                           режимы - 1) только для чтения 2) для перезаписи (удалит старое) 3) для добавления
# вызвать метод read() или write() для обьекты file
# закрыть файл методом close()
# r - read - чтение      w - write - перезаписи     a - add - добавление


#f = open('1.txt', 'w') # f = это обьект файл
#f.write('Hello, file!')
#f.close

#f = open('1.txt', 'r') # f = это обьект файл
#print(f.read())
#f.close

with open('1.txt', 'a') as f: # with позволяет забыть про закрытие файла
    f.write('Who are you?')

