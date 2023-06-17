class Liczba:
    def __init__(self, x):
        self.x = x

    def __operation__(self, other):
        return self.x ** 2 + 2 * self.x * other.x + other.x


liczba1 = Liczba(3)
liczba2 = Liczba(4)

print(liczba1.__operation__(liczba2))