class Pet:
    def __init__(self, model, *args, **kwargs):
        super().__init__()
        self.model = model
        self.age = "8 age"

    def talk(self):
        print("rah, rah, rah!")


class Jump:
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.jump_height = "3m"

    def jump_height (self):
        print("jump_height 3m")


class Cat(Pet, Jump):
    def info(self):
        print(self.age)
        print(self.jump_height)
        print(self.model)

cat = Cat (model="Sphynx")
cat.info()


class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__()
        self.model = model
        self.RAM = "16 Gb"

    def calc(self):
        print("Calculate....")

