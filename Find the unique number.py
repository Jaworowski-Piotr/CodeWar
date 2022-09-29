def find_uniq(arr):

    for i, n in enumerate(arr):
        print(f"{i}   {n}")
        if n != arr[i+1]:
            return arr[i+1]

print((find_uniq([ 1, 1, 1, 1, 1, 2])))