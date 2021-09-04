import math

def isPrime(n):
    if n>1:
        for i in range( 2,int(n/2) + 1):
            if n%i == 0:
                return 0
        return 1

t = int(input())
while t:
    t -= 1
    line = input()
    arr = line.split()
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    temp = math.gcd(arr[0],arr[1]);
    # print(temp)
    c = 0
    a = str(temp)

    for i in a:
        c += int(i)

    if(isPrime(c)):
        print("YES")
    else:
        print("NO")

