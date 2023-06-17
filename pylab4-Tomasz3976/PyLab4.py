from itertools import product, permutations

letters = ("A", "B", "C")
print(list(product(letters, range(3))))
print(list(permutations(letters)))