class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Chiwawa(Dog):
    def __init__(self, name, age, abbaiaSempre='dipende'):
        super().__init__(name, age)
        self.abbaiaSempre = abbaiaSempre



buddy = Chiwawa("Buddy", 9, 'si')
print(buddy.abbaiaSempre)


pippo = Chiwawa("Buddy", 9)
print(pippo.abbaiaSempre)