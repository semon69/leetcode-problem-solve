def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev2, prev1 = 1, 2
    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1


print(climbStairs(6))