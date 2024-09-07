def mySqrt(x):
    p = 0.00001
    guess = x/2.0
    
    while abs(guess * guess - x) > p:
        guess = (guess + x / guess) / 2.0
    return int(guess)


print(mySqrt(8))