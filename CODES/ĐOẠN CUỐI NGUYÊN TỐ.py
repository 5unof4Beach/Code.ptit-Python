t = int(input())
import math
import itertools
def isPrime(n):
    if n < 2:
        return 0
    for i in itertools.islice(itertools.count(2), int(math.sqrt(n) - 1)):
        if n % i == 0:
            return 0
    return 1


while t:
    t-=1
    flag = 1
    n = input()
    res = 0
    for i in range(len(n)-4,len(n)):
        res = res*10 + int( n[i] )

    # print(res)
    if isPrime(res):
        print("YES")
    else:
        print("NO")