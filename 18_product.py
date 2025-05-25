class Product:
    def _init_(self, price):
        self._price = price  # private attribute

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
        print("Price has been deleted.")
        del self._price


# Example usage
p = Product(100)
print(p.price)

p.price = 150
print(p.price)

p.price = -50

del p.price