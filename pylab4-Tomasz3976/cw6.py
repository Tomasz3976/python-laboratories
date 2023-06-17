def newton(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return newton(n-1, k-1) + newton(n-1, k)

n = 5
k = 2
wynik = newton(n, k)
print(f"Wartosc symbolu Newtona dla n={n}, k={k}: {wynik}")