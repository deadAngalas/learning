spisok = []
names = ['Kesha', 'Zoro', 'Boba']

names.append('Biba')
names.pop()

n = names.index('Zoro')


print(names)
print(len(names))

for i in names:
    print(i)




numbers = [91, 29, 42, 4246, 643]

numbers.sort(reverse= True)
print(numbers)

numbers[0] = 'SKAM'
numbers.sort()
print(numbers)

