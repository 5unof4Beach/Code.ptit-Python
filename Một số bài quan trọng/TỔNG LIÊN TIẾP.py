# https://www.geeksforgeeks.org/count-ways-express-number-sum-consecutive-numbers/

def count(n):
    res = 0
    L = 1
    while (L * (L + 1) < 2 * n):
        a = (1.0 * n - (L * (L + 1)) / 2) / (L + 1)
        if (a - int(a) == 0.0):
            res += 1
        L += 1
    return res

n = int(input())
while n:
    n-=1
    num = int(input())
    print(count(num))