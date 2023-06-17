import random

def lotto():
    list = []
    for i in range(6):
        list.append(random.randint(1, 49))
    return list

print(lotto())

