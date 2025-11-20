class Animal():
    def __init__(self, name, species, age, sound, zoo_name):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        self.zoo_name = zoo_name

    def __str__(self):
        return (f"{self.name} is from {self.species} species.\nhe/she is {self.age} years old.\nthe {self.name}"
                f" sounds like {self.sound}, now he/she is living in {self.zoo_name} zoo")

    def make_sound(self):
        print(f"the {self.name} sounds like {self.sound}")

    def info(self):
        print(f"{self.name} is from {self.species} species.\nhe/she is {self.age} years old.")


lion = Animal("lion", "Felidae", 21, "Roar", "myZoo")

lion.info(), lion.make_sound()


class Bird(Animal):
    def __init__(self, name, species, age, sound, zoo_name, wing_span):
        Animal.__init__(self, name, species, age, sound, zoo_name)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} sounds amazing, they {self.sound}")


cockatiel = Bird("Cockatiel", "Bird", 4, "singing", "myZoo", 14)
print('------')
cockatiel.info()
print('------')
print(str(cockatiel))