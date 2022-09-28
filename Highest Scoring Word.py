def high(s):
    alpha = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
        "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
        "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
    }    #można było urzyć funkcji ord
    values = []
    words = s.split(" ")
    for word in words:
        value_of_word = 0
        for letter in word:
            value_of_word += alpha[letter]
        print(value_of_word)
        values.append(value_of_word)
    return str(words[values.index(max(values))])
s= "zrczzrmwfy ytjun twgm ulpbkvldk yljzqsqicg mwt cibsqpplat nmcgcflmr diomiozfom mtmthstfa hxv fwcy nzkfytzg glvu dhwa ewxfgnayg"
print(high(s))

####Najciekawsze rozwiązanie####
# def high(x):
#     words=x.split(' ')
#     list = []
#     for i in words:
#         scores = [sum([ord(char) - 96 for char in i])]
#         list.append(scores)
#     return words[list.index(max(list))]