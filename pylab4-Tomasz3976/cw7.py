def operacje():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    # Sprawdzenie zawartości zbiorów
    print("Zbior 1:", set1)
    print("Zbior 2:", set2)

    # Operacje na zbiorach
    suma = set1 | set2  # suma zbiorów
    czesc_wspolna = set1 & set2  # część wspólna zbiorów
    roznica = set1 - set2  # różnica zbiorów
    roznica_symetryczna = set1 ^ set2  # różnica symetryczna zbiorów

    # Wyświetlenie wyników operacji
    print("Suma:", suma)
    print("Czesc wspolna:", czesc_wspolna)
    print("Roznica:", roznica)
    print("SRoznica symetryczna:", roznica_symetryczna)

    # Sprawdzenie przynależności elementów do zbiorów
    element1 = 3
    element2 = 6
    print(f"Czy {element1} znajduje się w zbiorze 1?", element1 in set1)
    print(f"Czy {element2} znajduje się w zbiorze 2?", element2 in set1)
    print(f"Czy {element2} znajduje się w zbiorze 2?", element2 in set2)

    # Modyfikacja zbioru
    set1.add(6)  # dodanie elementu do zbioru
    set2.remove(8)  # usunięcie elementu ze zbioru

    # Wyświetlenie zaktualizowanych zbiorów
    print("Zaktualizowany zbior 1:", set1)
    print("Zaktualizowany zbior 2:", set2)

operacje()