class Counter:
    count = 0  

    def __init__(self):
        Counter.count += 1 

    @classmethod
    def display_count(cls):
        print("Total objects created:", cls.count)

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()
