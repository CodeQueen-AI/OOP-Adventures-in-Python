class Dog:
    def __init__(self, name, breed):
        self.name = name      
        self.breed = breed   

    def bark(self):          
        print(f"{self.name} says: Woof woof!")

my_dog = Dog("Bruno", "Labrador")

my_dog.bark()
