class Animal():
    def __init__(self, type_of_animal, color, age, name):
        self.type_of_animal = type_of_animal
        self.color = color
        self._age = age
        self._name = name

        self.introduce()

    def introduce(self):
        print(f'Hello, I am a {self.type_of_animal}')



    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < self._age:
            print('Возраст кошки не может быть меньше текущего')
        else:
            self._age = new_age

class Cat(Animal):
    def __init__(self, color, age, name, breed):
        type_of_animal = 'cat'
        super().__init__(type_of_animal, color, age, name)
        self.breed = breed

        self.introduce_cat()

    def introduce_cat(self):
        print(f'My breed is {self.breed}')

    def making_sound(self):
        return 'Meow'

class Dog(Animal):
    def __init__(self, color, age, name, breed):
        type_of_animal = 'dog'
        super().__init__(type_of_animal, color, age, name)
        self.breed = breed

        self.introduce_dog()

    def introduce_dog(self):
        print(f'My breed is {self.breed}')

    def making_sound(self):
        return 'Woof'


animal1 = Animal('cat', 'black', 5, 'Chloe')

animal2 = Animal('dog', 'blue', 6, 'Musya')

cat1 = Cat('black', 5, 'Dusya', 'manchkin')

dog1 = Dog('black', 9, 'Usya', 'Corgie')

list_of_animals = [cat1, dog1]
for pet in list_of_animals:
    print(pet.making_sound())