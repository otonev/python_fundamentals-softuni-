#!/usr/bin/env/python
class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        species = species[0].upper()+species[1::]
        if species == "Mammal":
            return f"{species}s in {self.name}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"
        elif species == "Fish":
            return f"{species}s in {self.name}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}"
        elif species == "Bird":
            return f"{species}s in {self.name}: {', '.join(self.birds)}\nTotal animals: {self.__animals}"


name = input()
zoo = Zoo(name)
n = int(input())
for _ in range(n):
    tokens = input().split()
    species = tokens[0]
    name = tokens[1]
    zoo.add_animal(species, name)
species = input()
print(zoo.get_info(species))
