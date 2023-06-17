def lista_kwadratow(x):
    return list(map(lambda x: x ** 2, range(1, x+1)))

x = 7
result = lista_kwadratow(x)
print(result)