def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b,a%b)

def isCoprime(a,b):
    if gcd(a,b) == 1:
        return 1
    return 0
t = int(input())
while t:
    t-=1

    n = input()

    n2 = 0
    for i in range(len(n)-1,-1,-1):
        n2 = n2*10 + int(n[i])

    if isCoprime(int(n),n2):
        print("YES")
    else:
        print("NO")