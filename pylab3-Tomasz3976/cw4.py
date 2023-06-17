import numpy as numpy

def wypełnianie():
    tablica = numpy.array([[2,3,4,5,6],
                           [0,0,0,0,0],
                           [0,0,0,0,0],
                           [0,0,0,0,0],
                           [0,0,0,0,0]])
    i = 1

    while i<5:
        for l in range (5):
            tablica[i][l] = pow(tablica[i-1][l],2)
        i += 1
    return tablica

print(wypełnianie())