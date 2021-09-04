t = int(input())
import math
import itertools
while t:
    t-=1
    def isPrime(n):
        if n < 2 :
            return 0
        for i in itertools.islice(itertools.count(2),int(math.sqrt(n)-1)):
            if n % i ==0:
                return 0
        return 1

    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if isPrime(sum):
        print("YES")
    else:
        print("NO")