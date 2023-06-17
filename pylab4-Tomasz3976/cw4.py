def generator_slow():
    word = 'spam'
    for i in range(1, len(word) + 1):
        yield word[:i]

print(list(generator_slow()))