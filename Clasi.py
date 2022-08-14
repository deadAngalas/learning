class House(): # СУПЕР КЛАСС
    """Описание дома""" # документирование класса
    def __init__(self, street, number): #метод, который автоматически выполняется при создании каждого нового экземпляра на базе класса
        """свойства дома"""
        self.street = street
        self.number = number
        self.age = 0

    def build (self):
        """строит дом"""
        print(f'Дом на улице {self.street} под номером {self.number} построен')
        print('Дом на улице ' + self.street + ' под номером ' + str(self.number) + ' построен')

    def age_of_house (self, year):
        """возраст дома"""
        self.age += year

House1 = House('Тарту', 5)
House2 = House('Пушкина',3)

print(House2.number)

House1.build()

print(House1.age)

House1.age_of_house(5)
print(House1.age)

class ProspectHouse(House): #указываем класс родителя в скобках  СУБ КЛАСС
    """дома на проспекте"""
    def __init__(self, prospect, number):
        super().__init__(self,number) #супер - позволяет связать родителя и потомка
        self.prospect = prospect

PrHouse = ProspectHouse('Ленина', 53)

print(PrHouse.prospect)
