def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls 

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
        
person = Person("CodeQueen")

print(person.greet()) 
