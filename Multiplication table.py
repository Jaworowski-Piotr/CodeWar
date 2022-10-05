def multiplication_table(size):
    arr = []
    for row in range(size):
        arr.append([])
        for columns in range(size):
            arr[row].append((row +1)*(columns +1))
    return arr


print(multiplication_table(size = 3))