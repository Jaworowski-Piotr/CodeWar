def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    numbers_of_vowels = 0
    for char in sentence:
        if char in vowels:
            numbers_of_vowels +=1
    return numbers_of_vowels

print(get_count("abracadabra"))