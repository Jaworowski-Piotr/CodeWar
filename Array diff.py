def array_diff(a, b):
    temp = []
    for x in a:
        if x not in b:
            temp.append(x)
    return temp

    # return [x for x in a if x not in b]

print(array_diff([1,1,2,2,2,2,2,2], [2]))