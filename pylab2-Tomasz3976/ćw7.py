from math import sqrt

a = float(input("Wprowadz parametr a: "))
b = float(input("Wprowadz parametr b: "))
c = float(input("Wprowadz parametr c: "))

delta = (b * b) - (4 * a * c)

if (delta < 0):
    print("Rownanie nie posiada rozwiazan w zbiorze liczb rzeczywistych")
else:
    rozw1 = (-b - sqrt(delta)) / (2*a)
    rozw2 = (-b + sqrt(delta)) / (2*a)

    try:
        with open('results.txt', 'a') as wyniki:
            wyniki.write("\nRozwiazania rownania {}x^2 + {}x + {} to:".format(a, b, c))
            wyniki.write('\n' + str(rozw1) + ' oraz ' + str(rozw2))
    finally:
        wyniki.close()