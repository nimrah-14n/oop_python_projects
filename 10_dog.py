Class Dog:
     def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def brak(self):
        print(f"{self.name} is says woof")

d = Dog("Rex", "German Shpered")

d.brak()