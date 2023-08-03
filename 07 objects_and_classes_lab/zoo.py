class Zoo:

    def __init__(self, zoo_name):
        self.__animals = 0
        self.zoo_name = zoo_name
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
        names = []
        print_species = ""

        if species == "mammal":
            print_species = "Mammals"
            names = self.mammals
        elif species == "fish":
            print_species = "Fishes"
            names = self.fishes
        elif species == "bird":
            print_species = "Birds"
            names = self.birds

        return f"{print_species} in {self.zoo_name}: {', '.join(names)}\nTotal animals: {self.__animals}"


the_zoo_name = input()
lines = int(input())

zoo = Zoo(the_zoo_name)

for _ in range(lines):
    new_animal = input().split()
    current_species = new_animal[0]
    current_name = new_animal[1]
    zoo.add_animal(current_species, current_name)

species_check = input()
print(zoo.get_info(species_check))
