class Multiplier:
    def __init__(self, factor):
        self.factor = factor 

    def __call__(self, number):
        return number * self.factor  

# Create a Multiplier instance with a factor of 5
multiply_by_five = Multiplier(5)

print(callable(multiply_by_five))  

result = multiply_by_five(10) 
print(f"10 multiplied by 5 is: {result}")
