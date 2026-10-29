class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: Rs.{self.price}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __add__(self, other):
        return self.price + other.price

    def __sub__(self, other):
        return self.price - other.price


p1 = Product("Pen", 20)
p2 = Product("Book", 50)

print(str(p1))
print(repr(p1))
print(len(p1))
print(p1 == p2)
print(p1 < p2)
print(p1 > p2)
print(p1 + p2)
print(p2 - p1)