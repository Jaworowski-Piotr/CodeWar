
def productFib(prod):
    a = 0
    b = 1
    while prod > a * b:
        c = a + b
        a = b
        b = c
    return [a, b, prod == a * b]

print(productFib(4895))