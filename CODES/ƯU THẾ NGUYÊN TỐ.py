import itertools
import math


def isPrime(n):
    if n < 2:
        return False
    for i in itertools.islice(itertools.count(2) , int(math.sqrt(n)-1)):
        if n % i ==0:
            return False
    return True

t = int(input())
while t:
    t -= 1
    n = input()
    flag = 1
    c=0
    if( not isPrime(len(n)) ): flag = 0
    for i in n:
        if isPrime( int(i) ): c += 1
    if c<= len(n) - c: flag = 0

    if flag: print("YES")
    else: print("NO")
