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
    sum = 0
    for i in range(0,len(n)):
        sum += int(n[i])
    if(i % 2==0 and int(n[i])%2 == 1  ):
        flag = 0
    elif(i % 2 == 1 and int(n[i]) % 2 ==0):
        flag = 0

    if not isPrime(sum):
        flag = 0

    if flag:
        print("YES")
    else:
        print("NO")
