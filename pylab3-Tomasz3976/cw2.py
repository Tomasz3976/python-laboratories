ilosc_znakow = int(input("Podaj ilość znaków: "))

tablica = []

for i in range(ilosc_znakow):
    znak = input("Podaj znak: ")
    tablica.append(znak)

print(tablica[::-1])