class Dog:
    count = 0  # this is a class variable
    dogs = []  # this is a class variable

    def __init__(self, name):
        self.name = name  # self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n):  # this is an instance method
        print("{} says: {}".format(self.name, "woof! " * n))

    @staticmethod
    def print_dogs():
        print("Liczba piesków wynosi: {}\n".format(Dog.count))
        print("Ich imiona to:")
        for i in range(len(Dog.dogs)):
            print(Dog.dogs[i])


burek = Dog("Burek")
reksio = Dog("Reksio")
pundzel = Dog("Pundzel")

Dog.print_dogs()
