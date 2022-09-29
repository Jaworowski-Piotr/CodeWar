def create_phone_number(n):
    new_string = "".join(map(str, n))
    return  f"({new_string[:3]}) {new_string[3:6]}-{new_string[6:]}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))