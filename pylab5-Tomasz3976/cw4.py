class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Student(Osoba):
    def __init__(self, imie, nazwisko, nr_albumu):
        super().__init__(imie, nazwisko)
        self.nr_albumu = nr_albumu

    def przywitanie(self):
        print("Cześć nazywam się {} {} i mój numer albumu to {}".format(self.imie, self.nazwisko, self.nr_albumu))


bartek = Student("Bartosz", "Michalski", 123421)
bartek.przywitanie()