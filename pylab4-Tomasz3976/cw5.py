def równanie_kwadratowe(a, b, c):
    x1 = (-b + (b**2 - 4*a*c) ** 0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c) ** 0.5) / (2*a)
    return x1, x2

def dekorator(func):
    def wrap(a, b, c):
        równanie = f"{a}x^2 + {b}x + {c}"
        print(f"Równanie: {równanie}")
        wynik = func(a, b, c)
        return wynik
    return wrap

udekorowana_funkcja = dekorator(równanie_kwadratowe)
wynik = udekorowana_funkcja(1, -3, 2)
print(f"Wynik: {wynik}")