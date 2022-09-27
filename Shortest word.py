def find_short(s):
    new_list = s.split(" ")
    print(new_list)
    numerki = []
    for word in new_list:
        numerki.append(len(word))
    l = min(numerki)
    return l

s = "bitcoin take over the world maybe who knows perhaps"
print(find_short(s))