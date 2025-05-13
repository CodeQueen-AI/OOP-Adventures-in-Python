class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start_engine(self):
        return f"{self.engine_type} engine started!"

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine 

    def start_car(self):
        print(f"Car model: {self.model}")
        print(self.engine.start_engine()) 

my_engine = Engine("V8")

my_car = Car("Mustang", my_engine)

my_car.start_car()
