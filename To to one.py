def longest(a1, a2):
    temp = a1 + a2
    new_sentence = []
    for char in temp:
        if char not in new_sentence:
            new_sentence += char
    return ("".join(sorted(new_sentence)))

print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))


# def longest(s1, s2):
#     return ''.join(sorted((set(s1+s2))))