print("KALKULATOR!!!")
print("Dostepne operacje:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnozenie")
print("4. Dzielenie")
print("5. Zakoncz dzialanie programu")

while True:
        operation = int(input("Wprowadz numer operacji: "))
        a = int(input("Wprowadz liczbe a: "))
        b = int(input("Wprowadz liczbe b: "))
        if operation == 1:
                print("Wynik dodawania: ")
                print(a + b)
        if operation == 2:
                print("Wynik odejmowania: ")
                print(a - b)
        if operation == 3:
                print("Wynik mnozenia: ")
                print(a * b)
        if operation == 4:
                print("Wynik dzielenia: ")
                print(a / b)
        if operation == 5:
                print("Koniec działania programu!")
                break
