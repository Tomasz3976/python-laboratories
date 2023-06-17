import random


def deck():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    types = ['c', 'd', 'h', 's']

    d = []
    for a in cards:
        for b in types:
            d.append((a, b))
    return d


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def deal(deck, n):
    list = []
    for i in range(0, 5 * n, 5):
        list.append(deck[i:i + 5])
    return list


print(deck())
print(shuffle_deck(deck()))
print(deal(deck(), 3))