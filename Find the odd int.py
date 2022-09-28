import numpy as np

def find_it(seq):
    np_array = np.unique(seq)
    print(np_array)
    for num in np_array:
        if seq.count(num)% 2:
            return num

print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
