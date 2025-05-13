class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name      
        self._salary = salary   
        self.__ssn = ssn  

    def show_info(self):
        print("Inside Class:")
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)

emp = Employee("CodeQueen", 50000, "123-45-6789")

print("Public Name:", emp.name)       

print("Protected Salary:", emp._salary)  

# Access private variable (will raise an error)
try:
    print("Private SSN:", emp.__ssn)   
except AttributeError as e:
    print("Error accessing private SSN:", e)

# Access private variable the proper (not recommended) way
print("Private SSN (via name mangling):", emp._Employee__ssn) 

emp.show_info()
