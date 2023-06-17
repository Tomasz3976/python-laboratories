class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Student(Osoba):
    def __init__(self, imie, nazwisko, nr_albumu):
        super().__init__(imie, nazwisko)
        self.nr_albumu = nr_albumu


marek = Student("Marek", "Nowak", 115643)
jacek = Student("Jacek", "Baran", 118743)
dominik = Student("Dominik", "Komsa", 123453)

print(marek.imie)
print(marek.nazwisko)
print(marek.nr_albumu)
print(jacek.imie)
print(jacek.nazwisko)
print(jacek.nr_albumu)
print(dominik.imie)
print(dominik.nazwisko)
print(dominik.nr_albumu)
