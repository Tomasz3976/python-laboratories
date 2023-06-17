from math import pi

def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    return x / y

def pole_kola(r):
    return pi * r * r

def obwod_kola(r):
    return 2 * pi * r


print("KALKULATOR!!!")
print("Dostepne operacje:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnozenie")
print("4. Dzielenie")
print("5. Pole kola")
print("6. Obwod kola")
print("7. Zakoncz dzialanie programu")

while True:
    operacja = int(input("Wprowadz numer operacji: "))

    if operacja == 7:
        print("Koniec działania programu!")
        break

    if operacja == 1 or operacja == 2 or operacja == 3 or operacja == 4:
        a = float(input("Wprowadz liczbe a: "))
        b = float(input("Wprowadz liczbe b: "))

        if operacja == 1:
             print("Wynik dodawania: ")
             print(dodawanie(a, b))
        if operacja == 2:
             print("Wynik odejmowania: ")
             print(odejmowanie(a, b))
        if operacja == 3:
            print("Wynik mnozenia: ")
            print(mnozenie(a, b))
        if operacja == 4:
            print("Wynik dzielenia: ")
            print(dzielenie(a, b))

    if operacja == 5 or operacja == 6:
        r = float(input("Wprowadz dlugosc promienia: "))

        if operacja == 5:
            print("Pole kola: ")
            print(pole_kola(r))
        if operacja == 6:
            print("Obwod kola: ")
            print(obwod_kola(r))