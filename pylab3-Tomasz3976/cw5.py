from collections import Counter


def histogram(path):
    letters = [ch for ch in open(path).read() if ch != '\n' if ch != ' ']
    print(letters)
    letter_counts = Counter(letters)
    letter_counts.most_common()
    return letter_counts


print(histogram("text.txt"))