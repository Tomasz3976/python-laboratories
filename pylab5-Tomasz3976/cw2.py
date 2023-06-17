class Student:
    def __init__(self, imie, nr_albumu):
        self.imie = imie
        self.nr_albumu = nr_albumu


adam = Student("Adam", 156473)
romek = Student("Roman", 142536)
wojtek = Student("Wojciech", 112445)

print(wojtek.imie)