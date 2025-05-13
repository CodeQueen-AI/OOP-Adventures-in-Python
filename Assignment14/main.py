class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"{self.name} is a {self.position}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee 

    def show_department_info(self):
        print(f"Department: {self.dept_name}")
        print(self.employee.get_details()) 

emp1 = Employee("CodeQueen", "Software Engineer")

dept = Department("IT", emp1)

dept.show_department_info()
