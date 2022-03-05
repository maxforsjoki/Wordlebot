import pandas as pd
def frequencies():
    letters = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        letters[letter] = 0

    file = open('sgb-words.txt', 'r')
    words = file.read().splitlines()
    for word in words:
        for letter in word:
            letters[letter]+=1
    return letters

letters = frequencies()
letters = {k: v for k, v in sorted(letters.items(), key=lambda item: item[1], reverse = True)}
print(letters)