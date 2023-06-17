def suma_listy(lista):
    wynik = 0
    for x in lista:
        wynik += x
    return wynik

def wczytaj_liczby(suma):
    lista = []
    with open('liczby.txt') as liczby:
        for linia in liczby:
            lista.append(int(linia.strip('\n')))
        return suma(lista)

print(wczytaj_liczby(suma_listy))