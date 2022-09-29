def dig_pow(n, p):
    sum = 0
    for num in str(n):
        sum += pow(int(num), p)
        p += 1
    if (sum/n) % 1 == 0:
        return True
    return -1

print(dig_pow(46288,3))