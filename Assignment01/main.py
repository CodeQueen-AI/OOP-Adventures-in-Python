class Student:
    def __init__(self, name, marks):
        self.name = name       
        self.marks = marks     

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Create an object of Student
student1 = Student("Ali", 90)
student1.display()
