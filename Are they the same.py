def comp(array1, array2):
    sort_arr1 = sorted(array1)
    sort_arr2 = sorted(array2)
    for i, x in enumerate(sort_arr1):
        if x*x != sort_arr2[i]:
            return False
    return True



a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(a1, a2))