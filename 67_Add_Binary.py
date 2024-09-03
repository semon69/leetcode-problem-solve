def addBinary(a: str, b: str):
    number = int(a, 2) + int(b, 2)
    return bin(number)[2:]

print(addBinary("1010", "1011"))