import random

tablica = []

for i in range(5):
    liczba = random.randint(-5, 5)
    tablica.append(liczba)

with open("result.txt", "w") as file:
    for liczba in tablica:
        file.write(str(liczba) + "\n")