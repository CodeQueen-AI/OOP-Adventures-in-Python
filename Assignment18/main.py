class Product:
    def __init__(self, price):
        self._price = price 

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value  

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price  

product = Product(100)

print(f"Product price: ${product.price}")

product.price = 120
print(f"Updated product price: ${product.price}")

product.price = -50

del product.price
