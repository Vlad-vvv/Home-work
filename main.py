import random


class Pet:
    count_of_pet = 0
    def __init__(self, name=None, weight = 10, cuteness = 10, age = 3, bread = None):
        self.name = name
        self.weight = weight
        self.cuteness = cuteness
        self.age = age
        self.bread = bread
        Pet.count_of_pet += 1

    def grow(self, weight=1):
        self.weight += weight

    def cute_grow(self, cute=1):
        self.cuteness -= cute

    def age(self, age=1):
        self.age += 1

    def __str__(self):
        return f'Привіт. Це {self.name}, моя вага  {self.weight} кг, моя милота {self.cuteness}, мені {self.age}, {self.bread} '

    def __del__(self):
        print(f'Привіт. Я {self.name}, я пішов ')


bread_of_dog = {"Акита-ину", "Алабай", "Басенджі", }


class bread:
    def __init__(self, bread_of_dog):
        self.bread = random.choice(list(bread_of_dog))


name_list = {"Шарік", "Тузик", "Бублік", }

class name:
    def __init__(self, name_list):
        self.name = random.choice(list(name_list))

Cooper = Pet(name=name, weight=10, cuteness=10, age=5, bread=bread)
print(Cooper)
print(Pet.count_of_pet)
Cooper.grow(5)
Cooper.cute_grow(3)
print(Cooper.weight)
print(Cooper.cuteness)
print(Cooper.bread)
