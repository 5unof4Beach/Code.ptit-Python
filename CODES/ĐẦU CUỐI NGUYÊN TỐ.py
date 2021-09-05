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
    res1 = 0
    res2 = 0
    for i in range(len(n)-3,len(n)):
        res1 = res1*10 + int( n[i] )

    for i in range(0,3):
        res2 = res2*10 + int( n[i] )
    # print(res1)
    # print(res2)
    # print(res)
    if isPrime(res1) and isPrime(res2):
        print("YES")
    else:
        print("NO")