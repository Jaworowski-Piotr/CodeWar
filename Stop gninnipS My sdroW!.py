def spin_words(sentence):
    temp = []
    for word in sentence.split(" "):
        if len(word) >= 5:
            temp.append(word[::-1])
        else:
            temp.append(word)
    print(" ".join(temp))
    return None


sentence = "Welcome to a jungle"
spin_words(sentence)