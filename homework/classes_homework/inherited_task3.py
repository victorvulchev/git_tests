#Cat = Miauuu!, Tomcat = Miau!, Kitten = Miauuuuuu!, Dog = Bauuu!, Frog = Kwak!
class Animal():
    def __init__(self, age, name, gender) -> None:
        self.age = age
        self.name = name
        self.gender = gender
    
    def make_sound(self):
        return "sound"
    
class Cat(Animal):
    def __init__(self, age, name, gender) -> None:
        super().__init__(age, name, gender)
    def make_sound(self):
        return "Miauuu!"
class Tomcat(Animal):
    def __init__(self, age, name, gender) -> None:
        super().__init__(age, name, gender)
    def make_sound(self):
        return "Miau!"
class Kitten(Animal):
    def __init__(self, age, name, gender) -> None:
        super().__init__(age, name, gender)
    def make_sound(self):
        return "Miauuuuuu!"
class Dog(Animal):
    def __init__(self, age, name, gender) -> None:
        super().__init__(age, name, gender)
    def make_sound(self):
        return "Bauuu!"
class Frog(Animal):
    def __init__(self, age, name, gender) -> None:
        super().__init__(age, name, gender)
    def make_sound(self):
        return "Kwak!"
    
number_of_animals = int(input("Enter number of animals:"))
animal_list = []
for i in range(number_of_animals):
    current_line = input("Enter info:")
    current_list = current_line.split(" ")
    species = current_list[0]
    name = current_list[1]
    age = current_list[2]
    gender = current_list[3]
    if species == "Cat":
        species = Cat(age, name, gender)
    elif species == "Tomcat":
        species = Cat(age, name, gender)
    elif species == "Kitten":
        species = Kitten(age, name, gender)
    elif species == "From":
        species = Frog(age, name, gender)
    else:
        species = Dog(age, name, gender)
    animal_list.append(species)

for i in animal_list:
    print(f"{i} {i.make_sound()}")
    