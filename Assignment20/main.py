class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        return "Age is valid."

try:
    age = 15
    print(check_age(age))
except InvalidAgeError as e:
    print(f"Error: {e}")
