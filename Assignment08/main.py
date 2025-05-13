class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  
        self.subject = subject
        print("Teacher constructor called")

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)

t = Teacher("Sumbal", "Mathematics")
t.display()
