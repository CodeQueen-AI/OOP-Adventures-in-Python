class Countdown:
    def __init__(self, start):
        self.start = start  # Set the starting number
        self.current = start  # Initialize the current number

    def __iter__(self):
        # __iter__ returns the iterator object itself
        return self

    def __next__(self):
        # __next__ defines the logic for the iteration
        if self.current > 0:
            self.current -= 1  # Countdown
            return self.current + 1  # Return the current number before decrementing
        else:
            raise StopIteration  # Stop when the countdown reaches 0

# Create a Countdown object starting from 5
countdown = Countdown(5)

# Iterate using a for-loop
for number in countdown:
    print(number)
