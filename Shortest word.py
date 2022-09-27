def find_short(s):
    spilt_list = s.split(" ")
    new_list = []
    for word in spilt_list:
        new_list.append(len(word))
    l = min(new_list)
    return l

s = "bitcoin take over the world maybe who knows perhaps"
print(find_short(s))