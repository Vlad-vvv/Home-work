class Pet:
    count_of_pet = 0
    def __init__(self, name=None, weight = 10, cuteness = 10):
        self.name = name
        self.weight = weight
        self.cuteness = cuteness
        Pet.count_of_pet += 1

    def grow(self, weight=1):
        self.weight += weight

    def cute_grow(self, cute=1):
        self.cuteness -= cute

    def __str__(self):
        return f'Привіт. Це {self.name}, моя вага  {self.weight} кг, моя милота {self.cuteness} '

    def __del__(self):
        print(f'Привіт. Я {self.name}, я пішов ')

Cooper = Pet(name='Cooper', weight=10, cuteness=10)
print(Cooper)
print(Pet.count_of_pet)
Cooper.grow(5)
Cooper.cute_grow(3)
print(Cooper.weight)
print(Cooper.cuteness)
