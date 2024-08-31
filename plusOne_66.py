def plusone(digits):
    number = int(''.join(map(str, digits)))
    
    org = number + 1
    digit_array = [int(digit) for digit in str(org)]
    
    return digit_array



print(plusone([9, 9, 9]))