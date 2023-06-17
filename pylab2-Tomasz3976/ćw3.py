def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    return x / y


print("KALKULATOR!!!")
print("Dostepne operacje:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnozenie")
print("4. Dzielenie")
print("5. Zakoncz dzialanie programu")

while True:
    operacja = int(input("Wprowadz numer operacji: "))

    if operacja == 5:
        print("Koniec działania programu!")
        break

    a = int(input("Wprowadz liczbe a: "))
    b = int(input("Wprowadz liczbe b: "))

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