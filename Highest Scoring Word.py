def high(s):
    alpha = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
        "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "r": 17, "s": 18, "t": 19,
        "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25
    }
    values = []
    words = s.split(" ")
    for word in words:
        value_of_word = 0
        for letter in word:
            value_of_word += alpha[letter]
        print(value_of_word)
        values.append(value_of_word)
    return words[values.index(max(values))]
s= "what time are we climbing up the volcano"
print(high(s))